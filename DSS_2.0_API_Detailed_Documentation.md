# DSS 2.0 API Documentation

## 1. Parameter: reference_id
#### Validations
* **Presence**: Must be present in the request.
  * Error: "The required reference_id was not found in the request." (ds-101)
* **Format**: Must match regex: /^[a-zA-Z0-9_\-']+$/
  * Error: "The reference_id passed in the request is invalid." (ds-102)
* **Length**: Maximum 64 characters
  * Error: "The reference_id passed in the request is invalid." (ds-102)
* **Uniqueness**: Should be unique for each transaction/request
  * Error: "The specified ReferenceID is not unique." (ds-428)
* **Combined Validation**: If both transaction_id and reference_id are invalid:
  * Error: "The transaction_id and reference_id passed in the request are invalid." (ds-142)
  * Error: "The transaction_id or reference_id passed in the request is invalid." (ds-425)
#### Field Options
* **Data type**: String
* **Enumerated values**: None (must match regex above)
* **Uniqueness**: Required to be unique per request/transaction
#### Additional Notes
* Used as a primary identifier for requests, logs, and callback tracking.
* Appears in error responses and logs for traceability.
* May be referenced in callback logs and for updating records.
* Used in search queries and validation across multiple services.
* Dependencies: Sometimes validated alongside transaction_id.
#### Mandatory or Optional
* Mandatory for most API endpoints that require tracking or referencing a transaction/request.
#### Configurations (if applicable)
* Default value: None; must be provided by the client.
* Environment overrides: None specified.
* Special rules: Must be unique and conform to the regex and length constraints.

---

