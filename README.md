# 🔔 Real-Time Notification System

> Day 11 – Event Driven Backend Architecture

---

# 📌 Problem Statement

Design a scalable notification system that sends real-time notifications to users.

Examples:

• Like notifications  
• Comment alerts  
• Order updates  
• System alerts  

---

# 🎯 Functional Requirements

- Send notification
- Store notification
- Deliver real-time alerts
- Mark notification as read
- Support millions of users

---

# ⚙️ Non Functional Requirements

- Low latency delivery
- High throughput
- Reliable message processing
- Fault tolerant
- Horizontal scalability

---

# 🧠 Core Concepts

✔ Event-driven architecture  
✔ Message queues  
✔ Push notifications  
✔ WebSocket delivery  
✔ Notification fan-out  

---

# 📊 High Level Flow

Event Created → Queue → Notification Service → User Devices

Example:

User likes post → Event created → Notification sent to post owner
