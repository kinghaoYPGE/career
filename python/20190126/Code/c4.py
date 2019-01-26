"""
进程间通信: 队列方式
"""
from multiprocessing import Process, Queue
import os, time, random

def write_job(q):
    print('Process to write: %s' % os.getpid())
    for value in 'PYTHON':
        print('put %s to queue' % value)
        q.put(value)
        time.sleep(random.random()*5)

def read_job(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get()
        print('get %s froom queue' % value)

# 父进程创建队列对象，传给子进程
print('Parent process %s' % os.getpid())
q = Queue()
p1 = Process(target=write_job, args=(q,))
p2 = Process(target=read_job, args=(q,))
p1.start()
p2.start()
p1.join()
p2.terminate()
