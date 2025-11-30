from rest_framework import serializers
from datetime import datetime
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    Responsibilities:
        - Serializes all fields of the Book model.
        - Validates data when creating or updating Book instances.
        - Ensures the publication_year is not set to a future year.

    Validation:
        - validate_publication_year(): Custom validator that prevents books
          from having a publication year beyond the current year.
    """
    
    class Meta:
        model = Book
        fields = "__all__"     # serialize all model fields

    # custom validation
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future ({current_year})."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    Responsibilities:
        - Serializes the author's name.
        - Includes a nested representation of the author's books.

    Nested Relationship:
        - Uses a read-only nested BookSerializer.
        - Displays all books associated with an author.
        - Works because the Book model defines `related_name='books'`,
          enabling reverse lookup via author.books.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = [
            "name",
            "books",
        ]
