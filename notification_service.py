class NotificationService:

    def __init__(self):
        self.notifications = {}

    def send_notification(self, user_id, message):
        if user_id not in self.notifications:
            self.notifications[user_id] = []

        notification = {
            "message": message,
            "read": False
        }

        self.notifications[user_id].append(notification)

    def get_notifications(self, user_id):
        return self.notifications.get(user_id, [])

    def mark_as_read(self, user_id, index):
        if user_id in self.notifications:
            self.notifications[user_id][index]["read"] = True


# Demo
if __name__ == "__main__":
    service = NotificationService()

    service.send_notification("user1", "Your order has been shipped")
    service.send_notification("user1", "New comment on your post")

    print(service.get_notifications("user1"))
