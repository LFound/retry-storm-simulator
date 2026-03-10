class Job:
    def __init__(self, job_id, duration, max_retries=2):
        self.job_id = job_id
        self.duration = duration
        self.retries = 0
        self.max_retries = max_retries

    def can_retry(self):
        return self.retries < self.max_retries

    def record_retry(self):
        self.retries += 1