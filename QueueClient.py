# QueueClient est une classe abstraite et doit récupérer les infos de QueueManager
from QueueManager import QueueManager


class QueueClient:
    def __init__(self, address="", port=50000, authkey=b"abc"):
        self.manager = QueueManager(address=(address, port), authkey=authkey)
        self.manager.connect()
        self.task_queue = self.manager.get_task_queue()
        self.result_queue = self.manager.get_result_queue()

    def get_results(self):
        return self.result_queue.get()
