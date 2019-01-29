from multiprocessing.managers import BaseManager
import time

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

manager = QueueManager(address=('127.0.0.1', 8000), authkey=b'python')
# 连接master进程
manager.connect()

# 拿到task队列进行任务处理
task = manager.get_task_queue()
# 拿到result队列放入处理结果
result = manager.get_result_queue()
for i in range(10):
    n = task.get(timeout=5)
    print('run task %d * %d' % (n, n))
    r = '%d * %d = %d' % (n, n, n*n)
    time.sleep(1)
    result.put(r)

print('worker done')
