# Coffee Shop - Full Stack Project
This is the Full-stack nanodegree program 3rd project, The project's objective is to practice and demonstrate learning:
* Implementing authentication and authorization in Flask
* Designing against key security principals
* Implementing role-based control design patterns
* Securing a REST API
* Applying software system risk and compliance principles

## What Will I Build?
A full stack drink menu application, see more details [here](./Coffee_Shop/README.md).

## Getting Started
You can follow instructions specified in:
1. [`./Coffee_Shop/backend/`](./Coffee_Shop/backend/README.md)
2. [`./Coffee_Shop/frontend/`](./Coffee_Shop/frontend/README.md)

## Postman collection Integeration Test:
Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`

2 users are registerd:
* Barista
  - `can get:drinks-detail`

* Manager
  - can `get:drinks`
  - can `get:drinks-detail`
  - can `post:drinks`
  - can `patch:drinks`
  - can `delete:drinks`


Encoded JWT for Barista:
 ```
 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjkydjQ2dGg2Z1JGUUVjN2swQWZHdCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2xhc3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZmUwYzUxMzU4MmJjMDA2OTQ2MjJkZCIsImF1ZCI6ImRldiIsImlhdCI6MTYyNzI2MzAyNSwiZXhwIjoxNjI3MjcwMjI1LCJhenAiOiJrQzZYdHFMRklwUXhRcTVzbkdpcWJLVU5FRUVHa2dUQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.M8IMXhzxGEE8z3j2Dn-s0tvPWfRHTcEbrCVzkV5z50jGvjVTk5YKgqWYEG9tXT2CYVVG9gw1JYTd7GQi6423nwF93r-OQtCs3HS9jRouldpcLvF5sJ-uS8W2IMQwzyZRdH2U8r6hBadOh9wK6ObzawHs0KDyuNrfbSk4RQPXyxqW3etk1jFFStTz6rwOXpjsbOIGEF7Cr8gVnLtjpa10ytT_Eaeiej1T5DiOicO5DZy1uanzT8bBOHixKNC8wBtt1T5a5X_4Y4mZ50Tf80E-zrOyRAKAmVSr4MdRQ1xsyjz2f2qbIXvZJdckqnRFepdF-tj3VxLJ77xoxmeb4phDMg
 
```
Decoded JWT for Barista Payload Data:
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
 Encoded JWT for Manager:
 ```
 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjkydjQ2dGg2Z1JGUUVjN2swQWZHdCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2xhc3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZmUwYmZhMGY4NjY0MDA2OTJhZGJhYyIsImF1ZCI6ImRldiIsImlhdCI6MTYyNzI2MzMwMiwiZXhwIjoxNjI3MjcwNTAyLCJhenAiOiJrQzZYdHFMRklwUXhRcTVzbkdpcWJLVU5FRUVHa2dUQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.Pyn3yywmyh0updSOzYMTPLjJpjWj-dkA3jTjhnw4VWPymwqI3mBgrBt0Z-rF59R-AmDqLAKHEThoFYHrRnA_eeB3j94v52PaDKyomAsevpZvk97PjwN2vIqBq7LanSz_Cs8fIcjw5m8D7JpgboC0fsJjn3Ch0CTq8Qe8ZWZY1hDxfUJw70MoNO_Cp8Hz4Np_cVuaG_fWe1Hrn0iV6AciqSZehaqr8DvE-_9gpV3D_o2myza6u6KrKJQjxk3WZP4QOvsDlhWj223l8-Kl1MTANq8BvXsOnPjSOFfbejEfu3YlsAeEzqFbhvMHinZ_wm0Uz8bt5Dx6hVHF6LLptDja1A
 ```
 
 Decoded JWT for Manager Payload Data:
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
## Examples 
