

![][image1]

# 

# 

#  **Aadhaar Extraction** 

  API Document  
 

## Prepared By:

[Veena G](mailto:veena.g@signdesk.com)  
May 6, 2024

## Approved By:

[Abhijith Koushik B K](mailto:abhijith.bk@signdesk.com)  
May 6, 2024

# **Revision History** {#revision-history}

| Revision No | Revision Date | Page No | Description | Author | Approver |
| :---: | :---: | :---: | :---: | :---: | :---: |
| \- |  |  | Document created | [Veena G](mailto:veena.g@signdesk.com) | [Abhijith Koushik B K](mailto:abhijith.bk@signdesk.com) |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

# Table of Contents {#table-of-contents}

[**Revision History	2**](#revision-history)

[**Table of Contents	3**](#table-of-contents)

[**Introduction	4**](#introduction)

[About Desk Nine Pvt Ltd	4](#about-desk-nine-pvt-ltd)

[SignDesk	4](#signdesk)

[**Aadhaar Extraction API	5**](#aadhaar-extraction-api)

[Request Parameters	7](#request-parameters)

[Response Parameters	7](#response-parameters)

[**Error Codes and Messages	10**](#error-codes-and-messages)

# **Introduction** {#introduction}

| About Desk Nine Pvt Ltd Desk Nine Pvt. Ltd. is an ISO 27001:2013 and 9001:2015 certified technology company providing seamless & AI-powered digital documentation solutions. To comprehensively solve the challenges caused due to the traditional documentation process, SignDesk was created under the aegis of Desk Nine Pvt. Ltd, to automate document workflows & boost productivity. SignDesk offers solutions for contract automation, electronic evidence creation, digital ID verification & onboarding, and automated recurring payments.  SignDesk SignDesk is a global provider of document automation solutions developed to maximize productivity, improve workflow efficiency, and help businesses achieve digital transformation goals. Our product suite offers AI-powered solutions for digital onboarding, ID verification, digital evidence creation, contract management, and recurring payment automation, customizable for businesses & verticals across industry sectors.   SignDesk’s intelligent documentation module consists of five product pillars: KYC/KYB Verification for businesses to maintain AML/CDD compliance & create seamless video-based onboarding journeys with low code APIs, Digital Stamping enabling businesses to pay stamp duty in real-time & streamline stamp procurement across the nation, E-Signature Workflow solution to create, track & eSign documents online at scale with a robust audit trail, Contract Lifecycle Management to digitize contract stages from draft to renewal and enable holistic contract governance; and eNACH eMandate solutions to automate recurring payments using Aadhaar, APIs or QR-codes.  |
| :---- |

# **Aadhaar Extraction API**  {#aadhaar-extraction-api}

| Aadhaar Extraction API  |  |
| ----- | :---- |
| Feature | This API verifies the document passed in the request. |
| HTTP Type | POST |
| Header | x-parse-application-id/x-parse-rest-api-id x-parse-rest-api-key |
| Request | {     "reference\_id": "xxxxx",     "doc\_type": "aadhaar\_card",     "source": "base64 of document",     "verification": "true" } |
| Response | **Success Response:** {     "status": "success",     "message": "xxxxx",     "reference\_id": "xxxxx",     "transaction\_id": "xxxxx",     "document\_type": "aadhaar\_card",     "extracted\_data":      {         "document\_number": "xxxxx",         "surname\_and\_given\_names": "xxxxx",         "sex": "xxxxx",         "date\_of\_birth": "xxxxx",         "address": "xxxxx",         "last\_four\_digits\_of\_aadhaar": "xxxxx",         "name\_as\_per\_aadhaar": "xxxxx"     },    "verified": true,    "result":      {         "validated\_data":           {             "verified": "xxxxx",             "ageBand": "xxxxx",             "state": "xxxxx",             "mobileNumber": "xxxxx",             "gender": "xxxxx"          }     } } **Failed Response:** {     "status": "failed",     "reference\_id": "xxxxx",     "error": "xxxxx",     "error\_code": "xxxxx”,     "response\_time\_stamp": "xxxxx" }  |
| Content-Type | Application/json |

### **Request Parameters** {#request-parameters}

| Sl.No | Parameter | Field Option | Description |
| ----- | ----- | :---: | ----- |
| 1 | reference\_id | Mandatory | This is a unique ID assigned to track the API call. |
| 2 | doc\_type | Mandatory | This refers to the document that is passed in the request. **Possible value:** aadhaar\_card |
| 3 | source | Mandatory | This refers to the base64 encoded file content. |
| 4 | verification | Conditional mandatory | This is a flag. If this flag is set to true, the client will receive validated data in response. |

### **Response Parameters** {#response-parameters}

| Sl. No | Parameter | Description |
| :---: | ----- | ----- |
| 1 | status | This refers to the status of the API call. |
| 2 | message | This refers to the message based on the status of the API. |
| 3 | reference\_id | This is a unique ID assigned to track the API call. |
| 4 | transaction\_id | This refers to the unique ID assigned to each transaction. |
| 5 | document\_type | This refers to the document that is passed in the request. |
| 6 | extracted\_data | This refers to the extracted data from the document passed in the request. |
| 7 | document\_number | This refers to the unique number assigned to each document. |
| 8 | surname\_and\_given\_names | This refers to the full name present in the passed document. |
| 9 | sex | This refers to the gender present in the passed document. |
| 10 | date\_of\_birth | This refers to the date of birth present in the passed document. |
| 11 | address | This refers to the address present in the passed document. |
| 12 | last\_four\_digits\_of\_aadhaar | This refers to the last four digits of aadhaar number present in the passed document. |
| 13 | name\_as\_per\_aadhaar | This refers to the name as per the Aadhaar card that is present in the passed document. |
| 14 | verified | This refers to the flag that indicates whether the extracted data has been verified or not. |
| 15 | result | This defines the result of the extracted data according to the document passed in the request. |
| 16 | validated\_data | This refers to the data which is verified according to the passed document. |
| 17 | ageBand | This refers to the range of age according to the age present in the passed document. |
| 18 | state | This refers to the state that is present in the passed document. |
| 19 | mobileNumber | This refers to the mobile number that is validated according to the passed document. |
| 20 | gender | This refers to the gender present in the passed document. |
| 21 | error | This displays a message stating the reason for the error if occurred. |
| 22 | error\_code | This refers to the error code corresponding to the error that occurred. |
| 23 | response\_time\_stamp | Response API timestamp. This is in the format “YYYY-MM-DDThh:mm:ss” (derived from ISO 8601). The Time zone should not be specified and is automatically defaulted to IST (UTC \+5.30).  |

# **Error Codes and Messages** {#error-codes-and-messages}

| Error Code | Error Message |
| :---: | ----- |
| **dv-001** | Unable to extract the document content |
| **dv-002** | The base 64 content passed in the request is invalid. |
| **dv-003** | Unable to process |
| **dv-004** | Unable to extract the document content, please try again |
| **dv-005** | Unknown error |
| **dv-006** | The source was not found in the request |
| **dv-007** | The document verification services are not configured for this organization |
| **dv-008** | The document verification APIs are not configured for this organization |
| **dv-009** | The reference\_id used in the request should be unique |
| **dv-010** | The required x-parse-application-id and x-parse-rest-api-key not found |
| **dv-011** | The required x-parse-application-id was not found |
| **dv-012** | The required x-parse-rest-api-key was not found |
| **dv-013** | The passed x-parse-application-id and x-parse-rest-api-key do not match |
| **dv-014** | The reference\_id passed in the request is invalid |
| **dv-015** | The required reference\_id was not found in the request |
| **dv-016** | The reference\_id was not found in the request |
| **dv-017** | The app\_user\_id used in the request should be unique. |
| **dv-060** | The API hit limit is exhausted for the client. Please replenish the hit limit. |
| **dv-251** | Please upload the back side of the image. |
| **dv-252** | Please upload the front side of the image. |

[image1]: <data:image/png;base64,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>