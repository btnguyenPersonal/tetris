import random

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
                        [1, 1, 1, 1],
                    ],
                    [
                        [1],
                        [1],
                        [1],
                        [1],
                    ],
                    [
                        [1, 1, 1, 1],
                    ],
                    [
                        [1],
                        [1],
                        [1],
                        [1],
                    ]
                ]
            case 'J':
                val = [
                    [
                        [2, 2, 2],
                        [0, 0, 2],
                    ],
                    [
                        [0, 2],
                        [0, 2],
                        [2, 2]
                    ],
                    [
                        [2, 0, 0],
                        [2, 2, 2],
                    ],
                    [
                        [2, 2],
                        [2, 0],
                        [2, 0]
                    ],
                ]
            case 'L':
                val = [
                    [
                        [3, 3, 3],
                        [3, 0, 0],
                    ],
                    [
                        [3, 3],
                        [0, 3],
                        [0, 3]
                    ],
                    [
                        [0, 0, 3],
                        [3, 3, 3],
                    ],
                    [
                        [3, 0],
                        [3, 0],
                        [3, 3]
                    ],
                ]
            case 'O':
                val = [
                    [
                        [4, 4],
                        [4, 4]
                    ],
                    [
                        [4, 4],
                        [4, 4]
                    ],
                    [
                        [4, 4],
                        [4, 4]
                    ],
                    [
                        [4, 4],
                        [4, 4]
                    ],
                ]
            case 'S':
                val = [
                    [
                        [0, 5, 5],
                        [5, 5, 0]
                    ],
                    [
                        [5, 0],
                        [5, 5],
                        [0, 5]
                    ],
                    [
                        [0, 5, 5],
                        [5, 5, 0]
                    ],
                    [
                        [5, 0],
                        [5, 5],
                        [0, 5]
                    ],
                ]
            case 'T':
                val = [
                    [
                        [6, 6, 6],
                        [0, 6, 0]
                    ],
                    [
                        [0, 6],
                        [6, 6],
                        [0, 6]
                    ],
                    [
                        [0, 6, 0],
                        [6, 6, 6]
                    ],
                    [
                        [6, 0],
                        [6, 6],
                        [6, 0]
                    ],
                ]
            case 'Z':
                val = [
                    [
                        [7, 7, 0],
                        [0, 7, 7]
                    ],
                    [
                        [0, 7],
                        [7, 7],
                        [7, 0]
                    ],
                    [
                        [7, 7, 0],
                        [0, 7, 7]
                    ],
                    [
                        [0, 7],
                        [7, 7],
                        [7, 0]
                    ],
                ]
        return val[self.orientation]

    def getRandomPiece(self):
        pieces = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
        return random.choice(pieces);

