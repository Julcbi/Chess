#     $env:Path = "C:\Users\aline\.local\bin;$env:Path"  

import itertools
class Figure:
    # Parent class attributes and methods
    def __init__(self, color):
        self.color = color

    
    def can_overstep(self):
        return False

#     $env:Path = "C:\Users\aline\.local\bin;$env:Path"   
#     $env:Path = "C:\Users\aline\.local\bin;$env:Path"   
class Pawn(Figure):
    def letter(self):
        return self.color + 'P'
   
    # Parent class attributes and methods
    #def tt(self):
    #    print(self.color)

    @staticmethod
    def get_moves():
        return [
            [1, 0],
            [2, 0],
            [1, -1],
            [1, 1] 
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

    def can_overstep(self):
        return True


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
        self.is_black_first_step = True
        self.is_white_first_step = True

    def step(self, is_White, src, dst):
        sx = int(src[0]) - 1
        sy = ord(src[1]) - 97

        dx = int(dst[0]) - 1
        dy = ord(dst[1]) - 97

        if dx > 7 or dx < 0 or dy > 7 or dy < 0:
            print("out of range")
            return False

        f = self.board[sx][sy]

        if not f or (f.color == "B" and is_White) or (f.color == "W" and not is_White):
            print("You are not using your figure")
            return False

        is_legal = False
        for move in f.get_moves():
            if not self.is_black_first_step and f.letter() == "BP" and move[0] == 2:
                continue

            if not self.is_white_first_step and f.letter() == "WP" and move[0] == 2:
                continue

            if f.color == "B":
                move[0] = -move[0]

            if move[0] == sx - dx and move[1] == sy - dy:
                if abs(move[1]) == 1 and isinstance(f, Pawn):
                    target = self.board[dx][dy]
                    if target is None or target.color == f.color:
                        continue
                is_legal = True
                break

        if f.letter() != "WH" and f.letter() != "BH":
            if sy == dy:
                if sx > dx:
                    for x in range(sx, dx, -1)[1:]:
                        if self.board[x][sy] is not None:
                            is_legal = False
                else:
                    for x in range(sx, dx)[1:]:
                        if self.board[x][sy] is not None:
                            is_legal = False

            if sx == dx:
                if sy > dy:
                    for y in range(sy, dy, -1)[1:]:
                        if self.board[sx][y] is not None:
                            is_legal = False
                else:
                    for y in range(sy, dy)[1:]:
                        if self.board[sx][y] is not None:
                            is_legal = False

            signY = 1
            signX = 1

            if sy > dy:
                signY = -1
            if sx > dx:
                signX = -1

            for y, x in zip(range(sy, dy, signY)[1:], range(sx, dx, signX)[1:]):
                print(x, y)
                if self.board[x][y] is not None:
                    is_legal = False

        print(is_legal)
        if not is_legal:
            return False

        target = self.board[dx][dy]
        if isinstance(target, King):
            print("Checkmate! The King has been captured. Game over.")
            self.board[dx][dy] = f  
            self.board[sx][sy] = None 
            self.render()
            exit(0)


        self.board[dx][dy] = self.board[sx][sy]
        self.board[sx][sy] = None

        if is_White:
            self.is_white_first_step = False
        else:
            self.is_black_first_step = False

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


    def is_king_in_check(self, is_white):
        """Verifica se o rei está sob ataque direto."""
        king_position = None
        for x, row in enumerate(self.board):
            for y, piece in enumerate(row):
                if isinstance(piece, King) and piece.color == ("W" if is_white else "B"):
                    king_position = (x, y)
                    break
            if king_position:
                break

        if king_position is None:
            return False  # Rei não encontrado no tabuleiro

        king_x, king_y = king_position

        for x, row in enumerate(self.board):
            for y, piece in enumerate(row):
                if piece and piece.color != ("W" if is_white else "B"):
                    for move in piece.get_moves():
                        move_x, move_y = move
                        if not piece.can_overstep():
                            for step in range(1, 8):
                                target_x = x + move_x * step
                                target_y = y + move_y * step
                                if 0 <= target_x < 8 and 0 <= target_y < 8:
                                    if (target_x, target_y) == (king_x, king_y):
                                        return True  # Rei está sob ataque
                                    if self.board[target_x][target_y] is not None:
                                        break
                        else:
                            target_x = x + move_x
                            target_y = y + move_y
                            if 0 <= target_x < 8 and 0 <= target_y < 8:
                                if (target_x, target_y) == (king_x, king_y):
                                    return True
        return False

    def can_defend_king(self, is_white):
        """Verifica se há alguma peça que pode defender o rei."""
        king_position = None
        for x, row in enumerate(self.board):
            for y, piece in enumerate(row):
                if isinstance(piece, King) and piece.color == ("W" if is_white else "B"):
                    king_position = (x, y)
                    break
            if king_position is None:
                return False

        king_x, king_y = king_position

        for x, row in enumerate(self.board):
            for y, piece in enumerate(row):
                if piece and piece.color == ("W" if is_white else "B"):
                    for move in piece.get_moves():
                        target_x = x + move[0]
                        target_y = y + move[1]
                        if 0 <= target_x < 8 and 0 <= target_y < 8:
                            original_piece = self.board[target_x][target_y]
                            self.board[target_x][target_y] = piece
                            self.board[x][y] = None

                            if not self.is_king_in_check(is_white):
                                # Restaura o estado original e retorna True
                                self.board[x][y] = piece
                                self.board[target_x][target_y] = original_piece
                                return True

                            # Restaura o estado original
                            self.board[x][y] = piece
                            self.board[target_x][target_y] = original_piece
        return False



board = ChessBoard()
is_White = True
while True:
    board.render()

    if board.is_king_in_check(is_White) and board.can_defend_king(is_White):
        print("Check!")

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
