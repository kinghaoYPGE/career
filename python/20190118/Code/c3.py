"""
if else表示的是逻辑判断，switch表示的是分支处理
如何让用字典代替switch语句?
switch:
    case 1:
        todo
        break
    case 2:
        todo
        break
    case 3:
        todo 
        break
    default:
        todo
"""
def do_normal():
    return 'this is normal'

def do_vip():
    return 'this is vip'

def do_svip():
    return 'this is svip'

def do_ssvip():
    return 'this is ssvip'

def do_default():
    return 'this is default'

switcher = {
    0: do_normal,
    1: do_vip,
    2: do_svip,
    3: do_ssvip
}
# ....得到当前用户身份时normal
current_level = 9

level = switcher.get(current_level, do_default)
print(level())