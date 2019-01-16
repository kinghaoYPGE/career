import re
s = 'python'
r = re.findall(r'\w{2}', s)
s2 = 'asdfa  asdf    *&^%--_sadf13;ksf\n'
# .代表任意字符, 默认排除\n
r = re.findall(r'.+', s2, flags=re.S)
s3 = 'python'
# r = re.findall('p\w*n', s3)
s4 = 'py2'
r = re.findall(r'\w\w\d', s4)
s5 = 'abcadcaec'
r = re.findall(r'a(b|d|e)c', s5)

# 正则替换
s6 = 'padf134afsd329139 1213 9dasf'
s7 = '12'
def sub_fn(x):
    # print(type(x))
    # print(dir(x))
    # print(x)
    num = int(x.group(0))
    if num <= 1:
        return '0'
    else:
        return '9'
r = re.sub('\d', sub_fn, s6, count=0)

# 正则切分
s8 = 'abc s d f  a'
r = re.split('\s+', s8)
s9 = 'a,b,,c  d'
r = re.split(r'[\s,]+', s9)
# print(''.join(r))

# 正则匹配
s10 = 'pyt8hon'
r = re.match('p', s10).group(0)
r = re.search('\d', s10).group(0)

# group分组
s11 = 'life is short, i use python, i love python'
r = re.match('life(.*)python(.*)python', s11)
# r = r.group(0)
# r = r.group(0, 1, 2)
# r = r.groups()
r = re.findall('life(.*)python(.*)python', s11)

# 预编译
s12 = 'asdf232fasdf123'
reg_str = re.compile(r'\d')
r = re.findall(reg_str, s12)
print(r)
