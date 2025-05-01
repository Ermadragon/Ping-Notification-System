# Ping-Notification-System

## Architecture Overview

This system is a **Flask-based microservices architecture** built to deliver **personalized notifications** on an e-commerce platform.

### Microservices

| Service | Port | Role |
|--------|------|------|
| User Service | 5001 | User CRUD + JWT |
| Notification Service | 5002 | Stores & manages notifications |
| Recommendation Service | 5003 | Generates and publishes recommendations |
| GraphQL Gateway | 5000 | Unified API layer |

### Infrastructure

-  **Docker Compose** for orchestration
-  **SQL Server** per service (3 total)
-  **Apache Kafka** for pub/sub communication
-  **JWT Auth** via User Service

### Communication

| Producer | Topic | Consumer |
|----------|-------|----------|
| Recommendation Service | `notifications` | Notification Service |

---

## Getting Started

### Prerequisites
- Docker + Docker Compose
- Port 5000–5003 + 1433–1435 free

### Build & Run
```bash
docker-compose up --build
