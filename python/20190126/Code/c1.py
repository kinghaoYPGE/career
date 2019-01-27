"""
多进程
fork方式:
    调用一次，会返回两次
    子进程返回的pid是0
    父进程返回的pid是子进程的id
"""
import os
print('Current Process: %s' % os.getpid())
# 新建一个子进程
pid = os.fork()
if pid == 0:
    # 子进程返回
    print('child process %s, parent Process: %s' %(os.getpid(), os.getppid()))
else:
    # 父进程返回
    print('Parent Process: %s, child process: %s' % (os.getpid(), pid))

