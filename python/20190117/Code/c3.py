# filter 过滤序列
list_a = [1, 2, 3, 4, 5, 6]
# r = [i for i in list_a if i%2==0]
def my_fn(x):
    return x % 2 == 0
r = filter(my_fn, list_a)
print(list(r))
list_b = ['a', 'B', None, 'C', '']
def my_fn2(x):
    return x
r = filter(my_fn2, list_b)
print(list(r))

# sorted 排序算法
# 排序的核心就是两个元素的比较大小
list_c = [1, -9, 0, 99, 8, 6]
r = sorted(list_c,key=abs, reverse=True)
list_d = ['bob', 'about', 'Zoo', 'Credit']
r = sorted(list_d, key=str.lower)
print(r)