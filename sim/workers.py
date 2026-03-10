import random


class WorkerPool:
    def __init__(self, failure_chance=0.2):
        self.failure_chance = failure_chance

    def process(self, job):
        failed = random.random() < self.failure_chance
        return not failed