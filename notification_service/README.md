# Notification Service

Manages storage and tracking of notifications.

## Features
- Kafka consumer on topic `notifications`
- Stores new messages in SQL Server
- Mark notifications as read
- Fetch unread messages per user

## Setup
- Connects to SQL Server (`notificationdb`)
- Requires Kafka bootstrap server
