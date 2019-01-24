"""
collections模块:就是对'组'数据结构的补充
"""
# tuple->namedtuple(命名元组)
from collections import *
point = (1, 2)  # 坐标点
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)  # 结构化
print('x: %s, y: %s' % (p.x, p.y))
print(isinstance(p, Point))
print(isinstance(p, tuple))

# list(线性存储:查询元素快,插入删除效率低)->deque(双向列表如 队列、栈): 首尾插入删除效率高)
dq = deque(['a', 'b', 'c', 1, 2, 3])
dq.append('x')
print(dq)
dq.appendleft('y')
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)

# dict->defaultdict(初始化一个默认值)
d_d = defaultdict(lambda: 'NIL')
d_d['a'] = 1
print(d_d['a'])
print(d_d['b'])

# dict->OrderedDict
d1 = dict([(1, 'a'), (5, 'e'), (2, 'b'), (3, 'c'), (4, 'd')])
d1[9] = '9'
print(d1.keys())  # 字典的key是无序的、不重复的、不可变的
od = OrderedDict([(1, 'a'), (5, 'e'), (2, 'b'), (3, 'c'), (4, 'd')])
print(od)

# dict->ChainMap:把一组dict串成一个ChainMap对象
cm = ChainMap({1:'1', 2: '2'}, {3: 'a', 4: 'b'})
for k, v in cm.items():
    print(k, v)

# dict->Counter(计数器): 统计字符
c = Counter('life is short, i use python!')
# str_target = 'life is short, i use python!'
c = Counter([1, 1, 2, 3, 'a', 2])
print(c)

