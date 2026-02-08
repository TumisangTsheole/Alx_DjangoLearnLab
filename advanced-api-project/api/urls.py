from django.urls import path

from .views import (
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookListView,
    BookUpdateView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("create/", BookCreateView.as_view(), name="book-create"),
    path("<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]
