# Social Media API

A robust social media API built with Django and Django REST Framework.

## Setup Instructions

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install django djangorestframework Pillow
    ```
3.  Navigate to the project directory:
    ```bash
    cd social_media_api
    ```
4.  Run migrations:
    ```bash
    python manage.py migrate
    ```

## User Authentication

- **Register:** `POST /api/register/` with `username`, `password`, `email`, `bio`, and `profile_picture`.
- **Login:** `POST /api/login/` with `username` and `password`. Returns an authentication token.
- **Profile:** `GET /api/profile/` (Authenticated) - Retrieve and update user profile.

Authentication is handled via Token Authentication. Include `Authorization: Token <your_token>` in the headers for protected endpoints.

## User Model

The custom user model `CustomUser` extends `AbstractUser` and includes:
- `bio`: A text field for user biography.
- `profile_picture`: An image field for user profile picture.
- `followers`: A many-to-many relationship with self to track follows.
