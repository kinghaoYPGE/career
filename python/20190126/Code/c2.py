"""
多进程
multiprocessing
"""
from multiprocessing import Process
import os
def run_job(name):
    print('Child Process %s: %s' % (name, os.getpid()))
p = Process(target=run_job, args=('child1', ))
# 开启进程
print('Current Process %s' % os.getpid())
print('Child Process start')
p.start()
p.join()
print('Child Process end')
