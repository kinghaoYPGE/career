"""
1 创建符合数独游戏的9x9的二维列表
2 在列表中填满符合游戏规则(每一行，每一列，每一区域都包含1-9数字，且不重复)的数字
3 抠掉一些数字，打印出来
"""
from itertools import product
import random

def check_rule(number, board, row, col, init_i, init_j):
    """
    如果遵循每一行，每一列，每一区域都包含1-9数字，且不重复的规则
    返回真
    """
    flag = True
    # 检查行
    if number in board[row]:
        flag = False
    
    # 检查列
    if not all([row[col] != number for row in board]):
        flag = False
    
    # 检查3x3的区域
    if not all([number not in row[init_j:init_j+3] for row in board[init_i:row]]):
        flag = False
    
    return flag

def fill_in(numbers):
    """
    填满符合游戏规则(每一行，每一列，每一区域都包含1-9数字，且不重复)的数字
    """
    borad = [[0 for i in range(9)] for i in range(9)] # 初始化成一个9x9的二维列表
    # 内积
    for i, j in list(product(list(range(9)), repeat=2)):
        # i, j ==> row, cloumn
        random.shuffle(numbers)  # 随机打乱list元素
        i0, j0 = i - i % 3, j - j % 3
        for x in numbers:
            if check_rule(x, borad, i, j, i0, j0):
                borad[i][j] = x
                break
        else:
            return None
    return borad

def make_borad():
    numbers = list(range(1, 10)) # 1-9
    board = None
    while board is None:
        board = fill_in(numbers)
    return board

def print_board(borad):
    pass

if __name__ == '__main__':
    board = make_borad()  # 创建数独二维列表
    print(board)
     # print_board(board)  # 打印九宫格