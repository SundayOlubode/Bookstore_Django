# Bookstore API - DJANGO
A Bookstore API to obtain information about authors and their books

---
## Stack
*Language: Python(Django).
*Database: Django model.

---

## How To Test:
- You can test the API by making request to the routes below using *POSTMAN*
- Live Link: https://bookstore-1tb0.onrender.com

## Basic Features

- Author's Registration.
- Login (Session-based).
- Get all books.
- Create a new book.
  

## Author
| field     | type      | constraints |
| --------- | --------- | ----------- |
| email     | CharField | required    |
| firstname | CharField | required    |
| lastname  | CharField | required    |
| password  | CharField | required    |
| dob       | DateField | required    |
| bio       | TextField | required    |

## Book
| field         | type         | constraints |
| ------------- | ------------ | ----------- |
| title         | CharField    | required    |
| released_year | DateField    | required    |
| author        | ForeignKey   | required    |
| price         | IntegerField | required    |
| description   | TextField    | required    |
| created_at    | DateField    | required    |

### Register Author

- Route: api/v1/register/   
- Method: POST
- Body: 
```
{
    "email": "msmith@gmail.com",
    "password": "zuzu",
    "firstname": "Messiah",
    "lastname": "Smith",
    "dob": "1991-09-10",
    "bio": "Author of 12 books of science fiction"
}
```

- Responses

Success
```
{
    "message": "Author registered successfully!",
    "data": {
        "id": 4,
        "email": "msmith@gmail.com",
        "password": null,
        "firstname": "Messiah",
        "lastname": "Smith",
        "dob": "1991-09-10",
        "bio": "Author of 12 books of science fiction"
    }
}

```
### Login Author

- Route: api/v1/login/   
- Method: POST
- Body: 
```
{
    "email": "msmith@gmail.com",
    "password": "zuzu"
}
```

- Responses

Success
```
{
    "message": "Login successful!",
    "data": {
        "id": 4,
        "email": "msmith@gmail.com",
        "password": null,
        "firstname": "Messiah",
        "lastname": "Smith",
        "dob": "1991-09-10",
        "bio": "Author of 12 books of science fiction"
    }
}

```
### Get All Books

- Route: api/v1/books/   
- Method: GET

- Responses

Success
```
{
    "message": "Get All Books Successful!",
    "data": [
        {
            "id": 1,
            "title": "The Lake of Avalon",
            "released_year": "1975-08-01",
            "price": 12,
            "description": "Many don't believe",
            "created_at": "2023-05-19T15:28:39.579289Z",
            "author": 5
        },
        {
            "id": 2,
            "title": "The science of living",
            "released_year": "2002-09-09",
            "price": 40,
            "description": "A science of living organisms, including men",
            "created_at": "2023-05-20T22:46:37.411280Z",
            "author": 4
        },
        {
            "id": 3,
            "title": "The birth of science",
            "released_year": "2012-01-08",
            "price": 35,
            "description": "A origination of science",
            "created_at": "2023-05-20T22:50:11.504201Z",
            "author": 4
        },
        {
            "id": 4,
            "title": "The art of living right",
            "released_year": "2022-09-09",
            "price": 45,
            "description": "Christ-centred living pattern",
            "created_at": "2023-05-20T22:51:27.945009Z",
            "author": 5
        }
    ]
}

```
### Add a Book

- Route: api/v1/add_book/   
- Method: POST
- Body: 
```
{
    "title": "The art of living right",
    "released_year": "2022-09-09",
    "price": 45,
    "description": "Christ-centred living pattern"
}
```

- Responses

Success
```
{
    "message": "Book added successfully!",
    "data": {
        "id": 4,
        "title": "The art of living right",
        "released_year": "2022-09-09",
        "price": 45,
        "description": "Christ-centred living pattern",
        "created_at": "2023-05-20T22:51:27.945009Z",
        "author": 5
    }
}
```
### Update a Book

- Route: api/v1/update/   
- Method: POST
- Body: 
```
{
    "title": "The art of living right",
    "released_year": "2022-09-09",
    "price": 45,
    "description": "Christ-centred living pattern"
}
```

- Responses

Success
```
{
    "message": "Book added successfully!",
    "data": {
        "id": 4,
        "title": "The art of living right",
        "released_year": "2022-09-09",
        "price": 45,
        "description": "Christ-centred living pattern",
        "created_at": "2023-05-20T22:51:27.945009Z",
        "author": 5
    }
}
```
## Author
- S. Samuel Olubode