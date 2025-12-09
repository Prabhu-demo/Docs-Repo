<link rel="stylesheet" href="style.css">

![alt text](image.png)

# API Documentation

**Prepared By:**  
Tanu Nanda Prabhu  

---



## Table of Contents
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

---

## Introduction

<!-- Blue Section Start -->

<link rel="stylesheet" href="styles.css">

<div class = "blue-box">
<h1>About Desk Nine Pvt. Ltd.</h1>
<p>
Desk Nine Pvt. Ltd. is an ISO 27001:2013 and 9001:2015 certified technology company providing seamless & AI-powered digital documentation solutions. To comprehensively address the challenges posed by the traditional documentation process, <strong>Melento (formerly SignDesk)</strong> was established under the guidance of Desk Nine Pvt. Ltd, to automate document workflows & boost productivity. Melento offers solutions for contract automation, electronic evidence creation, digital ID verification & onboarding, and automated recurring payments.
</p>

<hr>

<h2>Melento</h2>
<p>
Melento (formerly SignDesk), a product of Desk Nine Pvt. Ltd., is a global RegTech offering document automation and workflow management to help businesses digitize, streamline, and scale their operations. With over a decade of experience and multiple international awards, including <em>Best RegTech of the Year</em> at the BW FinTech Festival 2025, Melento powers digital transformation for 3000+ clients, including 60+ major banks, through AI-driven, compliance-ready workflow solutions.
</p>

<hr>

<h3>Our Solutions</h3>
<ul>
  <li><strong>Digital Onboarding</strong> using low-code APIs for digital and video-based onboarding</li>
  <li><strong>Digital Stamping (India-only)</strong> for real-time payment of stamp duty and centralized procurement</li>
  <li><strong>E-signatures</strong> to create, track, and execute online documents</li>
  <li><strong>Contract Lifecycle Management (CLM)</strong> digitizing the end-to-end contract process</li>
  <li><strong>eNACH/eMandate Automation</strong> for recurring payment management</li>
  <li><strong>Collaborative Intelligence Platform</strong> with AI-powered workflows, real-time multi-party collaboration, and role-based approvals</li>
</ul>

<hr>

<h3>Headquarters</h3>
<p>
Headquartered in <strong>Bangalore</strong> with offices across six Indian cities, a global presence, and a team of 300+ technology professionals, Melento delivers trusted, paper-free solutions for documentation, end-to-end operational workflow, and contract lifecycle management, while enhancing compliance and accelerating business outcomes.
</p>
</div>

---


## API Name

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









## Request Parameters

| Sl.No | Parameter | Field Option | Description |
| ----- | :---- | :---- | :---- |
| 1 | reference\_id | Mandatory | This is a unique ID sent in response to an API request. |
| 2 | source | Mandatory | It is used when the raw data request is used and the base64 string is passed in it. |
| 3 | mask\_qr\_code | Optional | This is the Boolean value that indicates whether the QR code on the Aadhaar card should be masked in the response. |
| 4 | source1 | Mandatory | This field is utilized when making a form data request. |
| 5 | source2 | Optional | This field is utilized when making a form data request. |

---

## Response Parameters

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

---

## Error Codes and Messages

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