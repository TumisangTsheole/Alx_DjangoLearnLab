from django.db import models

# Create your models here.
#
# # The Author model represents a writer in the system.
# Each Author can be linked to multiple Book objects (one-to-many relationship).


class Author(models.Model):
    name = models.CharField()


# The Book model represents a published book.
# Each Book belongs to a single Author, enforced by the ForeignKey relationship.
# The 'related_name="books"' allows reverse access: author.books.all()
class Book(models.Model):
    title = models.CharField()
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
