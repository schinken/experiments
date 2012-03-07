__author__ = 'schinken'

import copy

# Peg Game Solver
# description: https://en.wikipedia.org/wiki/Peg_solitaire
#
# Example Game:
#
#       1
#      2 3
#     4 5 6
#    7 8 9 a
#   b c d e f

possible_moves = [
    ('1','2','4'),('2','4','7'),('4','7','b'),('b','7','4'),('7','4','2'),('4','2','1'),
    ('1','3','6'),('3','6','a'),('6','a','f'),('f','a','6'),('a','6','3'),('6','3','1'),
    ('b','c','d'),('c','d','e'),('d','e','f'),('f','e','d'),('e','d','c'),('d','c','b'),
    ('3','5','8'),('5','8','c'),('c','8','5'),('8','5','3'),
    ('2','5','9'),('5','9','e'),('e','9','5'),('9','5','2'),
    ('7','8','9'),('8','9','a'),('a','9','8'),('9','8','7'),
    ('6','9','d'),('d','9','6'),
    ('4','8','d'),('d','8','4'),
    ('4','5','6'),('6','5','4')6
]

class PegGame:

    board = []

    def __init__(self):
        self.createBoard()

    def createBoard(self):
        # create a lowercase dictionary with values 1 to f as key
        self.board = { "%x" % x : True for x in range(1, 16) }

    def getPossibleMoveForPeg( self, peg, end=False ):

        # if end is set, we have to check for the end-position
        index = 0
        if end:
            index = 2

        peg = str(peg)
        possible = []

        # determine the possible moves for the current peg
        for move in possible_moves:
            if move[ index ] == peg and self.isMoveAvailable( move ):
                possible.append( move )

        return possible

    def getPossibleMoves(self):

        moves = []
        for move in possible_moves:
            if self.isMoveAvailable( move ):
                moves.append( move )


        return moves


    def isMoveAvailable( self, move ):

        # the start position needs a peg
        if not self.hasPeg( move[0] ):
            return False

        # the second position needs a peg, too
        if not self.hasPeg( move[1] ):
            return False

        # the last one needs
        if self.hasPeg( move[2] ):
            return False

        return True


    def hasPeg( self, pos ):
        return self.board[ pos ]

    def removePeg(self, pos):
        self.board[ pos ] = None

    def setPeg(self, pos):
        self.board[ pos ] = True

    def jump(self, move):
        self.removePeg( move[0] )
        self.removePeg( move[1] )
        self.setPeg( move[2] )

    def pegsLeft(self):
        cnt = 0

        for peg in self.board.values():
            if peg:
                cnt += 1

        return cnt


def main():
    print "Do something"

    tree = {}
    for start in ( "%x" % x for x in range(1, 16) ):

        objGame = PegGame()
        objGame.removePeg( start )

        tree[ start ] = {'subtree': {}, 'obj': objGame }

        solveRecursive( objGame, start, tree[ start ] )


    printTree(tree)

def printTree( tree, indention=0 ):

    for key, obj in tree.iteritems():
        print '   '*indention, key, ' ( left:', obj['obj'].pegsLeft(), ')'
        printTree( obj['subtree'], indention+1 )


def solveRecursive( objGame, position, tree ):

    for move in objGame.getPossibleMoves():

        objGame = copy.deepcopy(objGame)
        objGame.jump( move )

        strmove = "%s->%s" % ( move[0], move[2] )
        tree['subtree'][ strmove ] =  {'subtree': {}, 'obj': objGame }

        solveRecursive( objGame, move[0], tree['subtree'][ strmove ] )



if __name__ == "__main__":
    main()