"""
python默认参数为可变数据(如list)时的用法
"""
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L