## Bookstore Inventory API
Django REST API for managing bookstore inventory.
This project implements a backend system for a bookstore that needs to manage book inventory and validate prices against current exchange rates.


### Build and Run with Docker
```bash
# Build the image
docker build -t bookstore-api .

# Run the container
docker run -p 8000:8000 --env-file .env bookstore-api
```

### Docker Compose
```bash
# Start all services
docker-compose up

# Stop all services
docker-compose down
```

## Documentation

### Base URL
```
http://localhost:8000/api/
```

### Endpoints
[POST] */books/*: Creates book
[GET] */books/*: Retrieves all the books
[GET] */books/{id}/*: Retrieves book by ID
[PUT] */books/{id}/*: Updates book
[DELETE] */books/{id}/*: Deletes book
[GET] */books/search?category={category}/*: Gets books by category 
[GET] */books/search?threshold={threshold}/*: Gets book with stock lower than specified threshold 
[POST] */books/{id}/calculate-price/* Calculates suggested selling price for book