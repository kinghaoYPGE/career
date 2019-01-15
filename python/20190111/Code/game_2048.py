"""
init: init()
    |-> game
game: game()
    |-> game
    |-> win
    |-> gameover
    |-> exit
win: lambda: not_game('win')
    |-> restart->init
    |-> exit
gameover: lambda not_game('gameover')
    |-> restart->init
    |-> exit
exit: break
"""
from collections import defaultdict
from random import choice, randrange
from itertools import product
import curses

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
target_str = 'wasdrq'
target_str += target_str.upper()
actions_dict = dict(zip([ord(ch) for ch in target_str], actions*2))

def get_user_actions(keyboard):
    """得到用户键盘输入"""
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

# 转置二维列表
def transpose(field):
    return [list(row) for row in zip(*field)]

# 逆转二维列表
def invert(field):
    return [row[::-1] for row in field]


# 创建棋盘
class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = 2048  # 过关分数
        self.score = 0  # 当前分数
        self.highscore = 0  # 最高得分
        self.reset()  # 重置棋盘

    # 重置    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

    # 初始化棋盘数字(2或4)
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        i, j = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    
    def move(self, direction):
        # 定义一行向左合并
        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row)-len(new_row))]
                return new_row
            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2*row[1])
                        self.score += 2 * row[i]
                    else:
                        if i+1 < len(row) and row[i] == row[i+1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: transpose(moves['Rigth'](transpose(field)))

        if direction in moves:
            if self.move_is_possibale(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    def draw(self, screen):
        pass

    def move_is_possibale(self, move):
        pass
            

def main(stdscr):
    game_field = GameField(win=32)

    def init():
        game_field.reset()
        return 'Game'

    def not_game(state):
        """state: win or gameover"""
        game_field.draw(stdscr)
        action = get_user_actions (stdscr) # 用户输入
        responses = defaultdict(lambda: state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action] 
    
    def game():
        game_field.draw(stdscr)
        action = get_user_actions (stdscr) # 用户输入

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    
    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'Gameover': lambda: not_game('Gameover'),
        'Game': game
    }

    curses.start_color()

    state = 'Init'

    while state != 'Exit':
        state = state_actions[state]()


curses.wrapper(main)
