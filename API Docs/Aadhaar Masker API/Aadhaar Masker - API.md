

#  **Aadhaar Masker**

### **_API Document_**


Table of Contents

[**Revision History	1**](#revision-history)

[**Introduction	3**](#introduction)

[About Desk Nine Pvt Ltd	3](#about-desk-nine-pvt-ltd)

[SignDesk	3](#signdesk)

[**Aadhaar Masker API	4**](#aadhaar-masker-api)

[Request Parameters	6](#request-parameters)

[Response Parameters	6](#response-parameters)

[**Error Codes and messages	7**](#error-codes-and-messages)




# **Aadhaar Masker API** {#aadhaar-masker-api}

## This is the new one

| Aadhaar Masker API          |  |
| ----- | :---- |
| Feature | Provides status updates.  |
| HTTP Type | POST |
| Header | x-parse-rest-api-key x-parse-application-id |
| Request | **1\. (Raw request)** {  "reference\_id": "xxxxx",  "source":  \[  "Base64 string" \]        "mask\_qr\_code": "xxxxx"          //true or false}  **2\. (Form Data Request)**  "reference\_id": "xxxxx"     "source1" : "image\_document"     "source2" :  "image\_document"  |
| Response | **1\. (When one image is given)** {  "status": "xxxx",  "message": " Data masked successfully",  "reference\_id": "xxxx",  "transaction\_id": "xxxx",  "response\_time\_stamp": "xxxx",  "result":       {  "image": “xxxx”       }  }  **2\. (When two images are given)** {  "status": "xxxx",  "message": " Data masked successfully",  "reference\_id": "xxxx",  "transaction\_id": "xxxx",  "response\_time\_stamp": "xxxx",  "result":            {  “first\_image” : “ xxxx”,  “second\_image” : “xxxx”    }  }  |
| Content-Type | Application/json |

### 

### Request Parameters {#request-parameters}

| Sl.No | Parameter | Field Option | Description |
| ----- | :---- | :---- | :---- |
| 1 | reference\_id | Mandatory | This is a unique ID sent in response to an API request. |
| 2 | source | Mandatory | It is used when the raw data request is used and the base64 string is passed in it. |
| 3 | mask\_qr\_code | Optional | This is the Boolean value that indicates whether the QR code on the Aadhaar card should be masked in the response. |
| 4 | source1 | Mandatory | This field is utilized when making a form data request. |
| 5 | source2 | Optional | This field is utilized when making a form data request. |

### 

### Response Parameters {#response-parameters}

| Sl. No | Parameter | Description |
| ----- | :---- | :---- |
| 1 | status | It represents whether the API is working or not, i.e., the success or failed scenario of the API.  |
| 2 | message | This is the main content or text that is being sent or received. |
| 3 | reference\_id | This is a unique ID sent in response to an API request. |
| 4 | transaction\_id | This defines the transaction ID passed as part of the request. |
| 5 | response\_time\_stamp | This represents the response time of the stamp. |
| 6 | result | This represents the result of the API. |
| 7 | image | It represents the image output field. |
| 8 | first\_image | This is the first image output field when two images are passed. |
| 9 | second\_image | This is the second image output field when two images are passed. |

# Error Codes and messages {#error-codes-and-messages}

| Error Code | Error Message |
| :---: | ----- |
| **dv-005** | Unknown error |
| **dv-006** | The required source was not found in the request |
| **dv-007** | The document verification services are not configured for this organization |
| **dv-008** | The document verification APIs are not configured for this organization |
| **dv-009** | The reference\_id used in the request should be unique |
| **dv-010** | The required x-parse-application-id and x-parse-rest-api-key not found |
| **dv-011** | The required x-parse-application-id was not found |
| **dv-012** | The required x-parse-rest-api-key was not found |
| **dv-013** | The passed x-parse-application-id and x-parse-rest-api-key do not match |
| **dv-014** | The reference\_id passed in the request is invalid |
| **dv-015** | The required reference\_id was not found in the request |
| **dv-034** | The documents could not be processed |
| **dv-060** | The API hit limit is exhausted for the client. Please replenish the hit limit. |
| **dv-070** | The encryption certificate does not exist |
| **dv-002** | The base64 content passed in the request is invalid |

[image1]: <data:image/png;base64,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>
