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

