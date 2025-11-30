
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Author(models.Model):
    """
    Represents a book author in the system.

    This model stores information about an author and defines a
    one-to-many relationship with the Book model.

    Relationship:
        - One Author can have multiple Books.
        - Access an author's books using: author.books.all()
    """
     
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Book(models.Model):
    """
    Represents a book written by an author.

    Fields:
        - title: Title of the book.
        - publication_year: The year the book was published.
        - author: ForeignKey linking the book to an Author.

    Relationship:
        - Many Books belong to one Author (Many-to-One).
        - Uses `related_name='books'` so books for an author can be accessed via:
              author_instance.books.all()
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"