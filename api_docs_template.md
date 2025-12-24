<link rel="stylesheet" href="style.css">
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<p align="center">
  <img src="Img/img4.jpg" alt="Blue table" style="width:50%; height:auto;" />

</p>

<h1 align = "center"> Request API </h1>

<h2 align = "center"> API Documentation </h2>


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


<p align="right">

<img src="Img\footer_with_cred.jpg">
</p>




# **Introduction**

## **Melento**

<p align = "justify">Melento is a collaborative intelligence platform that transforms siloed data and systems into autonomous workflows that streamline processes and accelerate decision-making.</p>

<p align = "justify">It provides an intuitive drag-and-drop builder so teams can quickly design and automate complex workflows across various departments and support with no need for traditional coding skills while orchestrating rules, approvals, and system integrations end-to-end.</p>

<p align = "justify">Teams collaborate in a unified workspace with shared tasks, documents, comments, and audit trails, providing full visibility into progress and accountability.</p>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


# **Table of Contents**
1. [Revision History](#revision-history)  
2. [Table of Contents](#table-of-contents)  
3. [Introduction](#introduction)  
   - [About Desk Nine Pvt. Ltd.](#about-desk-nine-pvt-ltd)  
   - [Melento](#melento)  
4. [Name](#name)  
5. [API Name](#api-name)  
6. [Request Parameters](#request-parameters)  
7. [Response Parameters](#response-parameters)  
8. [Error Codes and Messages](#error-codes-and-messages)  



<br>

# **API Name**

- **HTTP Type**: `POST`  
- **Header**:  
  - `Authorization: Bearer abc123xyz`  
  - `Content-Type: application/json`  
- **Request**:

```json
{
  "reference_id": "REF-987654",
  "source": "YmFzZTY0U3RyaW5n",
  "mask_qr_code": true,
  "source1": "form-data-field",
  "source2": "optional-field"
}
```

- **Response**: `200 OK`
- **Content-Type**: `application/json`








<br>

## **Request Parameters**

| Sl.No | Parameter | Field Option | Description |
| ----- | :---- | :---- | :---- |
| 1 | reference\_id | Mandatory | This is a unique ID sent in response to an API request. |
| 2 | source | Mandatory | It is used when the raw data request is used and the base64 string is passed in it. |
| 3 | mask\_qr\_code | Optional | This is the Boolean value that indicates whether the QR code on the Aadhaar card should be masked in the response. |
| 4 | source1 | Mandatory | This field is utilized when making a form data request. |
| 5 | source2 | Optional | This field is utilized when making a form data request. |


<br>

## **Response Parameters**

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


<br>

## **Error Codes and Messages**

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