# GraphQL Gateway

Exposes a unified GraphQL API over all services.

## Features
- Auth via JWT
- Resolvers proxy to microservices
- Uses Strawberry GraphQL

## Endpoints
- `/graphql` — interactive GraphQL playground

## Sample Query
```graphql
query {
  me {
    name
    email
    preferences
  }
  unreadNotifications {
    id
    content
  }
}
