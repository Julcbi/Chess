#     $env:Path = "C:\Users\aline\.local\bin;$env:Path"  

import itertools
class Figure:
    # Parent class attributes and methods
    def __init__(self, color):
        self.color = color

    def can_overstep():
        return false

#     $env:Path = "C:\Users\aline\.local\bin;$env:Path"   
#     $env:Path = "C:\Users\aline\.local\bin;$env:Path"   
class Pawn(Figure):
    def letter(self):
        return self.color + 'P'
   
    # Parent class attributes and methods
    def tt(self):
        print(self.color)

    @staticmethod
    def get_moves():
        return [
            [1, 0]
        ]
#     $env:Path = "C:\Users\aline\.local\bin;$env:Path" 

class King(Figure):
    def letter(self):
        return self.color + 'K'
    @staticmethod
    def get_moves():
        return [
            [1, -1],
            [0, -1],
            [0, 1],
            [1, 0],
            [-1, 0],
            [1, 1],
            [-1, -1],
            [-1, 1]
        ]
class Horse(Figure):

    def letter(self):
        return self.color + 'H'

    def can_overstep():
        return true
    @staticmethod
    def get_moves():
        return [
            [1, 2],
            [2, 1],
            [2, -1],
            [1, -2],
            [-1, -2],
            [-2, -1],
            [-2, 1],
            [-1, 2]
        ]

class Rook(Figure):
    def letter(self):
        return self.color + 'R'
    @staticmethod
    def get_moves():
        return [
            [0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
            [0, 5],
            [0, 6],
            [0, 7],
            
            [0, -1],
            [0, -2],
            [0, -3],
            [0, -4],
            [0, -5],
            [0, -6],
            [0, -7],

            [1, 0],
            [2, 0],
            [3, 0],
            [4, 0],
            [5, 0],
            [6, 0],
            [7, 0],

            [-1, 0],
            [-2, 0],
            [-3, 0],
            [-4, 0],
            [-5, 0],
            [-6, 0],
            [-7, 0]
        ]

class Bishop(Figure):
    def letter(self):
        return self.color + 'B'
    @staticmethod
    def get_moves():
        moves = []
        for i in range(1, 8):
            moves.append([i, i])
            moves.append([-i, i])
            moves.append([i, -i])
            moves.append([-i, -i])

        return moves

class Queen(Figure):

    def letter(self):
        return self.color + 'Q'

    @staticmethod
    def get_moves():        
        return Bishop.get_moves() + Rook.get_moves()
        

class ChessBoard:
    def __init__(self):
        self.board = [
            [Rook("B"), Horse("B"), Bishop("B"), King("B"), Queen("B"), Bishop("B"), Horse("B"), Rook("B")],
            [Pawn("B"), Pawn("B"), Pawn("B"), Pawn("B"), Pawn("B"), Pawn("B"), Pawn("B"), Pawn("B")],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn("W"), Pawn("W"), Pawn("W"), Pawn("W"), Pawn("W"), Pawn("W"), Pawn("W"), Pawn("W")],
            [Rook("W"), Horse("W"), Bishop("W"), Queen("W"), King("W"), Bishop("W"), Horse("W"), Rook("W")],
        ]

    def step(self, is_White, src, dst):

        sx = int(src[0]) - 1
        sy = ord(src[1]) - 97

        dx = int(dst[0]) - 1
        dy = ord(dst[1]) - 97
        
        f = self.board[sx][sy]

        if (f.color == "B" and is_White) or (f.color == "W" and not is_White):
            print("You are not using your figure")
            return False

        is_legal = False
        for move in f.get_moves():
            print(sx - dx)
            print(sy - dy)
            if f.color == "B":
                move[0] = - move[0]

            if move[0] == sx - dx and move[1] == sy - dy:
                is_legal = True

        print(is_legal)
        if not is_legal:
            return False

        self.board[dx][dy] = self.board[sx][sy]
        self.board[sx][sy] = None

        return True

    def render(self):
        print("   a  b  c  d  e  f  g  h\n")
        for (i, r) in enumerate(self.board):
            print(i + 1, end="  ")
            for f in r:
                if f == None:
                    print(end="   ")
                else:
                    # TODO: Color the output
                    print(f.letter(), end=" ")
            print()

        print("\n   a  b  c  d  e  f  g  h")



board = ChessBoard()

is_White = True 

 
while True:
    board.render()
    if is_White: 
        print("White turn")
    else:
        print("Black turn")
    src = input ("src: ")
    dst = input ("dst: ")

    while not board.step(is_White, src, dst):
        print("Wrong input, try again")
        src = input ("src: ")
        dst = input ("dst: ")

    is_White = not is_White


    