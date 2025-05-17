import copy
import time
from tkinter import *
from piece import Piece

root = Tk()
root.title("Tetris")
canvas = Canvas(root, width=550, height=820)
canvas.pack()

class GameGrid:
    def __init__(self, rows, cols, pixel_width):
        self.gameOver = False
        self.rows = rows
        self.cols = cols
        self.pixel_width = pixel_width
        self.grid = []
        self.level = 0
        self.lines = 0
        self.next_piece = Piece(0, 4)
        for i in range(self.rows):
            self.grid.append([0] * cols)
        self.resetDefaultPieceState()

    def getLevelColor(self):
        match self.level % 9:
            case 0:
                return 'white'
            case 1:
                return 'red'
            case 2:
                return 'olive'
            case 3:
                return 'blue'
            case 4:
                return 'orange'
            case 5:
                return 'magenta'
            case 6:
                return 'lime'
            case 7:
                return 'cyan'
            case 7:
                return 'purple'
            case 8:
                return 'green'

    def resetDefaultPieceState(self):
        self.piece = self.next_piece
        self.next_piece = Piece(0, 4)

    def isValidState(self):
        renderGrid = copy.deepcopy(self.grid)
        piece = self.piece.getPiece()
        for i in range(len(piece)):
            for j in range(len(piece[i])):
                try:
                    if renderGrid[i + self.piece.row][j + self.piece.col] != 0 and piece[i][j] != 0:
                        return False
                except IndexError:
                    return False
        return True

    def placePiece(self):
        piece = self.piece.getPiece()
        for i in range(len(piece)):
            for j in range(len(piece[i])):
                if piece[i][j] != 0:
                    self.grid[i + self.piece.row][j + self.piece.col] = (99 * 100) + (piece[i][j] % 100)
        self.collectLines()

    def collectLines(self):
        for i in range(len(self.grid)):
            if all(int(x / 100) == 99 for x in self.grid[i]):
                self.lines += 1
                if self.lines >= (self.level + 1) * 30:
                    self.level += 1
                del self.grid[i]
                self.grid.insert(0, [0] * 10)

    def dropPiece(self):
        self.piece.row += 1
        if self.isValidState():
            return;
        else:
            self.piece.row -= 1
            self.placePiece()
            self.resetDefaultPieceState()
        if not self.isValidState():
            self.gameOver = True

    def down(self, event):
        self.dropPiece()
        self.renderGrid()

    def turnRight(self, event):
        self.piece.turnRight()
        if not self.isValidState():
            self.piece.turnLeft()
        self.renderGrid()

    def turnLeft(self, event):
        self.piece.turnLeft()
        if not self.isValidState():
            self.piece.turnRight()
        self.renderGrid()

    def right(self, event):
        self.piece.col += 1
        if not self.isValidState():
            self.piece.col -= 1
        self.renderGrid()

    def left(self, event):
        if self.piece.col > 0:
            self.piece.col -= 1
            if not self.isValidState():
                self.piece.col += 1
        self.renderGrid()

    def getWaitTime(self):
        frames = [33, 28, 24, 20, 17, 14, 11, 9, 7, 6, 5.5, 5, 4.5, 4, 3.75, 3.5, 3.25, 3]
        return int(16.67 * frames[self.level])

    def getColor(self, num):
        match int(num / 100):
            case 0:
                return 'black'
            case 1:
                return 'red'
            case 2:
                return 'orange'
            case 3:
                return 'magenta'
            case 4:
                return 'blue'
            case 5:
                return 'lime'
            case 6:
                return 'saddlebrown'
            case 7:
                return 'cyan'
            case 99:
                return self.getLevelColor()

    ## TODO fix these
    def isTopConnection(self, renderGrid, i, j):
        try:
            return (renderGrid[i][j] % 100) % 2 == 1 and ((renderGrid[i - 1][j] % 100) >> 1) % 2 == 1
        except IndexError:
            return False

    def isLeftConnection(self, renderGrid, i, j):
        try:
            return ((renderGrid[i][j] % 100) >> 2) % 2 == 1 and ((renderGrid[i][j - 1] % 100) >> 3) % 2 == 1
        except IndexError:
            return False

    def isBottomConnection(self, renderGrid, i, j):
        try:
            return ((renderGrid[i][j] % 100) >> 1) % 2 == 1 and (renderGrid[i + 1][j] % 100) % 2 == 1
        except IndexError:
            return False

    def isRightConnection(self, renderGrid, i, j):
        try:
            return ((renderGrid[i][j] % 100) >> 3) % 2 == 1 and ((renderGrid[i][j + 1] % 100) >> 2) % 2 == 1
        except IndexError:
            return False

    def renderGrid(self):
        canvas.delete("all")
        if self.gameOver:
            print("LINES: " + str(self.lines))
            print("LEVEL: " + str(self.level))
            quit()
        renderGrid = copy.deepcopy(self.grid)
        piece = self.piece.getPiece()
        for i in range(len(piece)):
            for j in range(len(piece[i])):
                try:
                    if piece[i][j] != 0:
                        renderGrid[i + self.piece.row][j + self.piece.col] = piece[i][j]
                except IndexError:
                    pass

        for i in range(len(renderGrid)):
            for j in range(len(renderGrid[i])):
                y = self.rows
                x = self.cols
                rect_id = canvas.create_rectangle(x, y, x+self.pixel_width, y+self.pixel_width, fill=self.getColor(renderGrid[i][j]), outline = "")
                borders = []
                if not renderGrid[i][j] == 0:
                    border_width = 3
                    if not self.isTopConnection(renderGrid, i, j):
                        borders.append(canvas.create_rectangle(x - border_width, y, x + self.pixel_width, y - border_width, fill='black', outline = ""))
                    if not self.isLeftConnection(renderGrid, i, j):
                        borders.append(canvas.create_rectangle(x, y, x - border_width, y + self.pixel_width, fill='black', outline = ""))
                    if not self.isBottomConnection(renderGrid, i, j):
                        borders.append(canvas.create_rectangle(x - border_width, y + self.pixel_width - border_width, x + self.pixel_width, y + self.pixel_width, fill='black', outline = ""))
                    if not self.isRightConnection(renderGrid, i, j):
                        borders.append(canvas.create_rectangle(x + self.pixel_width - border_width, y, x + self.pixel_width, y + self.pixel_width, fill='black', outline = ""))
                canvas.move(rect_id, self.pixel_width * j, self.pixel_width * i)
                for border in borders:
                    canvas.move(border, self.pixel_width * j, self.pixel_width * i)

        next_piece = self.next_piece.getPiece()
        for i in range(len(next_piece)):
            for j in range(len(next_piece[i])):
                if next_piece[i][j] != 0:
                    x = self.pixel_width * 11
                    y = self.pixel_width * 2
                    border_width = 3
                    borders = []
                    rect_id = canvas.create_rectangle(x, y, x+self.pixel_width, y+self.pixel_width, fill=self.getColor(next_piece[i][j]), outline = "")
                    if not self.isTopConnection(next_piece, i, j):
                        borders.append(canvas.create_rectangle(x - border_width, y, x + self.pixel_width, y - border_width, fill='black', outline = ""))
                    if not self.isLeftConnection(next_piece, i, j):
                        borders.append(canvas.create_rectangle(x, y, x - border_width, y + self.pixel_width, fill='black', outline = ""))
                    if not self.isBottomConnection(next_piece, i, j):
                        borders.append(canvas.create_rectangle(x - border_width, y + self.pixel_width - border_width, x + self.pixel_width, y + self.pixel_width, fill='black', outline = ""))
                    if not self.isRightConnection(next_piece, i, j):
                        borders.append(canvas.create_rectangle(x + self.pixel_width - border_width, y, x + self.pixel_width, y + self.pixel_width, fill='black', outline = ""))
                    canvas.move(rect_id, self.pixel_width * j, self.pixel_width * i)
                    for border in borders:
                        canvas.move(border, self.pixel_width * j, self.pixel_width * i)
        canvas.create_text(self.pixel_width * 12, self.pixel_width * 1, text="NEXT", font=("Arial", 20))
        canvas.create_text(self.pixel_width * 13, self.pixel_width * 6, text="LINES: " + str(self.lines), font=("Arial", 20))
        canvas.create_text(self.pixel_width * 13, self.pixel_width * 7, text="LEVEL: " + str(self.level), font=("Arial", 20))

grid = GameGrid(22, 10, 30)
root.bind("a", grid.left)
root.bind("s", grid.down)
root.bind("d", grid.right)
root.bind("j", grid.turnLeft)
root.bind("k", grid.turnRight)

def game_loop():
    grid.dropPiece()
    grid.renderGrid()
    root.after(grid.getWaitTime(), game_loop)

game_loop()
root.mainloop()
