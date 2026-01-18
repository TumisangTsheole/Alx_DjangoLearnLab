from django.urls import path
from .views import list_books, LibraryDetailView, register, UserLoginView, user_logout, admin_view, librarian_view, member_view, add_book, change_book, delete_book

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:book_id>/change/', views.change_book, name='change_book'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
