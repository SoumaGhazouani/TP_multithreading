from multiprocessing.managers import BaseManager
from QueueManager import QueueClient

class Boss(QueueClient): pass 

if __name__ == "__main__":
    m = Boss(address=('', 50000), authkey=b'abracadabra')

    Boss.register('get_test_queue')
    m.connect()
    queue = m.get_test_queue()
    for i in range (5):
        task = "task"
        queue.put('tas')
        
    