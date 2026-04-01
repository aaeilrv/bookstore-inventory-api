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
  

## Endpoints

  
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

