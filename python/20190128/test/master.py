"""
服务进程：master
"""
from multiprocessing.managers import BaseManager
from queue import Queue

def task_queue():
    task_queue = Queue()
    return task_queue

def result_queue():
    result_queue = Queue()
    return result_queue

class QueueManager(BaseManager):
    pass

if __name__ == '__main__':
    manager = QueueManager(address=('127.0.0.1', 8000), authkey=b'python')
    manager.register('get_task_queue', callable=task_queue)
    manager.register('get_result_queue', callable=result_queue)  
    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    for i in range(10):
        print('=======put task %d' % i)
        task.put(i)

    print('=======get results======')
    for i in range(10):
        r = result.get(timeout=10)
        print('=======Result %s' % r)

    manager.shutdown()
    print('server exit')
