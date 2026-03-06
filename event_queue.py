from queue import Queue

class EventQueue:

    def __init__(self):
        self.queue = Queue()

    def publish_event(self, event):
        self.queue.put(event)

    def consume_event(self):
        if not self.queue.empty():
            return self.queue.get()


# Demo
if __name__ == "__main__":
    q = EventQueue()

    q.publish_event({"user": "u1", "msg": "New login detected"})
    print(q.consume_event())
