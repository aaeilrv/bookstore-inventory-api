## Bookstore Inventory API

  

Django REST API for managing bookstore inventory.

  

This project implements a backend system for a bookstore that needs to manage book inventory and validate prices against current exchange rates.

  

### Prerequisites

- Docker

- Docker Compose

  

### Build and Run with Docker

  

```bash
# Build the image
docker  build  -t  bookstore-api  .
```

  
```bash
# Run the container
docker  run  -p  8000:8000  --env-file  .env  bookstore-api
```
  

### Docker Compose
```bash
# Start all services
docker  compose  up
```


```bash
# Stop all services
docker  compose  down
```

  
```bash
# Start services in detached mode
docker  compose  up  -d
```

```bash
# View logs
docker  compose  logs  -f
```
  
```bash
# Rebuild and start
docker  compose  up  --build
```

### Migrations

```bash
# Make migrations
docker exec bookstore-web python manage.py makemigrations
```

```bash
# Migrate
docker exec bookstore-web python manage.py migrate
```
  

## API Documentation

### Base URL
```bash
http://localhost:8000/api/
```
### Endpoints
  
| Method | Endpoint | Description| 
|--|--|--|
| **POST**| /books/ | Create  a  new  book |
|  **GET**  |  /books/  |  Retrieve  all  books (with pagination)|
|  **GET**  |  /books/{id}/  |  Retrieve  a  book  by  ID  |
|  **PUT**  |  /books/{id}/  |  Update  a  book  |
|  **DELETE**  |  /books/{id}/  |  Delete  a  book  |
|  **GET**  |  /books/search/?category={category}/  |  Get  books  by  category  |
|  **GET**  |  /books/search/?threshold={threshold}/|Get  books  with  stock  lower  than  specified  threshold|
|  **POST**  |  /books/{id}/calculate-price/  |  Calculate  suggested  selling  price  for  a  book  |

### Examples

 **1. Create a Book**
**Request**
```bash
POST /api/books/
Content-Type: application/json
{
	"title":  "El Quijote",
	"author":  "Miguel de Cervantes",
	"isbn":  "978-84-376-0494-1",
	"cost_usd":  15.99,
	"stock_quantity":  25,
	"category":  "Literatura Clásica",
	"supplier_country":  "ES",
	"selling_price_local":  null
}
```

**Response**
```bash
Response Status: 201 CREATED	
{
	"id":  "9259621d-d003-489e-ac35-4f30392dbeb2",
	"title":  "El Quijote",
	"author":  "Miguel de Cervantes",
	"isbn":  "978-84-376-0494-1",
	"cost_usd":  15.99,
	"selling_price_local":  null,
	"stock_quantity":  25,
	"category":  "Literatura Clásica",
	"supplier_country":  "ES",
	"created_at":  "2026-04-01T17:46:28.468912Z",
	"updated_at":  "2026-04-01T17:46:28.468928Z"
}
```

**Constraints**
- `isbn` must be unique, have either 10 or 13 digits and no characters except for dashes (-).
- `cost_usd` must be greater than 0.
- `stock_quantity` must not be negative.

---

**2. Retrieve all books**

**Request**
```bash
# first page
GET /api/books/

# other pages
GET /api/books/?page={page_number}
```

**Response**
```bash
Response Status: 200 OK
{
	"count":  25,
	"next":  "http://localhost:8000/api/books/?page=2",
	"previous":  null,
	"results":  [
		{
			"id":  "caf9c3c7-3c51-4f2c-901d-9d1b27a5ea69",
			"title":  "Cien Años de Soledad",
			"author":  "Gabriel García Márquez",
			"isbn":  "978-84-376-0494-7",
			"cost_usd":  18.5,
			"selling_price_local":  null,
			"stock_quantity":  42,
			"category":  "Literatura Latinoamericana",
			"supplier_country":  "CO",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "701f7be8-1047-42d5-9ea7-2d142a18d724",
			"title":  "1984",
			"author":  "George Orwell",
			"isbn":  "978-04-523-5243-6",
			"cost_usd":  12.99,
			"selling_price_local":  null,
			"stock_quantity":  37,
			"category":  "Ciencia Ficción",
			"supplier_country":  "GB",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "32d13e77-8edb-436b-a138-252d61858929",
			"title":  "El Alquimista",
			"author":  "Paulo Coelho",
			"isbn":  "978-06-062-5101-3",
			"cost_usd":  14.99,
			"selling_price_local":  null,
			"stock_quantity":  53,
			"category":  "Ficción",
			"supplier_country":  "BR",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "91f0e909-59d5-482d-b090-86c9fa26afd6",
			"title":  "Orgullo y Prejuicio",
			"author":  "Jane Austen",
			"isbn":  "978-01-435-1094-7",
			"cost_usd":  11.99,
			"selling_price_local":  null,
			"stock_quantity":  28,
			"category":  "Literatura Clásica",
			"supplier_country":  "GB",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "c7a45666-dd69-4962-ae62-65dd47b8dde4",
			"title":  "El Gran Gatsby",
			"author":  "F. Scott Fitzgerald",
			"isbn":  "978-07-432-6476-5",
			"cost_usd":  13.5,
			"selling_price_local":  null,
			"stock_quantity":  31,
			"category":  "Literatura Clásica",
			"supplier_country":  "US",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "08b633b7-0724-4e5e-ac57-5f9f8c0633e1",
			"title":  "Matar a un Ruiseñor",
			"author":  "Harper Lee",
			"isbn":  "978-00-611-2006-8",
			"cost_usd":  16.99,
			"selling_price_local":  null,
			"stock_quantity":  22,
			"category":  "Ficción",
			"supplier_country":  "US",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "149cb45b-5545-4f0d-9c0e-fa2b452a0a72",
			"title":  "La Sombra del Viento",
			"author":  "Carlos Ruiz Zafón",
			"isbn":  "978-84-008-3258-2",
			"cost_usd":  19.99,
			"selling_price_local":  null,
			"stock_quantity":  19,
			"category":  "Misterio",
			"supplier_country":  "ES",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "a98c8f7e-803e-4afb-83f8-6dbe91b53e0c",
			"title":  "El Código Da Vinci",
			"author":  "Dan Brown",
			"isbn":  "978-03-854-5045-6",
			"cost_usd":  17.5,
			"selling_price_local":  null,
			"stock_quantity":  64,
			"category":  "Suspenso",
			"supplier_country":  "US",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "e8edf4c7-e60c-4acf-9d92-5ae9eb906311",
			"title":  "Harry Potter y la Piedra Filosofal",
			"author":  "J.K. Rowling",
			"isbn":  "978-04-743-9627-4",
			"cost_usd":  22.99,
			"selling_price_local":  null,
			"stock_quantity":  89,
			"category":  "Fantasía",
			"supplier_country":  "GB",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "2a9c5b44-2152-4536-a479-3cd2dbe88eb5",
			"title":  "El Principito",
			"author":  "Antoine de Saint-Exupéry",
			"isbn":  "978-01-567-2400-3",
			"cost_usd":  9.99,
			"selling_price_local":  null,
			"stock_quantity":  76,
			"category":  "Literatura Infantil",
			"supplier_country":  "FR",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		}
	]
}
```

**Pagination**
- Uses the default pagination system of Django REST Framework.
- Currently set at 10 records per page.

---

**3. Get book by ID**

**Request**
```bash
GET /api/books/{id}
```

**Response**
```bash
# Book exists
Response Status: 200 OK
{
	"id":  "9259621d-d003-489e-ac35-4f30392dbeb2",
	"title":  "El Quijote",
	"author":  "Miguel de Cervantes",
	"isbn":  "978-84-376-0494-1",
	"cost_usd":  15.99,
	"selling_price_local":  null,
	"stock_quantity":  25,
	"category":  "Literatura Clásica",
	"supplier_country":  "ES",
	"created_at":  "2026-04-01T17:46:28.468912Z",
	"updated_at":  "2026-04-01T17:46:28.468928Z"
}

#Book doesn't exist
Response Status: 400 Not Found
{
	"detail":  "Not found."
}
```

---

**4. Update Book**

**Request**
```bash
PUT /api/books/{id}
Content-Type: application/json

{
	"title":  "El Quijote",
	"author":  "Miguel de Cervantes",
	"isbn":  "978-84-376-0494-1",
	"cost_usd":  28,
	"selling_price_local":  null,
	"stock_quantity":  25,
	"category":  "Literatura Clásica",
	"supplier_country":  "ES",
	"created_at":  "2026-04-01T17:46:28.468912Z",
	"updated_at":  "2026-04-01T17:46:28.468928Z"
}
```


**Response**
```bash
# Book exists
Response Status: 200 OK
{
	"id":  "9259621d-d003-489e-ac35-4f30392dbeb2",
	"title":  "El Quijote",
	"author":  "Miguel de Cervantes",
	"isbn":  "978-84-376-0494-1",
	"cost_usd":  28.0,
	"selling_price_local":  null,
	"stock_quantity":  25,
	"category":  "Literatura Clásica",
	"supplier_country":  "ES",
	"created_at":  "2026-04-01T17:46:28.468912Z",
	"updated_at":  "2026-04-01T17:50:33.958687Z"
}

#Book doesn't exist
Response Status: 400 Not Found
{
	"detail":  "Not found."
}
```

---

**5. Delete Book**

**Request**
```bash
DELETE /api/books/{id}
```


**Response**
```bash
# Book exists
Response Status: 204 No Content

#Book doesn't exist
Response Status: 400 Not Found
{
	"detail":  "Not found."
}
```

---

**6. Search by Category**

**Request**
```bash
GET /api/books/search?category={category}
```


**Response**
```bash
# Book exists
Response Status: 200 OK
{
	"count":  1,
	"category":  "misterio",
	"books":  [
		{
			"id":  "149cb45b-5545-4f0d-9c0e-fa2b452a0a72",
			"title":  "La Sombra del Viento",
			"author":  "Carlos Ruiz Zafón",
			"isbn":  "978-84-008-3258-2",
			"cost_usd":  19.99,
			"selling_price_local":  null,
			"stock_quantity":  19,
			"category":  "Misterio",
			"supplier_country":  "ES",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		}
	]	
}

#Category doesn't have books
Response Status: 200 OK
{
	"count":  0,
	"category":  "literatura clasica",
	"books":  []
}

# Didn't add category field
Response Status: 400 Bad Request
{
	"error":  "Category parameter cannot be empty."
}
```

---


**7. Search by Low Stock**

**Request**
```bash
GET /api/books/low-stock?threshold={threshold}
```


**Response**
```bash
# There are books below threshold
{
	"count":  5,
	"threshold":  "23",
	"books":  [
		{
			"id":  "669a6f69-dee4-4e17-a863-dc9fd80a3fbb",
			"title":  "Rayuela",
			"author":  "Julio Cortázar",
			"isbn":  "978-84-376-0494-9",
			"cost_usd":  21.99,
			"selling_price_local":  null,
			"stock_quantity":  15,
			"category":  "Literatura Latinoamericana",
			"supplier_country":  "AR",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "d4cce1dd-8485-4f88-a361-02a9b737985e",
			"title":  "La Insoportable Levedad del Ser",
			"author":  "Milan Kundera",
			"isbn":  "978-06-094-5312-2",
			"cost_usd":  16.99,
			"selling_price_local":  null,
			"stock_quantity":  18,
			"category":  "Ficción",
			"supplier_country":  "CZ",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "149cb45b-5545-4f0d-9c0e-fa2b452a0a72",
			"title":  "La Sombra del Viento",
			"author":  "Carlos Ruiz Zafón",
			"isbn":  "978-84-008-3258-2",
			"cost_usd":  19.99,
			"selling_price_local":  null,
			"stock_quantity":  19,
			"category":  "Misterio",
			"supplier_country":  "ES",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "08b633b7-0724-4e5e-ac57-5f9f8c0633e1",
			"title":  "Matar a un Ruiseñor",
			"author":  "Harper Lee",
			"isbn":  "978-00-611-2006-8",
			"cost_usd":  16.99,
			"selling_price_local":  null,
			"stock_quantity":  22,
			"category":  "Ficción",
			"supplier_country":  "US",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		},
		{
			"id":  "e5281ea9-a56c-471d-9565-0643c12e8788",
			"title":  "El Amor en los Tiempos del Cólera",
			"author":  "Gabriel García Márquez",
			"isbn":  "978-84-000-0005-3",
			"cost_usd":  20.99,
			"selling_price_local":  null,
			"stock_quantity":  23,
			"category":  "Literatura Latinoamericana",
			"supplier_country":  "CO",
			"created_at":  "2026-04-01T17:58:03.875697Z",
			"updated_at":  "2026-04-01T17:58:03.875697Z"
		}
	]
}

# No books below threshold
Response Status: 200 OK
{
	"count":  0,
	"threshold":  "10",
	"books":  []
}

# Didn't add threshold
{
	"error":  "Threshold parameter cannot be empty."
}

```

---


**8. Calculate Selling Price**

**Request**
```bash
POST /api/books/{book_id}/calculate-price/
```

**Response**
```bash
# Book exists
Response Status: 200 OK
	{
		"book_id":  "c7a45666-dd69-4962-ae62-65dd47b8dde4",
		"cost_usd":  13.5,
		"exchange_rate":  473.92,
		"cost_local":  6397.92,
		"margin_percentage":  40,
		"selling_price_local":  8957.088,
		"currency":  "VES",
		"calculation_timestamp":  "2026-04-01T18:11:54.986086Z"
	}

# Book doesn't exist
	{
		"detail":  "Not found."
	}
```