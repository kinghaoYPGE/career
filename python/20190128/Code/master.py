"""
分布式进程
分布在多台机器上的进程，通过网络进行通信
"""
# master.py
from multiprocessing.managers import BaseManager
from queue import Queue
task_queue = Queue()  # 任务队列
result_queue = Queue() # 结果队列

class QueueManager(BaseManager):
    pass

# 将两个队列注册到网络上
QueueManager.register('get_task_queue', callable=lambda:task_queue)
QueueManager.register('get_result_queue', callable=lambda:result_queue)

manager = QueueManager(address=('', 8000), authkey=b'python')
manager.start()

# 放任务到task_queue
task = manager.get_task_queue()
# 为了得到worker传递过来的结果
result = manager.get_result_queue()
for i in range(10):
    print('put %s in task_queue' % i)
    task.put(i)

print('get results from result_queue')
for i in range(10):
    r = result.get(timeout=10)
    print('Result is %s' % r)

manager.shutdown()
print('master exit')




