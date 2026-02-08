from datetime import datetime

from rest_framework import serializers

from .models import Author, Book

# BookSerializer converts Book model instances into JSON and vice versa.
# Using "__all__" ensures all fields (id, title, publication_year, author) are included.


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "publication_year", "author"]


# AuthorSerializer converts Author model instances into JSON and vice versa.
# It includes the author's name and a nested list of related books.
# The nested BookSerializer dynamically serializes all books linked to the author.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # nested serializer

    class Meta:
        model = Author
        fields = ["name", "books"]

    # Field-level validation for publication_year
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future (>{current_year})."
            )
        return value
