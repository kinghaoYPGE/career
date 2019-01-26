"""
多线程
threading
"""
import threading, time
from threading import Thread

def loop():
    print('thread %s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s done.' % threading.current_thread().name)


print('thread %s is run...' % threading.current_thread().name)
t = Thread(target=loop, name='LoopThread')
t.start()
t.join() # 同步
print('thread %s done' % threading.current_thread().name)

