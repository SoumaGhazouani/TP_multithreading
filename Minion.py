from multiprocessing.managers import BaseManager
from QueueManager import QueueClient


class Minion(QueueClient): pass


if __name__ == "__main__":
    Minion.register('get_test_queue')

    m = Minion(address=('127.0.0.1', 50000), authkey=b'abracadabra')

    m.connect()

    queue = m.get_test_queue()

    queue.get()
    