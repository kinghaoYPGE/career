"""
进程池创建进程
"""
from multiprocessing import Pool
import os, time, random
print('Parent process %s' % os.getpid())
def long_time_task(name):
    print('Run task %s: %s' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*5)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, (end-start)))
# 创建进程池
p = Pool(4)
for i in range(8):
    p.apply_async(long_time_task, args=('child process'+str(i),))

p.close()
p.join()

