#     $env:Path = "C:\Users\aline\.local\bin;$env:Path"   
class Figure:
    # Parent class attributes and methods
    def __init__(self, color):
        self.color = color

    def can_overstep():
        return false

#     $env:Path = "C:\Users\aline\.local\bin;$env:Path"   
#     $env:Path = "C:\Users\aline\.local\bin;$env:Path"   
class Pawn(Figure):
   
    # Parent class attributes and methods
    def tt(self):
        print(self.color)

    def get_moves():
        return [
            [1, 0]
        ]
#     $env:Path = "C:\Users\aline\.local\bin;$env:Path" 

class King(Figure):

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
    def can_overstep():
        return true

    def get_moves(self):
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

    def get_moves():
        moves = []
        for i in range(1, 8):
            moves.append([i, i])
            moves.append([-i, i])
            moves.append([i, -i])
            moves.append([-i, -i])

        return moves

class Queen(Figure):

    def get_moves():
        moves = []
        moves.append(Bishop.get_moves())
        moves.append(Rook.get_moves())

        return moves
        
class Tower(Figure):
   
    # Parent class attributes and methods
    def tt(self):
        print(self.color)

class ChessBoard:
    def __init__(self):
        self.board = [
            [Rook("B"), Horse("B"), Bishop("B"), King("B")4, Queen("B"), Bishop("B"), Horse("B"), Rook("B")],
            [Pawn("B"), Pawn("B"), Pawn("B"), Pawn("B"), Pawn("B"), Pawn("B"), Pawn("B"), Pawn("B")],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn("W"), Pawn("W"), Pawn("W"), Pawn("W"), Pawn("W"), Pawn("W"), Pawn("W"), Pawn("W")],
            [Rook("W"), Horse("W"), Bishop("W"), Queen("W"), King("W"), Bishop("W"), Horse("W"), Rook("W")],
        ]

board = ChessBoard()
print(board.board)
horse = Horse("White")
bi = Bishop("White")
print(Queen.get_moves())

 
