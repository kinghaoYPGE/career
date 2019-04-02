import redis
import time

# r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
# r.set('name', 'redis_test')
# print(dir(r))
# print(r['name'])
# print(r.get('name'))

# 连接池
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('gender', 'male')
print(r.get('gender'))
r.set('age', '18', ex=3)  # ex：秒 px: 毫秒
# print(r.get('age'))
# time.sleep(3)
# print(r.get('age'))
# print(r.set('age', '99', xx=True))  # nx:当前key不存在，则操作 xx: 当前key存在，则操作
r.mset({'k1': 'v1', 'k2': 'v2'})
print(r.mget('k1', 'k2'))
print('old: ', r.getset('age', '99'), 'new: ', r.get('age'))  # 设置新值并获取旧值


