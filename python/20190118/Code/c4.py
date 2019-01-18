"""
列表推导式
"""
list_a = [1, 2, 3, 4, 5]
#列表推导
r = [i**2 for i in list_a]
list_b = list(range(1, 11))
r = [i for i in list_b if i%2==0]
#集合推导
set_a = {1, 2, 3, 4, 5}
r = {i**2 for i in list_a}
#字典推导
dic_a = {1:'a', 2:'b', 3:'c'}
r = {v:k for k, v in dic_a.items()}
r = [str(k)+v for k, v in dic_a.items()]
#嵌套推导
list_c = [1, 2, 3, 4, 5]
r = [j+10 for j in [i**2 for i in list_c]]
print(r)