# Feature Documentation
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
- Karnataka: Auto-calculation applies to all article codes
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


----


# State-wise Stamp Duty Validation & Auto Calculation Framework

## 1. Feature Overview
This feature implements **state-wise, article-wise stamp duty validations and auto-calculation logic** during the stamping request processing flow.  
It ensures legal compliance by validating stamp duty amounts, enforcing state-specific rules, handling auto-calculated stamp duties, and validating party details based on configurable organization-level settings.

---

## 2. Objectives
- Prevent incorrect or legally invalid stamp duty amounts  
- Enforce state-specific stamp duty constraints  
- Avoid duplicate requests using reference ID validation  
- Support configurable auto-calculation mechanisms  
- Provide flexibility for client-specific integrations  

---

## 3. Supported States
- Karnataka  
- Gujarat  
- Rajasthan  
- Delhi  
- Tamil Nadu  

---

## 4. State & Article-wise Stamp Duty Validation
Stamp duty is validated based on:
- State  
- Article Code  
- Article Name  

### Validation Types
- Minimum stamp amount  
- Maximum stamp amount  
- Range-based validation  

Example:
- Article Code: 14  
- Article Name: Bond  
- Allowed Range: ₹0 – ₹5,00,000  

---

## 5. Percentage-based Stamp Duty Validation
For selected article codes:
- Stamp duty is validated as a percentage of the loan/consideration amount  
- Percentage values are configuration-driven  

---

## 6. Reference ID Validation
- Reference ID must be unique per organization  
- Duplicate reference IDs result in an error response  
- All responses are logged  

---

## 7. Stamp Duty Auto Calculation

### 7.1 Auto Calculation Modes
Only one can be enabled at a time:
- SHC (External) Calculator  
- SignDesk Internal Calculator  

If both are enabled, SignDesk calculation takes precedence.

---

### 7.2 SHC Auto Calculation
Applicable States:
- Karnataka (all article codes)  
- Gujarat & Rajasthan (selected article codes)  

Behavior:
- Calls SHC API  
- Returns calculated stamp amount  
- Client must retry if mismatch  

---

### 7.3 SignDesk Auto Calculation
- Uses internal microservice (DSS 2.0)  
- If rules are missing (DS354), request proceeds with client stamp amount  

---

## 8. Client-Specific Handling (KVB)
- Different request structure  
- Nested stampPaperData object  
- Keys mapped internally  

---

## 9. Party Information Validation

### 9.1 First Party
Autofill Configuration:
- Enabled → fetched from organization data  
- Disabled → client must pass all mandatory fields  

Validations include name, state, address, city, pincode, and country.

---

### 9.2 Second Party
- Mandatory only if stamp duty is paid by second party  
- Can be ignored for configured states  
- If provided, full validation applies  

Client-specific override allows second party name as "NA".

---

## 10. Stamp Type Rules
- Non-traditional stamp types enforce state & country validation  
- Second party validation applies only when stamp is paid by second party  

---

## 11. Search Charge Calculation
- Currently enabled only for Rajasthan  
- Configuration-driven for future expansion  

---

## 12. Error Handling
- Duplicate reference ID → Error  
- Validation failure → Error  
- Auto calculation failure → Exception or fallback  

---

## 13. Logging & Auditing
- All responses logged  
- Calculated stamp amounts returned in API responses  

---

# KVB-Specific Validations, Search Charge & Payment Mode Logic

## 1. Overview
This document captures **KVB-specific validations**, **search charge calculation logic**, and **payment mode & dynamic party swapping behavior** derived from the technical walkthrough.  
These rules are layered on top of the standard stamping workflow and apply only when corresponding organization-level configurations are enabled.

---

## 2. Document Category Validation (KVB Only)
- Allowed values: **1 to 13**
- Accepted formats:
  - Single digit: `1–9`
  - Double digit: `10, 11, 12, 13`
- Any value outside this range results in validation failure.
- This restriction is enforced **only for KVB requests**.

---

## 3. Search Charge Calculation

### 3.1 Applicability
- Search charge is **state-configurable**
- Currently **enabled only for Rajasthan**
- Mandatory when enabled for a state

---

### 3.2 Configuration Structure
- Search charge is defined as an **array of percentages**
- Example: `[10, 10, 10]` → Total 30%

---

### 3.3 Calculation Logic
Search charge is **not calculated as a single aggregated percentage**.

Instead:
1. Each percentage is calculated **individually**
2. Each value is **rounded independently**
3. All rounded values are **summed**

#### Example
Stamp Amount: `115`  
Percentages: `[10, 10, 10]`

- 10% of 115 = 11.5 → rounded to 12
- Total Search Charge = `12 + 12 + 12 = 36`

This avoids rounding discrepancies that occur with direct percentage aggregation.

---

### 3.4 Validation
- If calculated search charge does not match request value:
  - Error: **Search charge used in the request is invalid**
- Same logic applies to:
  - Single request
  - Multi-request (array-based stamping)

---

### 3.5 Mandatory Field Validation
- If search charge is enabled for the state and not passed:
  - Error: **Search charge is a mandatory field**

---

## 4. Multi-Request Handling
For multi-stamp requests:
- Search charge must be an array
- Each element must correspond to its stamp amount
- Any mismatch causes validation failure

---

## 5. Client-Specific Infrastructure (L&T)
- Dedicated API server
- Request structure largely same as standard clients
- Minor parameter-level variations
- Same validation logic reused

---

## 6. Document Reference Number Validation
- Alphanumeric only
- Maximum length: **20**
- Applies to UID-based request bodies

---

## 7. Dynamic Party Swapping Feature

### 7.1 Feature Description
- Swaps **First Party** and **Second Party**
- Configuration-driven
- Behavior differs between **Portal** and **API**

---

### 7.2 Key Parameters
- `stampDutyPaidBy` → First Party / Second Party
- `stampDutyPaymentMethod` → `VALID` / `ONLINE`

---

### 7.3 Swapping Logic
Swapping is determined **only when payment method is ONLINE**.

| Paid By | Method  | Result |
|-------|--------|--------|
| First Party | VALID | No swap, wallet deduction |
| First Party | ONLINE | Swap parties, send payment link |
| Second Party | ONLINE | Swap, payment link |
| Second Party | VALID | Wallet deduction |

---

## 8. Payment Mode Configuration

### 8.1 Supported Payment Modes
- **Prepaid** → Wallet only
- **JIT (Just-In-Time)** → Online payment only
- **Hybrid** → Both wallet & online allowed

---

### 8.2 Prepaid Rules
- Stamp duty must be paid by **First Party**
- Payment method must be **VALID**
- ONLINE payment method is invalid
- `stampDutyPaymentMethod` is not mandatory

---

### 8.3 JIT Rules
- Stamp duty must be paid by **Second Party**
- Payment method must be **ONLINE**
- VALID payment method is invalid

---

### 8.4 Hybrid Rules
- Both First Party and Second Party allowed
- Both VALID and ONLINE allowed
- No strict violations

---

## 9. Invalid Combination Handling
If:
- Payment mode is not enabled
- Swapping is not enabled
- But `stampDutyPaymentMethod` is passed

→ Error: **This feature is not enabled for the organization**

---

## 10. Case Sensitivity
- `VALID` / `ONLINE`
- Case-insensitive
- Any other value is invalid

---

## 11. Known Observations
- Some validations appear reversed in legacy logic
- Feature is live and backward-compatible
- Additional testing recommended for edge cases

---

## 12. Logging
- All validation failures logged
- Same error returned in API response

---

## 13. Summary
This feature ensures:
- Legal correctness of search charges
- Precise rounding compliance
- Controlled payment flows
- Safe handling of client-specific deviations

----


# Dynamic Party Swapping & Payment Mode Validation – Detailed Overview

## 1. Context
This document captures clarifications and refinements discussed around the **Dynamic Party Swapping feature**, **payment mode enablement**, and **related validations**.  
It focuses on distinguishing **swap flow vs payment-mode-enabled flow**, resolving earlier confusion, and documenting how party data is validated and stored.

---

## 2. Swap Flow vs Payment Mode Enabled

### 2.1 Swap Flow (Allow Dynamic Parties)
- Controlled by configuration key: **allowDynamicParties**
- Independent of *payment mode enabled*
- Validations for swap flow are considered **correct and complete**
- If swapping is enabled and:
  - `stampDutyPaymentMethod` is **not passed**
  → **Error is thrown**

> Earlier confusion arose because swap flow was mistaken for payment-mode-enabled flow.

---

### 2.2 Payment Mode Enabled (Client-specific Enhancement)
- Possibly enabled for **only one client**
- When enabled:
  - `stampDutyPaidBy` decides valid combinations
  - Only two payment methods allowed:
    - `VALID`
    - `ONLINE`
  - Payment method:
    - Must be present
    - Must match allowed value
    - Cannot be empty

---

## 3. Core Keys Driving the Flow

| Key | Purpose |
|---|---|
| stampDutyPaidBy | Identifies First Party or Second Party |
| stampDutyPaymentMethod | Determines VALID vs ONLINE |
| allowDynamicParties | Enables swap behavior |

These keys together determine:
- Normal flow vs swap flow
- Wallet deduction vs payment link
- Which party is treated as payer vs printed party

---

## 4. Swap Flow Scenarios (ONLINE Logic)

- **ONLINE payment implies party swapping**
- Whether payment link is sent depends on who is paying

| Paid By | Method | Outcome |
|------|------|-------|
| First Party | VALID | Normal flow, wallet deduction |
| First Party | ONLINE | Swap parties, payment link |
| Second Party | ONLINE | Swap parties, payment link |
| Second Party | VALID | Wallet deduction |

> ONLINE does not strictly mean second-party payment.  
> It primarily indicates **swap behavior**.

---

## 5. Business Rationale for Swapping
- Organization pays stamp duty
- Client wants **customer name printed as First Party** on challan
- Swap is mainly:
  - **Naming change**
  - **Address reassignment**
- No swap occurs in normal VALID payment scenarios

---

## 6. Payment Mode Rules

### 6.1 JIT (Just-In-Time)
- Only **Second Party payment** allowed
- If `stampDutyPaidBy = First Party`:
  - `stampDutyPaymentMethod` must be **ONLINE**
- Any mismatch → Validation error

---

### 6.2 Prepaid
- Only **VALID (wallet)** allowed
- If `stampDutyPaidBy = First Party`:
  - Must be VALID
- ONLINE → Error

---

## 7. Error Scenarios
If:
- Payment mode is not enabled
- Swap is not enabled
- But `stampDutyPaymentMethod` is sent

→ Error: **Feature not enabled for organization**

---

## 8. Storing Payer Details

### 8.1 API Input vs DB Storage
API may receive:
- duty payer phone number
- duty payer email
- duty payer image

While storing:
- Values are mapped to **First Party** or **Second Party**
- Mapping depends on:
  - Paid by
  - ONLINE vs VALID
  - Swap logic

---

### 8.2 Assignment Logic
- Paid by First Party → store under First Party
- Paid by Second Party → store under Second Party

---

## 9. Autofill Party Info Configuration

- Configuration exists for **autofill party info**
- Applicable to **portal and API**
- If enabled:
  - Missing party details fetched from organization data
- If disabled:
  - Client must pass all mandatory fields
- Validation applies only to:
  - Fields not auto-filled

---

## 10. Party Address & Identity Validation

### 10.1 Second Party Mandatory Conditions
- Second party details validated only when required by flow
- Mandatory fields:
  - Name
  - State
- Address validated only if second party details are required

---

### 10.2 Name Validation Rules
- Max length: **50**
- Alpha-numeric
- Allowed special characters:
  - Space
  - Dot (.)
  - Forward slash (/)
  - Backward slash (\)

---

### 10.3 NA Override
- If Second Party Name = `"NA"`:
  - Skip all second party validations
  - Address validation also skipped

---

### 10.4 State Validation
- Party address must contain **only one state**
- State validated against:
  - Configured stamping states for the organization
- Country:
  - Optional
  - If passed, must be `India`

---

## 11. Scope of Documentation
- Focused on **differences and special cases**
- Common validations are assumed documented elsewhere
- Parameter-level validation included only where behavior differs

---

## 12. Key Takeaways
- Swap flow and payment mode are **independent features**
- ONLINE implies swap, not necessarily second-party payment
- Party swapping exists primarily for **printing and naming requirements**
- Validation rules are configuration-driven and client-specific
- Autofill significantly alters validation expectations

---

## 13. Status
- Feature is live
- Backward-compatible
- Legacy validations retained
- Additional testing recommended for edge scenarios
