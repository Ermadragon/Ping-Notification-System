# User Service

Handles:
- User Registration
- JWT Auth
- Preferences Management

## Setup
- SQL Server running with `userdb` created
- `pip install -r requirements.txt`
- Set environment `JWT_SECRET_KEY`

## Endpoints
- POST `/users/register`
- PUT `/users/<id>/preferences` (JWT protected)
- GET `/users/<id>` (JWT protected)
