from collections import deque


class QueueManager:
    def __init__(self):
        self.queue = deque()

    def add_job(self, job):
        self.queue.append(job)

    def get_job(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def size(self):
        return len(self.queue)