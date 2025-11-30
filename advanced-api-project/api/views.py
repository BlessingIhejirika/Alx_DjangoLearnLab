from rest_framework import generics, filters, permissions, status
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework as filters_drf


class BookListView(generics.ListAPIView):
    """
    Retrieves and returns a list of all Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters_drf.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'publication_year', 'author__name'] # Filter by author's name
    search_fields = ['title', 'author__name'] # Fields to search across
    ordering_fields = ['title', 'publication_year'] # Fields to order by



class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single Book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    
    
    """
    Creates a new Book.
    Custom behavior:
        - Ensures user is authenticated.
        - Handles validation errors gracefully.
        - Adds a custom response message.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Override create() to provide custom response formatting
        and improved validation handling.
        """
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response(
                {"error": "Invalid data submitted", "details": e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Save the book instance
        self.perform_create(serializer)

        return Response(
            {
                "message": "Book created successfully",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing Book.
    Custom behavior:
        - Ensures user is authenticated.
        - Custom success message.
        - Handles validation errors.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        """
        Override update() for custom validation and messaging.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial
        )

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response(
                {"error": "Update failed", "details": e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_update(serializer)

        return Response(
            {
                "message": "Book updated successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )


class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a Book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

