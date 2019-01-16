"""
正则表达式: 特殊的字符序列，可以按照一定规则操作(提取、替换)字符串
"""
import re
s = 'life 1is 0short, 2i u3se python!'
# 普通字符
# r = re.findall('python', s) 
# new_str = ''
# for i in s:
    # try:
        # new_str += str(int(i))
    # except:
        # pass
# print(new_str)
# 元字符
# \d: 提取数字，\D: 提取非数字
r = re.findall('\D', s)
print(''.join(r))
# 字符集
s2 = 'abxefcd1234'
# 字符集定界
r = re.findall('b[^cd]e', s2)
s3 = 'abcdefg'
r = re.findall('[a-g]', s3)
r = re.findall('[0-9]', s)
# 概括字符集
# r = re.findall('\d', s3) 
s4 = 'fie1^%$*s2dfjc ad3sf  sfd  as     d_)'
r = re.findall('[^A-Za-z0-9_]', s4)
# \w: 数字和字母, \W: 非数字和字母
r = re.findall('\w', s4)
s5 = """
    asdf  sdfa
    """
# \s: 空白字符，\S: 非空白字符
r = re.findall('\S', s5)
s6 = 'abcdabcdef123pythonasd'
# 数量词(默认是贪婪匹配)
r = re.findall(r'[a-d]{2,4}?', s6)
s7 = 'pythonnnnnnnn'
# 概括数量词
# *: 0次或多次，+: 1次或多次，?: 0次或1次
r = re.findall('python?', s7)
s8 = '123123123'
# 判断字符是不是4-8位数字
# 边界匹配
r = re.findall('^\d{4,8}$', s8)
print(r)


