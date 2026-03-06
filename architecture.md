# 🏗️ Notification System Architecture

User Action
   ↓
Event Producer
   ↓
Message Queue (Kafka / RabbitMQ)
   ↓
Notification Service
   ↓
Delivery Service
   ↓
Push Notification (Mobile/Web)

---

# Components

Event Producer
Creates events when actions happen.

Message Queue
Buffers events and ensures reliable processing.

Notification Service
Processes events and stores notifications.

Delivery Service
Sends notifications via:

- WebSocket
- Push notifications
- Email/SMS

---

# Scaling Strategy

• Partition queues  
• Consumer groups  
• Horizontal notification services  
• Cache recent notifications  

---

# Failure Handling

If notification service crashes:

Queue retains messages  
Consumer restarts and processes again
