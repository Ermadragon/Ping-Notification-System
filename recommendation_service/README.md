# Recommendation Service

Generates personalized product notifications from mock activity.

## Features
- Stores mock purchase/browsing activity
- Produces Kafka messages with recommendations
- Manual trigger via API

## Endpoints
- POST `/recommendations/generate/<user_id>`: Send recommendations
- POST `/recommendations/mock`: Seed user activity
