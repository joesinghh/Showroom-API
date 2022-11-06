### Showroom API

## Endpoints

1. __register/__

`POST ` 
 Request body :
```json

{
    "username": "demo",
    "password": "demo123*lol",
    "password2": "demo123*lol",
    "email": "demo@gmail.com",
    "is_staff": false
}
```
Response :


```json
{
    "username": "demo",
    "email": "demo@gmail.com",
    "is_staff": false
}
```

2. __api-token-auth/__
`POST`
REquest:
```json
{
    "username":"demo",
    "password":"demo123*lol"
    
}
```
Response
```json
{
    "token": "37ab404fcd602942f35546112ac45131597e7b14"
}
```

3. __profile/__

`GET` 
`header : Authorization : TOKEN <your token>`
Response:
```json
{
    "id": 4,
    "username": "joesingh",
    "is_staff": false
}
```

4. Bike data
no auth required

GET

[
    {
        "id": 1,
        "modelnumber": "123",
        "price": 123,
        "warranty": "1.00",
        "color": "red",
        "category": 1
    },
    {
        "id": 2,
        "modelnumber": "1234",
        "price": 123,
        "warranty": "1.00",
        "color": "red",
        "category": 1
    }
]

5. ADD bikes
POST

{
        "id": 1,
        "modelnumber": "123",
        "price": 123,
        "warranty": "1.00",
        "color": "red",
        "category": 1
    }

6. PUT, DELETE modbike

{
        "id": 2,
        "modelnumber": "1234",
        "price": 123,
        "warranty": "1.00",
        "color": "red",
        "category": 1
    }

DELETE


7. ORDER 
POST

{
    "id": 2,
    "date": "2022-11-06T06:22:28.552038Z",
    "user": 2,
    "bike": 1
}

GET
[
    {
        "id": 1,
        "date": "2022-11-06T06:20:53.069284Z",
        "user": 3,
        "bike": 1
    },
    {
        "id": 2,
        "date": "2022-11-06T06:22:28.552038Z",
        "user": 2,
        "bike": 1
    }
]

6. Order details
{
    "id": 1,
    "date": "2022-11-06T06:20:53.069284Z",
    "user": 3,
    "bike": 1,
    "Warranty Status": "0 days left"
}
