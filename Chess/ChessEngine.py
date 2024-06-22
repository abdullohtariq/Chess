# It will check Valid Moves And storing all the information about the current state of the game.
# And it also have a move log.

class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],]
        self.whiteToMove = True
        self.move = []
    def makeMove(self, move):
        self.board[move.startRow][move.startRow] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.move.append(move)
        self.whiteToMove = not self.whiteToMove
class move:
    ranksToRows = {
        "1": 7,
        "2": 6,
        "3": 5,
        "4": 4,
        "5": 3,
        "6": 2,
        "7": 1,
        "8": 0,
    }
    rowsToRanks = {
        v: k for k, v in ranksToRows.items()  # Cool Way of reversing a hashmap
    }
    filesToCol ={
        "h": 7,
        "g": 6,
        "f": 5,
        "e": 4,
        "d": 3,
        "c": 2,
        "b": 1,
        "a": 0,
    }
    colToFiles = {
        v: k for k, v in ranksToRows.items()  # Cool Way of reversing a hashmap
    }

    def __init__(self, startsq, endsq, board):
        self.startRow = startsq[0]
        self.startCol = startsq[1]
        self.endRow = endsq[0]
        self.endCol = endsq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    def getRankFile(self, r, c):
        return self.colToFiles[c] + self.ranksToRows[r]


