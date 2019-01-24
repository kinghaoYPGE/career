"""
python常用内建模块
batteries included
"""
# 日期、时间处理 datetime
from datetime import datetime
# 获取当前时间
now = datetime.now()
# print(type(now))
# print(dir(now))
# print(now)
# 获取指定时间
dt = datetime(2018, 1, 1, 12)
print(dt)
import time
# 时间戳: 1970年1月1号 00:00:00 到当前时间的秒数 如:1548332070(秒).9364579(毫秒*1000=秒)
ts = time.time()
print(ts)
# datetime转换成timestamp
ts2 = dt.timestamp()
print(ts2)
# timestamp转换成datetime
now = datetime.fromtimestamp(ts)
print(now)
# str转换成datetime
sdate = datetime.strptime('2019-01-01 20:20:59', '%Y-%m-%d %H:%M:%S')
print(sdate)
# datetime转换成str
date_str = datetime.now().strftime('%Y年%m月%d日 %H时%M分%S秒')
print(date_str)

# datetime运算
now = datetime.now()
print('now:', now)
from datetime import timedelta
now += timedelta(days=1)  # 明天
print('now+1:', now)
now += timedelta(days=1, hours=2)
print('now+2days+2hours:', now)
now -= timedelta(weeks=1)
print('now-1week:', now)


