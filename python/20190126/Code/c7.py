"""
给线程绑定局部变量
"""
from threading import Thread, local, current_thread

# ThreadLocal: 当前线程的环境变量
local_school = local()

def process_student():
    std = local_school.student
    print('Thread %s running: Hello %s' % (current_thread().name, std))


def run_task(name):
    # 绑定学生名字到当前线程
    local_school.student = name
    process_student()


t1 = Thread(target=run_task, args=('zhangsan',), name='Thread-A')
t2 = Thread(target=run_task, args=('lisi',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
