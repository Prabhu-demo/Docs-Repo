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
