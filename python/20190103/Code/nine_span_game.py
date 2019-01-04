"""
1 创建符合数独游戏的9x9的二维列表
2 在列表中填满符合游戏规则(每一行，每一列，每一区域都包含1-9数字，且不重复)的数字
3 每一行随机抠掉一些数字，打印出来
"""
from itertools import product
import random

def check_rule(m, number, board, row, col):
    """
    如果遵循每一行，每一列，每一区域都包含1-9数字，且不重复的规则，返回真
    number: 被校验的数字
    board: 当前九宫格所有的元素(9x9的二维列表)
    row, col: 当前行数，当前列数
    """
    flag = True
    # 检查行
    if number in board[row]:
        flag = False
    
    # 检查列
    if not all([row[col] != number for row in board]):
        flag = False
    
    # 检查3x3的区域
    init_i, init_j = row - row % m, col - col % m  # 初始化一个3x3区域的元素索引
    if not all([number not in row[init_j:init_j+m] for row in board[init_i:row]]):
        flag = False
    
    return flag

def fill_in(m, n, numbers):
    """
    填满符合游戏规则(每一行，每一列，每一区域都包含1-9数字，且不重复)的数字
    """
    borad = [[0 for i in range(n)] for i in range(n)] # 初始化成一个9x9的二维列表
    # 内积 i是每一行的索引，j是每一列的索引
    for i, j in list(product(list(range(n)), repeat=2)):
        random.shuffle(numbers)  # 随机打乱list元素
        
        for x in numbers:
            if check_rule(m, x, borad, i, j):
                # 如果有符合规则的数字就开始赋值并停止，然后开始下一次的元素赋值
                borad[i][j] = x
                break
        else:
            # 如果发现没有符合规则的数字就返回None，然后重新开始
            return None
    return borad

def make_borad(m=3):
    n = m**2
    numbers = list(range(1, n+1)) # 1-9
    board = None
    while board is None:
        board = fill_in(m, n, numbers)
    return board

def print_board(borad, m=3, count=5):
    """
    每一行随机抠掉一些数字，打印出来
    """
    n = m ** 2
    numbers = list(range(n))
    borad_copy = borad.copy()
    for i, j in product(range(count), range(n)):
        x = random.choice(numbers)
        borad_copy[x][j] = None
    
    spacer = "++-----+-----+-----+-----+-----+-----+-----+-----+-----++"
    print(spacer.replace('-', '='))
    for i, line in enumerate(borad_copy):
        print("||  {}  |  {}  |  {} ||  {}  |  {}  |  {} ||  {}  |  {}  |  {}  ||"\
        .format(*[cell or ' 'for cell in line]))
        if (i+1) % 3 == 0:
            print(spacer.replace('-', '='))
        else:
            print(spacer)
    return borad_copy     
 
    

if __name__ == '__main__':
    board = make_borad()  # 创建数独二维列表
    print_board(board)  # 打印九宫格题目
    # 接受用户提供的答案，验证结果是否正确
    # 根据用户提交时间给用户打分
    # 提供官方答案供用户对比
    # 创建破解方法
    