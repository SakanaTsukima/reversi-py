# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import copy
import re

# 盤上の情報を格納するデータフレーム
row = [np.repeat(0, 8)]
board = pd.DataFrame(np.repeat(row, 8, axis=0))


# ターンの始まりを告げる関数
def turn_start(color):
    if color == 1:
        return print('Input 1P\'s piece ("0,0"~"7,7").')
    else:
        return print('Input 2P\'s piece ("0,0"~"7,7").')


class Reverse:
    def __init__(self):
        self.board = copy.deepcopy(board)

    def all_directions(self, color, y, x):

        def lefts():
            if x < 2:
                pass
            elif self.board[y][x - 1] == 0 or self.board[y][x - 1] == int(color):
                pass
            # 左隣のコマが白だった場合
            else:
                m = 0
                while m < x - 1:
                    # ターゲットの黒コマにぶち当たったら
                    if self.board[y][x - (m + 2)] == int(color):
                        # ターゲットと入力コマとの間の白コマを返す
                        for n in range(m + 1):
                            self.board[y][x - (n + 1)] = int(color)
                        break
                    m += 1
                return

        def rights():
            if x > 5:
                pass
            elif self.board[y][x + 1] == 0 or self.board[y][x + 1] == int(color):
                pass
            else:
                m = 0
                while m + x < 6:
                    if self.board[y][x + (m + 2)] == int(color):
                        for n in range(m + 1):
                            self.board[y][x + (n + 1)] = int(color)
                        break
                    m += 1
                return

        def tops():
            if y < 2:
                pass
            elif self.board[y - 1][x] == 0 or self.board[y - 1][x] == int(color):
                pass
            else:
                m = 0
                while m < y - 1:
                    if self.board[y - (m + 2)][x] == int(color):
                        for n in range(m + 1):
                            self.board[y - (n + 1)][x] = int(color)
                        break
                    m += 1
                return

        def bottoms():
            if y > 5:
                pass
            elif self.board[y + 1][x] == 0 or self.board[y + 1][x] == int(color):
                pass
            else:
                m = 0
                while m + y < 6:
                    if self.board[y + (m + 2)][x] == int(color):
                        for n in range(m + 1):
                            self.board[y + (n + 1)][x] = int(color)
                        break
                    m += 1
                return

        def top_lefts():
            if y < 2 or x < 2:
                pass
            elif self.board[y - 1][x - 1] == 0 or self.board[y - 1][x - 1] == int(color):
                pass
            else:
                m = 0
                while m < y - 1 and m < x - 1:
                    if self.board[y - (m + 2)][x - (m + 2)] == int(color):
                        for n in range(m + 1):
                            self.board[y - (n + 1)][x - (n + 1)] = int(color)
                        break
                    m += 1
                return

        def top_rights():
            if y < 2 or x > 5:
                pass
            elif self.board[y - 1][x + 1] == 0 or self.board[y - 1][x + 1] == int(color):
                pass
            else:
                m = 0
                while m < y - 1 and m + x < 6:
                    if self.board[y - (m + 2)][x + (m + 2)] == int(color):
                        for n in range(m + 1):
                            self.board[y - (n + 1)][x + (n + 1)] = int(color)
                        break
                    m += 1
                return

        def bottom_lefts():
            if y > 5 or x < 2:
                pass
            elif self.board[y + 1][x - 1] == 0 or self.board[y + 1][x - 1] == int(color):
                pass
            else:
                m = 0
                while m + y < 6 and m < x - 1:
                    if self.board[y + (m + 2)][x - (m + 2)] == int(color):
                        for n in range(m + 1):
                            self.board[y + (n + 1)][x - (n + 1)] = int(color)
                        break
                    m += 1
                return

        def bottom_rights():
            if y > 5 or x > 5:
                pass
            elif self.board[y + 1][x + 1] == 0 or self.board[y + 1][x + 1] == int(color):
                pass
            else:
                m = 0
                while m + y < 6 and m + x < 6:
                    if self.board[y + (m + 2)][x + (m + 2)] == int(color):
                        for n in range(m + 1):
                            self.board[y + (n + 1)][x + (n + 1)] = int(color)
                        break
                    m += 1
                return

        lefts()
        rights()
        tops()
        bottoms()
        top_lefts()
        top_rights()
        bottom_lefts()
        bottom_rights()
        return self.board


class Judgement(Reverse):
    def __init__(self):
        super().__init__()

    # パスをせざるをえない盤面であるかを確認するmethod
    def passing(self, color):
        for Y in range(8):
            for X in range(8):
                if self.board[Y][X] == 0:
                    r = Reverse()
                    if not r.all_directions(color, Y, X).equals(board):
                        return False
        return True

    # 入力されたコマの値が正しいかを判断するmethod
    def judge(self, color, y, x):
        # 盤外への入力を認めない
        if int(input_coords[0]) not in range(8) or int(input_coords[1]) not in range(8):
            return False
        # 既にコマのある位置に入れさせない
        elif self.board[y][x] != 0:
            return False

        else:
            r = Reverse()
            # コマを返せなければ受け付けない
            if r.all_directions(color, y, x).equals(board):
                return False
            # コマが１つ以上返るようであればOK
            else:
                return True

    # 盤面を更新するためのmethod
    @staticmethod
    def update(color, y_acceptable, x_acceptable):
        r = Reverse()
        return r.all_directions(color, y_acceptable, x_acceptable)


board[3][3] = -1
board[3][4] = 1
board[4][3] = 1
board[4][4] = -1

i = 1
while True:
    # どちらか一方のコマのみになった場合はゲームを終了する
    if 1 not in board.values:
        break
    if -1 not in board.values:
        break
    j = Judgement()
    # どこにも置けない場合はパスをし，相手に番が移る
    if j.passing(i):
        print('PASS')
        i = i * (-1)
        continue
    turn_start(i)

    # 1ターンの動作を行う
    while True:
        # 局面を表示し手を入力させる
        print(board)
        input_ = input()
        # 入力された手が正常でなければ再入力を求める
        if not re.fullmatch(r'\d,\d', input_):
            print('Input with a proper format like "2,5".')
        else:
            input_coords = input_.split(',')
            y_input, x_input = int(input_coords[0]), int(input_coords[1])
            # 入力された手が正常でなければ再入力を求める
            if not j.judge(i, y_input, x_input):
                print('Input to a proper section ("0,0"~"7,7").')
            # 入力された手が正常であれば盤面を更新する
            else:
                board = j.update(i, y_input, x_input)
                board[y_input][x_input] = i
                # 相手の番へ
                i = i * (-1)
                break
    # 盤面がすべて埋まったらゲームを終了する
    if 0 not in board.values:
        break

# 勝敗を表示する
result = sum(board.sum())

if result > 0:
    print('1P WIN')
elif result < 0:
    print('2P WIN')
else:
    print('DRAW')
