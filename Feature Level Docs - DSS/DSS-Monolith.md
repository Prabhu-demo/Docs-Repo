# Feature Documentation

## SH Validations & Consideration Amount Checks
### 1. Overview
This feature validates first-party details, reference IDs, and consideration vs. stamp duty amounts before proceeding with further stamp duty processing. It ensures data integrity, prevents invalid requests, and enforces business/legal rules.

---

### 2. First Party Validations
- Internal validation only (no Shield API call at this stage).
- If the first party name is not registered, throw an error: “**First party name used in the request is not registered.**”
- On success, proceed to collect additional document-related validations.

---

### 3. Reference ID Validation
- Each request must include a reference ID.
- If missing, throw error: “Reference ID is required.”
- All requests and responses are logged in API logs for traceability.
- Logs capture: reference ID, request body, and response.

---

### 4. Consideration Amount vs. Stamp Duty Validation
#### 4.1 Configuration
- Validation is controlled by organization-level configuration:
- If enabled → enforce rules.
- If disabled → client can pass any values.
#### 4.2 Rules
- General Rule:
- The consideration amount must always be greater than the stamp duty amount.
- Multi-Request Handling:
- If multiple stamp amounts are passed in an array for the same document:
- Pick the maximum stamp duty amount from the array.
- Compare it against the consideration amount.
- If consideration ≤ max stamp duty → throw error.
- Single Request Handling:
- Compare the single stamp duty amount against the consideration amount.
- If consideration ≤ stamp duty → throw error.
#### 4.3 Special Condition
- If stamp duty > ₹3,000 and consideration amount = 0 → throw error:
“Consideration amount cannot be zero if stamp duty exceeds ₹3,000.”
- If stamp duty < ₹3,000 and consideration ≤ stamp duty → throw error.

---

### 5. Error Handling
- Errors are logged in API logs with reference ID and request details.
- Error codes/messages are not yet standardized; documentation effort is ongoing to unify them.

---

### 6. Decision Points from Meeting
- First-party validation is internal (no external API call).
- Reference ID is mandatory and logged.
- Consideration vs. stamp duty validation depends on configuration.
- Multi-request arrays require max stamp duty comparison.
- Special condition: consideration cannot be zero if stamp duty > ₹3,000.
- Error codes/messages need standardization across documentation and code.

---

### 7. Action Items
- Standardize error codes/messages for consistency.
- Document multi-request handling clearly in the API reference.
- Ensure the configuration flag for consideration checks is properly documented.
- Add test cases for the ₹3,000 threshold condition.


---

## Stamp Duty Validation & Auto-Calculation

### 1. Overview
This feature enforces state-level stamp duty validations and provides auto-calculation mechanisms based on article codes, document categories, and consideration amounts. It ensures compliance with legal rules, prevents duplicate requests, and supports client-specific configurations.

---

### 2. Supported States
Stamp duty validation and auto-calculation are currently implemented for five states:
- Delhi
- Rajasthan
- Gujarat
- Tamil Nadu
- Karnataka

---

### 3. Validation Rules
#### 3.1 Article-Based Validation
- Each article code + article name pair has defined stamp duty ranges.
- Example: Article Code 14 (“Born”) → Stamp amount range: ₹0 – ₹5,00,000.
- Some article codes enforce only a minimum value, with no maximum cap.
#### 3.2 Loan-Based Validation
- For certain article codes, stamp duty is calculated as a percentage of the loan amount.
- Percentage is configured based on government rules, but stored in the system for enforcement.
#### 3.3 Reference ID Validation
- Each request must include a unique reference ID per organization.
- Duplicate reference IDs trigger error: “Reference ID is not unique.”
- Responses are logged and returned via API.

---

### 4. Auto-Calculation Logic
#### 4.1 Enabled States
- Karnataka: Auto-calculation applies to all article codes.
- Gujarat & Rajasthan: Auto-calculation applies only to specific configured article codes.
#### 4.2 Calculation Modes
- Shield Auto-Calculation
- Uses external API (Shield).
- Exclusive with Sign Auto-Calculation (cannot enable both).
- Failure → throw Unknown Exception.
- Success → return calculated stamp amount in API response.
- Client must resubmit with the corrected stamp amount if a mismatch occurs.
- Sign Auto-Calculation
- Uses internal Microservice 2.0 API.
- Parameters: state, document category, and consideration amount.
- Returns either success (with calculated stamp amount) or failure.
- Responses are logged in API logs.
#### 4.3 Error Handling
- DS354: If rules are missing for a document category, the system proceeds with the client-provided stamp amount.
- If the response returns NA or mismatched values, the system proceeds with the client-provided stamp amount.
- If API fails, throw error: “Unable to fetch calculated stamp duty amount.”

---

### 5. Client-Specific Configurations
#### 5.1 KVB Client
- Request format differs: data nested inside stampPaperData.
- Keys handled: firstPartyAddress, date, etc.
- System detects client type and applies appropriate parsing logic.

---

### 6. First Party Information Handling
#### 6.1 Autofill Configuration
- If enabled, the system fetches organization data (address, state, pin code, country, etc.) from onboarding records.
- If disabled: client must provide all first-party details explicitly.
#### 6.2 Validation Rules

| Field              | Mandatory | Rule / Constraint                          | Error Message                                |
|--------------------|-----------|--------------------------------------------|----------------------------------------------|
| State              | Yes       | Must be a valid state code (no union territories) | Invalid state code                           |
| First Party Name   | Yes       | Length 2-60 (KVB-specific); alphanumeric, spaces allowed | Invalid name                                |
| First Party Address| Yes       | Object required                            | Required first party object is missing        |
| Country            | Optional  | If present, must equal India               | Invalid country                              |
| Locality           | Optional  | Max length 100                             | Invalid locality                             |
| Pin Code           | Optional  | Numeric, length = 6                        | Invalid pin code                             |
| Street Address     | Yes       | Length 2-200                               | Invalid street address                       |
| City               | Yes       | Length 2-30                                | Invalid city                                 |
| Autofill Config    | Conditional | If enabled, system fetches org data; if disabled, client must provide | Missing autofill configuration              |

---

### 7. Second Party Information Handling
#### 7.1 Non-Mandatory States
- Organization-level configuration allows second-party info to be optional for specific states.
- Example: Karnataka configured → second party details not required.
#### 7.2 Special Case – “NA” Value
- If the second party name = “NA”, the system skips validation of the second party details.
- Client-specific feature (applies to one client only).
#### 7.3 Validation Rules (when details are provided)

| Field              | Mandatory | Rule / Constraint                          | Error Message                                |
|--------------------|-----------|--------------------------------------------|----------------------------------------------|
| Second Party Name  | Yes       | Length 2-60, alphanumeric only             | Invalid name                                 |
| State & Country    | Conditional | Validated only if stamp type ≠ traditional and paid by second party | Invalid state/country |
| Locality           | Optional  | Max length 100                             | Invalid locality                             |
| Pin Code           | Optional  | Numeric, length = 6                        | Invalid pin code                             |
| Street Address     | Optional  | Length 2-200                               | Invalid street address                       |
| City               | Optional  | Length 2-30                                | Invalid city                                 |
| Stamp Duty Paid By | Yes       | Must be either First Party or Second Party | Invalid payer                                |
| Special Case – “NA”| Conditional | If name = NA, skip validation             | Validation skipped                           |

---

### 8. Additional Features
#### 8.1 Search Charge Calculation
- Currently enabled only for Rajasthan.
- Configurable at core level → can be extended to other states.
- If enabled, calculations proceed accordingly for configured states.
  
---

### 9. Decisions Captured
- DS354 error code allows fallback to client-provided stamp amount.
- KVB client requires special request format handling.
- Autofill configuration determines whether first-party details are auto-populated or client-supplied.
- Second-party info can be optional depending on organization configuration.
- “NA” value for second party name bypasses validation.
- Search charge calculation is configurable but currently limited to Rajasthan.

---

### 10. Action Items
- Document DS354 error handling in the API reference.
- Maintain dual request format support (standard vs. KVB).
- Ensure autofill logic integrates with organization onboarding data.
- Validate first and second party details consistently across autofill/manual entry modes.
- Confirm search charge calculation extension for other states.


