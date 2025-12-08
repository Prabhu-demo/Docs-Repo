# Resend Invitation API

## Feature

This API is used to resend the signing invitation when the initial invitation was not sent.

## HTTP Method

**POST**

## Headers

| Header Name              | Description            |
| ------------------------ | ---------------------- |
| `x-parse-rest-api-key`   | Required API key       |
| `x-parse-application-id` | Application identifier |


## Request Body

``` json
{
    "document_id": "xxxx",
    "docket_id": "xxxx",
    "stakeholder_id": "xxxx",
    "reference_id": "xxxx"
    "attempt_count": "xxxx"
}
```

## Response

#### With Invitation Link

``` json
{
    "status": "xxxx",
    "error_code": "xxxx",
    "message": "xxxx",
    "reference_id": "xxxx",
    "resendInvitationLink": "xxxx"
}
```

#### Without Invitation Link

``` json
{
    "status": "xxxx",
    "error_code": "xxxx",
    "message": "xxxx",
    "reference_id": "xxxx"
}
```

## Content-Type

JSON in Base64 encoded format.

## Request Parameters

| Parameter Name   | Field Option | Description                                                                         |
| ---------------- | ------------ | ----------------------------------------------------------------------------------- |
| `stakeholder_id` | Mandatory    | Unique ID assigned to every stakeholder.                                            |
| `reference_id`   | Mandatory    | Unique ID assigned to every eSign requester for each API call.                      |
| `docket_id`      | Mandatory    | Unique ID for the set of uploaded document(s). One `docket_id` is assigned per set. |
| `document_id`    | Mandatory    | Unique ID assigned to each uploaded document.                                       |


## Response Parameters

| Parameter Name         | Description                                                                 |
| ---------------------- | --------------------------------------------------------------------------- |
| `status`               | Indicates success or failure of the API.                                    |
| `message`              | Status message of the invitation.                                           |
| `reference_id`         | Unique ID assigned to every eSign requester for each API call.              |
| `resendInvitationLink` | Invitation link sent to signers who did not receive the initial invitation. |
| `error`                | Error message associated with the failure.                                  |
| `error_code`           | Code corresponding to the error.                                            |

