import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")

def list_all_books_in_library(library_name):
    """
    List all books in a library.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}.")

if __name__ == '__main__':
    # Create some sample data
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.R.R. Tolkien")

    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="The Hobbit", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book3)

    librarian1 = Librarian.objects.create(name="Mr. Smith", library=library1)

    # Run the queries
    query_all_books_by_author("George Orwell")
    print("-" * 20)
    list_all_books_in_library("Central Library")
    print("-" * 20)
    retrieve_librarian_for_library("Central Library")
