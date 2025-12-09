
![alt text](Img\melento.png "optional title")

# Aadhaar Validation Mismatch Webhook API



\#95, Rudra Chambers, 3rd Floor, 4th Main Road,  
11th Cross, Malleshwaram, Bangalore \- 560003  
Phone: 080-46682650   [www.signdesk.com](http://www.signdesk.com)

| Document Number | Last Updated  | Version ID | Information Classification |
| :---: | :---: | :---: | :---: |
| AVMC08012024 | 08-01-2024 | 1.0 | Confidential |

	

| Prepared By | Title |
| :---: | :---: |
| [Abhijith Koushik B K](mailto:abhijith.bk@signdesk.com) | Technical Writer |

Disclaimer

This document is for the sole use of the intended recipient(s) and contains confidential and privileged information. Any unauthorized review, use, disclosure, copying or distribution is strictly prohibited.

# Revision History

| Revision Number | Version ID | Revision Date | Page No | Revision Description | Author | Approved By |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | V1 |  |  | Document Created | Abhijith Koushik B K |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

Table of Contents

[**Revision History	2**](#revision-history)

[**Introduction	4**](#introduction)

[About Desk Nine Pvt Ltd	4](#about-desk-nine-pvt-ltd)

[SignDesk.com	4](#signdesk.com)

[**Aadhaar Validation Mismatch Webhook \- Success Case	5**](#aadhaar-validation-mismatch-webhook---success-case)

[Request Parameters	7](#request-parameters)

[Response Parameters	7](#response-parameters)

## 

## 

# Introduction

## About Desk Nine Pvt Ltd 

Desk Nine Pvt. Ltd. is an ISO 27001:2013 and 9001:2015 certified technology company that was started to provide seamless & AI-powered digital documentation solutions. In order to comprehensively solve the problems and challenges caused due to the traditional documentation process,  Desk Nine Pvt. Ltd has created an entity to automate & digitize paper-based documentation & manual workflows  \- SignDesk.com. SignDesk offers contract workflow automation, electronic evidence creation, digital KYC verification & onboarding, and automated recurring payments. 

## SignDesk.com 

SignDesk.com offers a Contract Workflow Automation Solution, developed exclusively to ease paperwork and documentation, and aimed primarily at the financial sector. Our digital documentation product provides end-to-end automated documentation, required for business processes like Customer Onboarding, Loan Disbursal Documentation, Vendor Onboarding, document execution, and many others. Video-based ID verification & onboarding, Aadhaar-based eSign & video signatures, Digitized Stamping, and Automated Recurring Payments via eNACH are the pillars of our Document Workflow Automation module. 

Our nation-wide Digital Stamping Solutions help people print legal documents on stamp paper by using our online platform from anywhere. Our eNACH service helps banks and other financial organizations automate their recurring payments digitally, thereby avoiding a lot of paperwork and saving time. Our legally compliant electronic signatures & innovative video signatures allow remote & instant document execution with seamless electronic evidence creation. Our AI-powered KYC verification solution automates the KYC verification & onboarding process with VCIP & VBIP-enabled digital workflows. We, at SignDesk, offer services that are in compliance with government policies and are legally valid. Our efforts to digitize inefficient paper-based methods have been recognized and awarded, the most recent being the Global Banking & Finance Review’s Best Digital Onboarding Product of 2020 in India, Inflection’s Best Digital Stamping Solution of 2020, and InnTech’s Best AI/ML Product of 2020\.

# Aadhaar Validation Mismatch Webhook 

HTTP Type - POST 

Request  

```json
{
    "docket_id": "xxxx",
    "document_id": "xxxx",
    "signer_id": "xxxx",
    "esign_type": "digital",
    "trigger": "aadhaar_signature_validation_failure",
    "validation_info": 
     [{
            "status": "failed",
            "field_name": "Name",
            "message": "The name did not match the details as per Aadhaar records.",
            "value_passed": "John",
            "value_as_per_aadhaar": "John Doe",
            "percentage_match": 14.285714285714285
        },
        {
            "status": "failed",
            "field_name": "Gender",
            "message": "The gender did not match the details as per Aadhaar records.",
            "value_passed": "M",
            "value_as_per_aadhaar": "F"
            },
        {
            "status": "failed",
            "field_name": "Year",
            "message": "The year of birth did not match the details as per Aadhaar records.",
            "value_passed": "1990",
            "value_as_per_aadhaar": "1992"
        }]


```

Response 
 

```json
{
    "status": "success/failed",
    "message": "xxxx"
}
```

Content-Type - Application/json

### 

### Request Parameters

| Sl. No | Parameter | Description |
| ----- | :---- | :---- |
| 1 | status | Defines the status of the API. Possible Values: success  failed |
| 2 | docket\_id | Unique ID assigned for every set of uploaded document(s). One docket\_id should be assigned for each set of uploaded document(s). |
| 3 | document\_id | It is a Unique ID assigned to each document. |
| 4 | signer\_id | Unique ID assigned to each signer by SignDesk to invoke the widget. |
| 5 | esign\_type | This refers to the type of **Aadhaar** eSign preferred. Can be passed only if **signature\_type: aadhaar** **Possible values:** otp biometric	 both Default value is otp |
| 6 | trigger | This defines the type of API triggered |
| 7 | validation\_info | This is an array that consists of the validated data. |

### 

### Response Parameters 

| Sl. No | Parameter | Description |
| ----- | :---- | :---- |
| 1 | status | Defines the status of the webhook. Possible Values: success  failed |
| 2 | message | This is a message displayed based on the webhook result. |


[def]: Img\melento.png