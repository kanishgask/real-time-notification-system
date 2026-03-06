# 📊 ER Diagram – Notification System

USERS
- user_id (PK)
- name

NOTIFICATIONS
- notification_id (PK)
- user_id (FK)
- message
- is_read

Relationship:

User 1 → N Notifications
