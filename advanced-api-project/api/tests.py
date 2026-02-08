from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author

class BookTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", author=self.author, publication_year=2024)

    def test_create_book(self):
        url = reverse("book-create")
        data = {"title": "New Book", "author": self.author.id, "publication_year": 2025}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, "New Book")

    def test_get_books(self):
        url = reverse("book-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_book(self):
        url = reverse("book-detail", kwargs={"pk": self.book.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_update_book(self):
        url = reverse("book-update", kwargs={"pk": self.book.pk})
        data = {"title": "Updated Book"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book.pk).title, "Updated Book")

    def test_delete_book(self):
        url = reverse("book-delete", kwargs={"pk": self.book.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = reverse("book-list")
        response = self.client.get(url + "?publication_year=2024", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_search_books(self):
        url = reverse("book-list")
        response = self.client.get(url + "?search=Test", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_order_books(self):
        Book.objects.create(title="Another Book", author=self.author, publication_year=2023)
        url = reverse("book-list")
        response = self.client.get(url + "?ordering=publication_year", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["title"], "Another Book")