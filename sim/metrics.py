class Metrics:
    def __init__(self):
        self.jobs_created = 0
        self.jobs_completed = 0
        self.failures = 0
        self.retries = 0
        self.permanent_failures = 0
        self.max_queue_depth = 0

    def record_queue_depth(self, depth):
        self.max_queue_depth = max(self.max_queue_depth, depth)

    def total_attempts(self):
        return self.jobs_completed + self.failures