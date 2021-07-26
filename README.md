# Coffee Shop - Full Stack Project
This is the Full-stack nanodegree program 3rd project, The project's objective is to practice and demonstrate learning:
* Implementing authentication and authorization in Flask
* Designing against key security principals
* Implementing role-based control design patterns
* Securing a REST API
* Applying software system risk and compliance principles

# What Will I Build?
A full stack drink menu application, see more details [here](./Coffee_Shop/README.md).

# Getting Started
You can follow instructions specified in:
1. [`./Coffee_Shop/backend/`](./Coffee_Shop/backend/README.md)
2. [`./Coffee_Shop/frontend/`](./Coffee_Shop/frontend/README.md)

# Backend
[`./Coffee_Shop/backend/src/api.py`](./Coffee_Shop/backend/src/auth.py)
and
[`./Coffee_Shop/backend/src/auth/auth.py`](./Coffee_Shop/backend/src/auth.py)
files has been modified

## API Endpoints 
The following endpoints are implemented and they perform CRUD methods on the SQLite database:
* `GET /drinks`
* `GET /drinks-detail`
* `POST /drinks`
* `PATCH /drinks/<id>`
* `DELETE /drinks/<id>`



```
GET /drinks
- public
- Fetches: only the drink.short() data representation
- Request Arguments: None
- Returns: status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
- Example:
{
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "blue",
                    "parts": 1
                }
            ],
            "title": "water"
        }
    ],
    "success": true
}
```
```
GET /drinks-detail
- Require the 'get:drinks-detail' permission
- Fetches: drink.long() data representation
- Request Arguments: payload
- Returns: status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
- Example:
{
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "blue",
                    "name": "water",
                    "parts": 1
                }
            ],
            "title": "water"
        }
    ],
    "success": true
}

```
```
POST /drinks
- Require the 'post:drinks' permission
- Creates: a new row in the drinks table
- Request Arguments: payload and body
- Example:
{
    "title": "Water3",
    "recipe": {
        "name": "Water",
        "color": "blue",
        "parts": 1
    }
}
- Returns: status code 200 and json
- Example:
{
    "drinks": [
        {
            "id": 2,
            "recipe": [
                {
                    "color": "blue",
                    "name": "Water",
                    "parts": 1
                }
            ],
            "title": "Water3"
        }
    ],
    "success": true
}
```
```
PATCH /drinks/<id>
- Require the 'patch:drinks' permission
- Updates: the corresponding row for <id>
- Request Arguments: paylod, body and id 
- Example: 
URL: /drinks/1
Body: 
{
    "title": "Water5"
}
- Returns: status code 200 and json {"success": True, "drinks": drink} 
  where drink an array containing only the updated drink
- Example:
{
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "blue",
                    "name": "water",
                    "parts": 1
                }
            ],
            "title": "Water5"
        }
    ],
    "success": true
}
```
```
DELETE /drinks/<id>
- Require the 'delete:drinks' permission
- Deletes: the corresponding row for <id>
- Request Arguments: paylod and id 
- Example: /drinks/2
- Returns: status code 200 and json
- Example:
{
    "delete": 2,
    "success": true
}
```

## Secure a REST API using Auth0
The third-party authentication system [Auth0](https://auth0.com/) is used

All required configuration settings are included in the [`./Coffee_Shop/backend/src/api.py`](./Coffee_Shop/backend/src/auth.py)
```
AUTH0_DOMAIN = 'fsnd-class.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'dev'
```

## The `@requres_auth` Decorator
A custom @requires_auth decorator is completed in [`./Coffee_Shop/backend/src/auth/auth.py`](./Coffee_Shop/backend/src/auth/auth.py)
##### Get the Authorization header from the request.
##### Take an argument to describe the action (i.e., @require_auth(‘create:drink’).
##### Decode and verify the JWT using the Auth0 secret.
Raise an error if:
- The token is expired.
- The claims are invalid.
- The token is invalid.
- The JWT doesn’t contain the proper action (i.e. create: drink).

## RBAC permission claims
#### Two users are registerd:
* Barista
  - can `get:drinks`
  - can `get:drinks-detail`

* Manager
  - can `get:drinks`
  - can `get:drinks-detail`
  - can `post:drinks`
  - can `patch:drinks`
  - can `delete:drinks`


##### Example of Encoded access JWT for Barista:
 ```
 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjkydjQ2dGg2Z1JGUUVjN2swQWZHdCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2xhc3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZmUwYzUxMzU4MmJjMDA2OTQ2MjJkZCIsImF1ZCI6ImRldiIsImlhdCI6MTYyNzI3MDcyNiwiZXhwIjoxNjI3Mjc3OTI2LCJhenAiOiJrQzZYdHFMRklwUXhRcTVzbkdpcWJLVU5FRUVHa2dUQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.bpUuaLorA0pDKI7ny5KNP3T5yrGOitW2LgktQsEyT1-GlissFvlRv0AUkLLfjHcDBt3pZngznCZkpJ3jcus1P2bMoSoXwU-0BO0IVpRbRjmclvfo7wtzWFAynMEBfij5JbYw6ZIu3FDnJ-GSEKbGap3U__523AdLC8ClKk9JjqvPeL1BkrWSZMR2IhCKjiHSAOIzNBZ8_GIiEwq60ErrIHQg0Xxq9dRb3OH4IqjAP7E2AEn3RZowLWEDgd3KicAtGAOxCTssVAnJuKBezqD4SpYOrMMxWCes6BeskSCKV-xBCUTsFfK9l6VMV7oq0A8PkmsrEnHtXMXKPkhHecfPuQ
 ```
##### Example of Decoded access JWT for Barista Payload Data:
```
{
  "iss": "https://fsnd-class.us.auth0.com/",
  "sub": "auth0|60fe0c513582bc00694622dd",
  "aud": "dev",
  "iat": 1627263025,
  "exp": 1627270225,
  "azp": "kC6XtqLFIpQxQq5snGiqbKUNEEEGkgTA",
  "scope": "",
  "permissions": [
    "get:drinks-detail"
  ]
}
 ```
 ##### Example of Encoded access JWT for Manager:
 ```
 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjkydjQ2dGg2Z1JGUUVjN2swQWZHdCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2xhc3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZmUwYmZhMGY4NjY0MDA2OTJhZGJhYyIsImF1ZCI6ImRldiIsImlhdCI6MTYyNzI3MDk4OCwiZXhwIjoxNjI3Mjc4MTg4LCJhenAiOiJrQzZYdHFMRklwUXhRcTVzbkdpcWJLVU5FRUVHa2dUQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.bhWE1QIoeWmrkI6RCG-KjTGIjBOJBOMjBzet-qzf7F1EydhDfE0NUzhEeVFPCUBrRjH4JI1pbFQfWpE8xP-QsvJTbk1_LpkAYSqaR5eOu55mxfUnDYP-rfgbmzu3_uB2FvwflAgXTGhaGwyaHCaVdfPCl7R_bxltRo9WOlfHEE0kvrblKCy32vmqClzwIviV7Uogy5oCOITFgggi72BStqZy9lm2vWrAt-ne_wmFl1oXcwM07ym06tPqOZkdhxWB5nImNwTt5ARHJqdyIxJgvZH9RaM7INaNNlkHdbZ_FfmEYqf3ihoHbHes0d4xLc5t88Ummmb5dJ16Po5iwNz3Zw
 ```
 
 ##### Example of Decoded access JWT for Manager Payload Data:
 ```
 {
  "iss": "https://fsnd-class.us.auth0.com/",
  "sub": "auth0|60fe0bfa0f866400692adbac",
  "aud": "dev",
  "iat": 1627263302,
  "exp": 1627270502,
  "azp": "kC6XtqLFIpQxQq5snGiqbKUNEEEGkgTA",
  "scope": "",
  "permissions": [
    "delete:drinks",
    "get:drinks-detail",
    "patch:drinks",
    "post:drinks"
  ]
}
 ```
# Frontend

The frontend has been configured with Auth0 variables and backend configuration
[`./Coffee_Shop/frontend/src/environment/environment.ts`](./Coffee_Shop/frontend/src/environment/environment.ts) file has been modified

```
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', 
  auth0: {
    url: 'fsnd-class.us', 
    audience: 'dev', 
    clientId: 'kC6XtqLFIpQxQq5snGiqbKUNEEEGkgTA',
    callbackURL: 'http://localhost:8100', 
  }
};
```
# Postman Collection Integeration Test
Import [postman](https://www.postman.com/) collection [`./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`](./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`)
Running collection using [Newman](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/)

<p align = "center">
<img src = "https://user-images.githubusercontent.com/72150188/126937502-b372d9ae-74ce-45cf-b6a8-17f8e5bc9f4c.png">
</p>
<p align = "center">
Fig.1 - Collection results using Newman CLI
</p>
