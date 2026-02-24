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

## Features

- **Posts & Comments:** Full CRUD for posts and comments.
- **Filtering:** Search posts by title or content using `?search=query`.
- **Following:** Follow and unfollow users.
- **Feed:** View posts from followed users at `/api/feed/`.
- **Likes:** Like and unlike posts.
- **Notifications:** Receive notifications for likes, comments, and follows at `/api/notifications/`.

## Testing

Testing was performed using Postman to verify:
1. User registration and token generation.
2. CRUD operations for posts and comments with author permissions.
3. Follow/unfollow logic and feed aggregation.
4. Like/unlike functionality and notification creation.
5. Notification retrieval for the current user.

## User Model

The custom user model `CustomUser` extends `AbstractUser` and includes:
- `bio`: A text field for user biography.
- `profile_picture`: An image field for user profile picture.
- `followers`: A many-to-many relationship with self to track follows.
