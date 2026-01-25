# CRUD Operations Documentation

## Create Operation

Command:
```python
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

Output:
```
# <Book: 1984>
```

## Retrieve Operation

Command:
```python
from bookshelf.models import Book
Book.objects.get(title="1984")
```

Output:
```
# <Book: 1984>
```

## Update Operation

Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```

Output:
```
# The book title is now "Nineteen Eighty-Four"
```

## Delete Operation

Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
```

Output:
```
# (1, {'bookshelf.Book': 1})
# <QuerySet []>
```
