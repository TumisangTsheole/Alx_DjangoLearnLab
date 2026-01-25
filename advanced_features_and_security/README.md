# Advanced Features and Security

This directory contains a Django project demonstrating advanced features and security best practices, specifically focusing on a custom user model and managing permissions and groups.

## 0. Implementing a Custom User Model in Django

This project replaces Django's default user model with a custom `CustomUser` model located in the `users` app.

### Custom User Model Details:
- **Location**: `advanced_features_and_security/LibraryProject/users/models.py`
- **Base Class**: Extends `AbstractUser` to retain built-in authentication features.
- **Additional Fields**:
    - `date_of_birth`: A `DateField` (nullable).
    - `profile_photo`: An `ImageField` for user profile pictures (nullable, uploads to `profile_photos/`).
- **Custom Manager**: `CustomUserManager` handles the creation of regular users and superusers, ensuring compatibility with the new fields.
- **Admin Integration**: Configured in `advanced_features_and_security/LibraryProject/users/admin.py` to display and manage the new fields in the Django administration interface.
- **Settings Configuration**: `AUTH_USER_MODEL` is set to `'users.CustomUser'` in `advanced_features_and_security/LibraryProject/LibraryProject/settings.py` to instruct Django to use this custom model.
- **Application References**: All `ForeignKey` or other references to the `User` model have been updated to `settings.AUTH_USER_MODEL` or `get_user_model()` to ensure compatibility and flexibility. Specifically, `UserProfile` in `relationship_app/models.py` was updated.

## 1. Managing Permissions and Groups in Django

This project implements a system for managing permissions and groups to control access to various parts of the application, particularly for the `Book` model in the `bookshelf` app.

### Custom Permissions:
- **Location**: Defined in the `Meta` class of the `Book` model (`advanced_features_and_security/LibraryProject/bookshelf/models.py`).
- **Permissions Added**:
    - `can_view_book`: Allows viewing book details and lists.
    - `can_create_book`: Allows adding new books.
    - `can_edit_book`: Allows modifying existing books.
    - `can_delete_book`: Allows deleting books.

### Groups and Role-Based Access Control:
- **Setup**: Groups (`Editors`, `Viewers`, `Admins`) are created via the Django administration interface.
- **Permission Assignment**:
    - **Viewers**: Assigned `can_view_book` permission.
    - **Editors**: Assigned `can_view_book`, `can_create_book`, and `can_edit_book` permissions.
    - **Admins**: Assigned all `bookshelf | book` permissions.

### Enforcing Permissions in Views:
- **Mechanism**: The `@permission_required` decorator from `django.contrib.auth.decorators` is used to protect views in `advanced_features_and_security/LibraryProject/bookshelf/views.py`.
- **Protected Views**:
    - `book_list` and `book_detail`: Protected by `bookshelf.can_view_book`.
    - `book_create`: Protected by `bookshelf.can_create_book`.
    - `book_update`: Protected by `bookshelf.can_edit_book`.
    - `book_delete`: Protected by `bookshelf.can_delete_book`.

## Setup and Usage:

1.  **Navigate to the project directory**:
    ```bash
    cd advanced_features_and_security/LibraryProject
    ```
2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1   # On Windows PowerShell
    # source venv/bin/activate    # On Linux/macOS
    ```
3.  **Install dependencies**:
    ```bash
    pip install Django==6.0.1 Pillow
    ```
4.  **Make and apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  **Create a superuser** (for admin access and group management):
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server**:
    ```bash
    python manage.py runserver
    ```
7.  **Access the Admin Interface**: Go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.
8.  **Configure Groups and Permissions**:
    *   Navigate to "Authentication and Authorization" -> "Groups".
    *   Create the `Editors`, `Viewers`, and `Admins` groups and assign the appropriate `bookshelf | book` permissions as described in the "Groups and Role-Based Access Control" section above.
9.  **Create Test Users and Assign to Groups**:
    *   Navigate to "Authentication and Authorization" -> "Users".
    *   Create test users (e.g., `editor_user`, `viewer_user`, `admin_user`, `normal_user`) and assign them to the relevant groups.
10. **Test Permissions**: Log in as different test users and verify that access to the book-related views (`/books/`, `/books/book/new/`, etc.) is correctly restricted based on their assigned permissions.

