from bauhaus import Encoding, proposition
from bauhaus.utils import count_solutions
from nnf import Var
from nnf import NNF, true, false
from nnf.operators import iff

E = Encoding()

# Class declaration that nstantiates the proposition type "Var"
@proposition(E)
class Var:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


def implication(l, r):
    return l.negate() | r


def neg(f):
    return f.negate()


# Prints the initial board setup
def show_board(board):
    for i in range(3):
        print(" | ", end="")
        for j in range(3):
            if board[i][j] == u:
                print(" u ", end="")
            elif board[i][j] == q1:
                print(" q1", end="")
            else:
                print(" o ", end="")
            print(" | ", end="")
        print()
    return


NNF.__rshift__ = implication
NNF.__invert__ = neg

# The board position: b = Black, w = White, o = empty **These variables are overwritten after the board is printed
# The "board" array below can be changed to modify the given board when debugging
q1 = 'q1'
u = 'u'
board = [
    [u, u, u],
    [u, u, u],
    [q1, q1, q1]
]

# Shows board
print("     Board")
print(" -------------")
show_board(board)
print(" -------------\n")

"""These are all 2D arrays of propositional variables.  Please note that we use a (y, x) coordinate system.
s[y][x]: denotes that there is a safe at the given square
b[y][x]: denotes that there is a bomb at the given square
q1[y][x]: denotes that a 1 tile at the given square can capture to the left
u[y][x]: denotes that an unknown at the given square can move forwards
"""
b = [
    [Var("b00"), Var('b01'), Var('b02')],
    [Var('b10'), Var('b11'), Var('b12')],
    [Var('b20'), Var('b21'), Var('b22')]]

s = [
    [Var('s00'), Var('s01'), Var('s02')],
    [Var('s10'), Var('s11'), Var('s12')],
    [Var('s20'), Var('s21'), Var('s22')]]

q1 = [
    [Var('q100'), Var('q101'), Var('q102')],
    [Var('q110'), Var('q111'), Var('q112')],
    [Var('q120'), Var('q121'), Var('q122')]]

u = [
    [Var('u00'), Var('u01'), Var('u02')],
    [Var('u10'), Var('u11'), Var('u12')],
    [Var('u20'), Var('u21'), Var('u22')]]

# Initializes the board by iterating through each position on the board 
# and assigning the appropriate proposition to the current tile.
def board_to_constraint(E):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == 'u'):
                E.add_constraint(u[i][j])
                E.add_constraint(~b[i][j])
                E.add_constraint(~s[i][j])
                E.add_constraint(~q1[i][j])
            elif (board[i][j] == 'b'):
                E.add_constraint(b[i][j])
                E.add_constraint(~u[i][j])
                E.add_constraint(~s[i][j])
                E.add_constraint(~q1[i][j])
            elif (board[i][j] == 's'):
                E.add_constraint(~b[i][j])
                E.add_constraint(~u[i][j])
                E.add_constraint(s[i][j])
                E.add_constraint(~q1[i][j])
            elif (board[i][j] == 'q1'):
                E.add_constraint(~b[i][j])
                E.add_constraint(~u[i][j])
                E.add_constraint(~s[i][j])
                E.add_constraint(q1[i][j])


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
"""This theory finds the possible moves
"""


def final_theory():
    board_to_constraint(E)

    # Add constraints to every square in the grid
    posDict = []
    row = 3
    col = 3
    # Assigning values to each of the squares other than our reference square (x, y). We give the other squares
    # values for when we need to check them when checking the perimeter of a Square.
    for x in range(row):
        for y in range(col):
            posDict.clear()
            E.add_constraint(~b[x][y] >> s[x][y])
            E.add_constraint(~s[x][y] >> b[x][y])
            if (x - 1 >= 0 and y - 1 >= 0):
                posDict.append([x - 1, y - 1])
            if (x - 1 >= 0):
                posDict.append([x - 1, y])
            if (x - 1 >= 0 and y + 1 < col):
                posDict.append([x - 1, y + 1])
            if (y - 1 >= 0):
                posDict.append([x, y - 1])
            if (y + 1 < col):
                posDict.append([x, y + 1])
            if (x + 1 < row and y - 1 >= 0):
                posDict.append([x + 1, y - 1])
            if (x + 1 < row):
                posDict.append([x + 1, y])
            if (x + 1 < row and y + 1 < col):
                posDict.append([x + 1, y + 1])

            # We make different constraints based on where our reference square is on the board
            for i in range(len(posDict)):
                # If the length of the dictionary is 3, it means our reference square is in the corner of the board.
                if len(posDict) == 3:
                    E.add_constraint((q1[x][y] & b[posDict[i][0]][posDict[i][1]]) >>
                                     (s[posDict[(i + 1) % 3][0]][posDict[(i + 1) % 3][1]]) &
                                     s[posDict[(i + 2) % 3][0]][posDict[(i + 2) % 3][1]])
                    E.add_constraint((q1[x][y] & s[posDict[i][0]][posDict[i][1]] &
                                      s[posDict[(i + 1) % 3][0]][posDict[(i + 1) % 3][1]] >>
                                      b[posDict[(i + 2) % 3][0]][posDict[(i + 2) % 3][1]]))
                # If the length of the dictionary is 5, the reference square is along the outer perimeter of the board.
                elif (len(posDict) == 5):
                    E.add_constraint((q1[x][y] & b[posDict[i][0]][posDict[i][1]]) >>
                                     (s[posDict[(i + 1) % 5][0]][posDict[(i + 1) % 5][1]]
                                      & s[posDict[(i + 2) % 5][0]][posDict[(i + 2) % 5][1]]
                                      & s[posDict[(i + 3) % 5][0]][posDict[(i + 3) % 5][1]]
                                      & s[posDict[(i + 4) % 5][0]][posDict[(i + 4) % 5][1]]))

                    E.add_constraint((q1[x][y] & s[posDict[i][0]][posDict[i][1]] &
                                      s[posDict[(i + 1) % 5][0]][posDict[(i + 1) % 5][1]] &
                                      s[posDict[(i + 2) % 5][0]][posDict[(i + 2) % 5][1]] &
                                      s[posDict[(i + 3) % 5][0]][posDict[(i + 3) % 5][1]]) >>
                                     (b[posDict[(i + 4) % 5][0]][posDict[(i + 4) % 5][1]]))
                    # If the length of the dictionary is 8, the reference square is somewhere not along the outer
                    # perimeter of the board.
                elif (len(posDict) == 8):
                    E.add_constraint((q1[x][y] & b[posDict[i][0]][posDict[i][1]]) >>
                                     (s[posDict[(i + 1) % 8][0]][posDict[(i + 1) % 8][1]] &
                                      s[posDict[(i + 2) % 8][0]][posDict[(i + 2) % 8][1]] &
                                      s[posDict[(i + 3) % 8][0]][posDict[(i + 3) % 8][1]] &
                                      s[posDict[(i + 4) % 8][0]][posDict[(i + 4) % 8][1]] &
                                      s[posDict[(i + 5) % 8][0]][posDict[(i + 5) % 8][1]] &
                                      s[posDict[(i + 6) % 8][0]][posDict[(i + 6) % 8][1]] &
                                      s[posDict[(i + 7) % 8][0]][posDict[(i + 7) % 8][1]]))

                    E.add_constraint((q1[x][y] & s[posDict[i][0]][posDict[i][1]]
                                      & s[posDict[(i + 1) % 8][0]][posDict[(i + 1) % 8][0]]
                                      & s[posDict[(i + 2) % 8][0]][posDict[(i + 2) % 8][1]]
                                      & s[posDict[(i + 3) % 8][0]][posDict[(i + 3) % 8][1]]
                                      & s[posDict[(i + 4) % 8][0]][posDict[(i + 4) % 8][1]]
                                      & s[posDict[(i + 5) % 8][0]][posDict[(i + 5) % 8][1]]
                                      & s[posDict[(i + 6) % 8][0]][posDict[(i + 6) % 8][1]])
                                     >> b[posDict[(i + 7) % 8][0]][posDict[(i + 7) % 8][0]])
                else:
                    print("Error")
    return E


if __name__ == "__main__":
    T = final_theory()
    T = T.compile()
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())
    print("\nVariable likelihoods:")
