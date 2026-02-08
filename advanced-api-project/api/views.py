from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


# Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # allow anyone


# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # must be logged in

    def perform_create(self, serializer):
        serializer.save()  # Save validated data to DB

    def create(self, request, *args, **kwargs):
        """
        Override create() to customize response format and validation handling.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # enforce validation
        self.perform_create(serializer)
        return Response(
            {"message": "Book created successfully!", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )


# Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # must be logged in

    def perform_update(self, serializer):
        """
        Custom hook to handle extra logic during update.
        For example, you could enforce role-based restrictions here.
        """
        serializer.save()

    def update(self, request, *args, **kwargs):
        """
        Override update() to customize response format and validation handling.
        """
        partial = kwargs.pop("partial", False)  # allow PATCH
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)  # enforce validation
        self.perform_update(serializer)
        return Response(
            {"message": "Book updated successfully!", "data": serializer.data},
            status=status.HTTP_200_OK,
        )


# Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
