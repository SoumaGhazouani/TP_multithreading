from multiprocessing.managers import BaseManager
from multiprocessing import Queue

test_queue = Queue()
result_queue = Queue()

class QueueManager(BaseManager):
    pass




class QueueClient:
    pass


if __name__ == "__main__":
    QueueManager.register('get_test_queue', callable=lambda:test_queue)
    QueueManager.register('get_result_queue', callable=lambda:result_queue)

    m = QueueManager(address=('127.0.0.1', 50000), authkey=b'abracadabra')
    #m.start()
    s = m.get_server()
    s.serve_forever()
