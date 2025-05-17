# todo change number to be % 100 as the color, and 1-16 as which pieces should connect
import random

# 00 = nothing
# 01 = up
# 02 = down
# 03 = up down
# 04 = left
# 05 = left up
# 06 = left down
# 07 = left up down
# 08 = right
# 09 = right up
# 10 = right down
# 11 = right up down
# 12 = right left
# 13 = right left up
# 14 = right left down
# 15 = right left up down

class Piece:
    def __init__(self, row, col):
        self.piece = self.getRandomPiece()
        self.orientation = 0
        self.row = row
        self.col = col

    def turnRight(self):
        self.orientation += 1
        self.orientation %= 4

    def turnLeft(self):
        self.orientation -= 1
        if (self.orientation < 0):
            self.orientation = 3

    def getPiece(self):
        val = [];
        match self.piece:
            case 'I':
                val = [
                    [
                        [108, 112, 112, 104],
                    ],
                    [
                        [102],
                        [103],
                        [103],
                        [101],
                    ],
                    [
                        [108, 112, 112, 104],
                    ],
                    [
                        [102],
                        [103],
                        [103],
                        [101],
                    ]
                ]
            case 'J':
                val = [
                    [
                        [208, 212, 206],
                        [0, 0, 201],
                    ],
                    [
                        [0, 202],
                        [0, 203],
                        [208, 205]
                    ],
                    [
                        [202, 0, 0],
                        [209, 212, 204],
                    ],
                    [
                        [210, 204],
                        [203, 0],
                        [201, 0]
                    ],
                ]
            case 'L':
                val = [
                    [
                        [310, 312, 304],
                        [301, 0, 0],
                    ],
                    [
                        [308, 306],
                        [0, 303],
                        [0, 301]
                    ],
                    [
                        [0, 0, 302],
                        [308, 312, 305],
                    ],
                    [
                        [302, 0],
                        [303, 0],
                        [309, 304]
                    ],
                ]
            case 'O':
                val = [
                    [
                        [410, 406],
                        [409, 405]
                    ],
                    [
                        [410, 406],
                        [409, 405]
                    ],
                    [
                        [410, 406],
                        [409, 405]
                    ],
                    [
                        [410, 406],
                        [409, 405]
                    ],
                ]
            case 'S':
                val = [
                    [
                        [0, 510, 504],
                        [508, 505, 0]
                    ],
                    [
                        [502, 0],
                        [509, 506],
                        [0, 501]
                    ],
                    [
                        [0, 510, 504],
                        [508, 505, 0]
                    ],
                    [
                        [502, 0],
                        [509, 506],
                        [0, 501]
                    ],
                ]
            case 'T':
                val = [
                    [
                        [608, 614, 604],
                        [0, 601, 0]
                    ],
                    [
                        [0, 602],
                        [608, 607],
                        [0, 601]
                    ],
                    [
                        [0, 602, 0],
                        [608, 613, 604]
                    ],
                    [
                        [602, 0],
                        [611, 604],
                        [601, 0]
                    ],
                ]
            case 'Z':
                val = [
                    [
                        [708, 706, 0],
                        [0, 709, 704]
                    ],
                    [
                        [0, 702],
                        [710, 705],
                        [701, 0]
                    ],
                    [
                        [708, 706, 0],
                        [0, 709, 704]
                    ],
                    [
                        [0, 702],
                        [710, 705],
                        [701, 0]
                    ],
                ]
        return val[self.orientation]

    def getRandomPiece(self):
        pieces = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
        return random.choice(pieces);

