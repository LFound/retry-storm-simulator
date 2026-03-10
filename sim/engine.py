import random
from sim.job import Job
from sim.queue_manager import QueueManager
from sim.metrics import Metrics
from sim.workers import WorkerPool


class Simulation:
    def __init__(self, total_jobs=50, failure_chance=0.2, seed=42):
        random.seed(seed)
        self.total_jobs = total_jobs
        self.queue = QueueManager()
        self.metrics = Metrics()
        self.workers = WorkerPool(failure_chance=failure_chance)

    def run(self):
        # Create initial jobs
        for i in range(self.total_jobs):
            duration = random.randint(1, 5)
            job = Job(job_id=i, duration=duration)
            self.queue.add_job(job)
            self.metrics.jobs_created += 1

        # Process until queue empty
        while self.queue.size() > 0:
            self.metrics.record_queue_depth(self.queue.size())

            job = self.queue.get_job()
            success = self.workers.process(job)

            if success:
                self.metrics.jobs_completed += 1
            else:
                self.metrics.failures += 1
                if job.can_retry():
                    job.record_retry()
                    self.queue.add_job(job)
                    self.metrics.retries += 1
                else:
                    self.metrics.permanent_failures += 1

        return {
            "jobs_created": self.metrics.jobs_created,
            "jobs_completed": self.metrics.jobs_completed,
            "failures": self.metrics.failures,
            "retries": self.metrics.retries,
            "permanent_failures": self.metrics.permanent_failures,
            "max_queue_depth": self.metrics.max_queue_depth,
            "total_attempts": self.metrics.total_attempts(),
        }