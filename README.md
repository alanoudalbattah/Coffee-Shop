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

## Postman collection Integeration Test
Import [postman](https://www.postman.com/) collection [`./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`](./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`)

## RBAC permission claims
#### Two users are registerd:
* Barista
  - `can get:drinks-detail`

* Manager
  - can `get:drinks`
  - can `get:drinks-detail`
  - can `post:drinks`
  - can `patch:drinks`
  - can `delete:drinks`


##### Example of Encoded JWT for Barista:
 ```
 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjkydjQ2dGg2Z1JGUUVjN2swQWZHdCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2xhc3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZmUwYzUxMzU4MmJjMDA2OTQ2MjJkZCIsImF1ZCI6ImRldiIsImlhdCI6MTYyNzI3MDg3NCwiZXhwIjoxNjI3Mjc4MDc0LCJhenAiOiJrQzZYdHFMRklwUXhRcTVzbkdpcWJLVU5FRUVHa2dUQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.Y-huiE1XK1hJIAG7bczI4FKX49TEwNpe5sCii8ZupdyFnh2na5hJN7nXRIav5rcoGOBPl5mNV8gBryawdBHf8I8x9C0yQLGKnJeP9sOJ0DUCRnZdvZjGiUzEVw2S1rjaqpHEUtgb8ASAijrUYsOlHJd4Sj3d8kBJnZGkckOhh3T8Rrf6D8lwvfLJeKrNIQpxXlkZE6BJ72hTuH1UlRx-d4pwGFVkxacnhCw3LUJzXA-t4W_5PkkNabqxhwG4k3m0SHMdVTVL9SOx1Am5ueZK0gNs9zxQZ_ecTME69BaSregXkl88e9nPdvnurcF82SMqkkvXrJtx3JuU_LWLMpsduw
 ```
##### Example of Decoded JWT for Barista Payload Data:
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
 ##### Example of Encoded JWT for Manager:
 ```
 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjkydjQ2dGg2Z1JGUUVjN2swQWZHdCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2xhc3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZmUwYmZhMGY4NjY0MDA2OTJhZGJhYyIsImF1ZCI6ImRldiIsImlhdCI6MTYyNzI2MzMwMiwiZXhwIjoxNjI3MjcwNTAyLCJhenAiOiJrQzZYdHFMRklwUXhRcTVzbkdpcWJLVU5FRUVHa2dUQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.Pyn3yywmyh0updSOzYMTPLjJpjWj-dkA3jTjhnw4VWPymwqI3mBgrBt0Z-rF59R-AmDqLAKHEThoFYHrRnA_eeB3j94v52PaDKyomAsevpZvk97PjwN2vIqBq7LanSz_Cs8fIcjw5m8D7JpgboC0fsJjn3Ch0CTq8Qe8ZWZY1hDxfUJw70MoNO_Cp8Hz4Np_cVuaG_fWe1Hrn0iV6AciqSZehaqr8DvE-_9gpV3D_o2myza6u6KrKJQjxk3WZP4QOvsDlhWj223l8-Kl1MTANq8BvXsOnPjSOFfbejEfu3YlsAeEzqFbhvMHinZ_wm0Uz8bt5Dx6hVHF6LLptDja1A
 ```
 
 ##### Example of Decoded JWT for Manager Payload Data:
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
