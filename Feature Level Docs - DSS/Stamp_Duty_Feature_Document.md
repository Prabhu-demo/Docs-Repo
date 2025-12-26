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

## 14. Design Principles
- Configuration-driven  
- Extensible  
- Backward compatible  
