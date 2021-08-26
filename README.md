# Product store
    Some description
    

# Installation guide
    - Install mongo database;
 
# REST API Description:

    **Create product:**   
    curl --request POST 'http://localhost:8000/create' --header 'Content-Type: application/json' --data-raw '{"collection": "new_collection", "name": "Nokia3311", "description": "Super telephone", "parameters": [{ "color": "blue"}, {"camera": "4032x3024pixels"}, {"games": "snake"}]}'
    Request:
    URL: server_ip:8000/create
    Method: POST
    Headers: 'Content-Type: application/json'
    Body:
    {
    "collection": "new_collection",
    "name": "Nokia3310",
    "description": "Super telephone",
    "parameters": [{ "color": "blue"}, {"camera": "4032x3024pixels"}, {"games": "snake"}]
    }
    Success Response:
    {
    "response": "Item successfully created"
    }
    Code: HTTP 201 Created
    
    **Get all products**
    curl --request POST 'localhost:8000/find' --header 'Content-Type: application/json' --data-raw '{"collection": "new_collection"}'
    Request:
    URL: server_ip:8000/find
    Method: POST
    Headers: 'Content-Type: application/json'
    Body:
    {
    "collection": "new_collection"
    }
    Success Response:
    {
    "result": [
        {
            "id": "612547e28a758c2b00090465",
            "name": "Samsung"
        },
        {
            "id": "612548a48a05e8deb1dd5cea",
            "name": "Iphone5"
        },
        {
            "id": "612548e9e8b493b8ae1d2b70",
            "name": "Iphone7"
        },
        {
            "id": "612549005daa822ab3536cd6",
            "name": "IpadMini"
        },
        {
            "id": "6126df285e7394202bd2ee84",
            "name": "Nokia3310"
        },
        {
            "id": "6126df4c3788c76d9b68ed15",
            "name": "Nokia3320"
        },
        {
            "id": "6126df9e5e7394202bd2ee86",
            "name": "Nokia3310"
        }
    ]
    }
    Code: HTTP 200 OK
    
    **Search products by name:**
    curl --request POST 'http://localhost:8000/find' --header 'Content-Type: application/json' --data-raw '{"collection": "new_collection", "name": "Nokia3310"}'
    Request:
    URL: server_ip:8000/find
    Method: POST
    Headers: 'Content-Type: application/json'
    Body:
    {
    "collection": "new_collection"
    "name": "Nokia3310"
    }
    Success Response:
    {
    "result": [
        {
            "id": "6126df285e7394202bd2ee84",
            "name": "Nokia3310"
        },
        {
            "id": "6126df9e5e7394202bd2ee86",
            "name": "Nokia3310"
        }
    ]
    }
    Code: HTTP 200 OK
    
    **Search products by parameters:**
    curl --request POST 'http://localhost:8000/find' --header 'Content-Type: application/json' --data-raw '{"collection": "new_collection", "parameters": {"color" : "green"}}'
    Request:
    URL: server_ip:8000/find
    Method: POST
    Headers: 'Content-Type: application/json'
    Body:
    {
    "collection": "new_collection",
    "parameters": {"color" : "green"}
    }
    Success Response:
    {
    "result": [
        {
            "id": "6126df285e7394202bd2ee84",
            "name": "Nokia3310"
        },
        {
            "id": "6126df4c3788c76d9b68ed15",
            "name": "Nokia3320"
        }
    ]
    }
    Code: HTTP 200 OK
    
    **Get detail product information by id:**
    curl --request GET 'http://localhost:8000/find?colname=new_collection&id=6126df285e7394202bd2ee84'
    Request:
    URL: server_ip:8000/find
    Method: GET
    Headers: 'Content-Type: application/json'
    Params: colname, id
    Success Response:
    {
    "result": {
        "description": "Super telephone",
        "id": "6126df285e7394202bd2ee84",
        "name": "Nokia3310",
        "parameters": [
            {
                "color": "green"
            },
            {
                "camera": "4032x3024pixels"
            },
            {
                "games": "snake"
            }
        ]
    }
    }
    Code: HTTP 200 OK
