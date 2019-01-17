"""
会员系统：
等级
    NORMAL = 'A'
    VIP = 'B'
    SVIP = 3
    SSVIP = 4
class Level(object):
    NORMAL = 1
    VIP = 2
    SVIP = 3
    SSVIP = 4
"""
from enum import Enum, unique, IntEnum
# Level = Enum('Level', ('NORMAL', 'VIP', 'SVIP', 'SSVIP'))
# print(type(Level))
# print(dir(Level))
# print(Level)
# print(Level.NORMAL)
# print(type(Level.NORMAL))
# print(dir(Level.NORMAL))
# print(Level.NORMAL.name, Level.NORMAL.value)
# for i in Level:
    # print(i.name, i.value)
# for name, member in Level.__members__.items():
    # print(name, member.value)

@unique
class Weekday(IntEnum):
    Sun = 0
    Mon = 1
    # other = 1
    Tue = 2
    Wed = 'a'
    Thu = 4
    Fri = 5
    Sat = 6
# 把一个值转换成一个枚举元素
# week = Weekday(0)
# print(week)
# print(week.name, week.value)
day1 = Weekday.Sun
# print(day1)
# week = Weekday(1)
# print(week)
# for name, member in Weekday.__members__.items():
    # print(name, member)
# Weekday.Sun = 7   枚举的值不可以更改
print(Weekday.Sun == Weekday.Mon)  # 等值比较

