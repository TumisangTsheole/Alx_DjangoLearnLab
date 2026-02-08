# Advanced API Project

This project uses the Django REST Framework's **generic views** to implement CRUD operations for the 'Book' model

---

## Endpoints
- 'GET /books/' -> List all books (openly accessible)
- 'GET /books/<id>/' -> Retireve a single book by ID (openly accessible)
- 'POST /books/create/' -> Create a new book (authenticated users only)
- 'PUT/PATCH /books/<id>/update' -> Update an existing book (authenticated book only)
- DELETE /books/<id>/delete/' -> Delete a book (authenticated users only)

---

## Permissions
- **ListView & DetailView** -> 'AllowAny' (unauthenticated users can read)
- **CreateView, UpdateView, DeleteView** -> 'IsAuthenticated' (only logged-in users can modify data)

---

## Advanced Features

### Filtering
You can filter the books by `title`, `author`, and `publication_year`.

Example: `GET /books/?publication_year=2024`

### Searching
You can search the books by `title` and `author`.

Example: `GET /books/?search=Test`

### Ordering
You can order the books by `title` and `publication_year`.

Example: `GET /books/?ordering=title`
