# Advanced API Project - Book Management

This project is an API built with **Django REST Framework (DRF)** to manage books and authors. It demonstrates CRUD operations using DRF's **generic views**, custom validations, permissions, and search filters.

---

## API Views Overview

The project exposes the following views for the **Book model**:

### 1. BookListView
- **URL:** `/api/books/`
- **Method:** GET
- **Description:** Retrieves all books in the system.
- **Features:**
  - Uses `ListAPIView`.
  - Supports search filtering by `title` or `publication_year`.
  - No authentication required.

### 2. BookDetailView
- **URL:** `/api/books/<id>/`
- **Method:** GET
- **Description:** Retrieves a single book by its ID.
- **Features:**
  - Uses `RetrieveAPIView`.
  - Returns 404 if the book does not exist.
  - No authentication required.

### 3. BookCreateView
- **URL:** `/api/books/create/`
- **Method:** POST
- **Description:** Creates a new book.
- **Features:**
  - Requires authentication (`IsAuthenticated`).
  - Custom `create()` method provides:
    - Enhanced validation error messages.
    - Custom success response JSON.
  - Automatically uses the `BookSerializer` validation.
- **Custom Hooks:**
  - `create()`
  - `perform_create()`

### 4. BookUpdateView
- **URL:** `/api/books/<id>/update/`
- **Method:** PUT/PATCH
- **Description:** Updates an existing book.
- **Features:**
  - Requires authentication.
  - Supports full or partial updates.
  - Custom `update()` method provides:
    - Custom error handling.
    - Custom success message.
- **Custom Hooks:**
  - `update()`
  - `perform_update()`

### 5. BookDeleteView
- **URL:** `/api/books/<id>/delete/`
- **Method:** DELETE
- **Description:** Deletes a book by its ID.
- **Features:**
  - Requires authentication.
  - Uses `DestroyAPIView`.
  - Returns HTTP 204 No Content on success.

---

## Custom Configurations

- **Permissions:**  
  - `IsAuthenticated` is required for Create, Update, and Delete views.
- **Filters:**  
  - `SearchFilter` applied to ListView.
  - Searchable fields: `title`, `publication_year`.
- **Validation:**  
  - Custom validation in the serializer ensures `publication_year` is not in the future.
- **Custom Response Messages:**  
  - Create and Update views return JSON with `message` and `data` keys.
- **Error Handling:**  
  - Validation errors return structured JSON with details.

---

## Testing the API

### API Endpoints

# List all books
GET /api/books/

# Retrieve a single book
GET /api/books/<id>/

# Create a new book (requires authentication)
POST /api/books/create/
Body:
{
  "title": "New Book",
  "publication_year": 2023,
  "author": 1
}

# Update an existing book (requires authentication)
PUT /api/books/<id>/update/
Body:
{
  "title": "Updated Title",
  "publication_year": 2022,
  "author": 1
}

# Delete a book (requires authentication)
DELETE /api/books/<id>/delete/
