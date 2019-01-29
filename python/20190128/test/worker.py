"""
处理任务进程
"""
from multiprocessing.managers import BaseManager
import time

class WorkerManager(BaseManager):
    pass

WorkerManager.register('get_task_queue')
WorkerManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('=====connecting master %s...=====' % server_addr)
manager = WorkerManager(address=(server_addr, 8000), authkey=b'python')
manager.connect()
task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = task.get(timeout=1)
    # 处理任务
    print('====process task %d * %d' %(n, n))
    r = '%d * %d = %d' % (n, n, n*n)
    time.sleep(1)
    result.put(r)
print('=====workder done.=====')
