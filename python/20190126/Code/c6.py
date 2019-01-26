import time
from threading import Thread, Lock

# 存款
balance = 0
lock = Lock()
def change_bal(n):
    global balance
    balance += n
    balance -= n

def run_task(n):
    for i in range(100000):
        # 为了防止对个线程操作同一个变量，加锁
        lock.acquire()
        try:
            change_bal(n)
        finally:
            # 释放锁
            lock.release()

t1 = Thread(target=run_task, args=(5,))
t2 = Thread(target=run_task, args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)

