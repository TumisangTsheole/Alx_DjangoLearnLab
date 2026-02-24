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

### Authentication & Profiles
- `POST /api/register/`: Register a new user.
- `POST /api/login/`: Login and get a token.
- `GET /api/profile/`: Get current user profile.
- `PUT/PATCH /api/profile/`: Update current user profile.

### Posts & Comments
- `GET /api/posts/`: List all posts.
- `POST /api/posts/`: Create a new post.
- `GET /api/posts/<id>/`: Retrieve a post.
- `PUT/PATCH /api/posts/<id>/`: Update a post (Author only).
- `DELETE /api/posts/<id>/`: Delete a post (Author only).
- `GET /api/comments/`: List all comments.
- `POST /api/comments/`: Create a comment.

### Following & Feed
- `POST /api/follow/<user_id>/`: Follow a user.
- `POST /api/unfollow/<user_id>/`: Unfollow a user.
- `GET /api/feed/`: View posts from users you follow.

### Likes & Notifications
- `POST /api/posts/<pk>/like/`: Like a post.
- `POST /api/posts/<pk>/unlike/`: Unlike a post.
- `GET /api/notifications/`: View your notifications.

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
