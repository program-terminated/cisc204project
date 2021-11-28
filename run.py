
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints

# list representing grid
#Q is known tiles
# - is unknown tiles
test_grid = [['-', 'Q1', '-'],
             ['Q1','Q1', '-'],
             ['-','-','-']]

def init_board(input_grid):
    # 3 x 3 board
    row = len(input_grid[0])
    col = len(input_grid)
    f = true;
    for i in range(col):
        for j in range(row):
            if test_grid[i][j] == "Q1":
                f &= ~B[i][j]
                f &= S[i][j]
                f &= Q1[i][j]
                f &= ~Q2[i][j]
                f &= ~Q3[i][j]
                f &= ~U[i][j]
   
             elif test_grid[i][j] == "Q2":
                f &= ~B[i][j]
                f &= S[i][j]
                f &= ~Q1[i][j]
                f &= ~Q3[i][j]
                f &= Q2[i][j]
                f &= ~U[i][j]
               
            elif test_grid[i][j] == "Q3":
                f &= ~B[i][j]
                f &= S[i][j]
                f &= Q3[i][j]
                f &= ~Q1[i][j]
                f &= ~Q2[i][j]
                f &= ~U[i][j]
                
            elif test_grid[i][j] == "B":
                f &= B[i][j]
                f &= ~S[i][j]
                f &= ~Q1[i][j]
                f &= ~Q2[i][j]
                f &= ~Q3[i][j]
                f &= ~U[i][j]
                
                
               
    
# Temporary example theory
def final_theory():
    E = Encoding()
    
    # Add constraints to every square in the grid
    posDict = {}

for x in range(length+1):
    for y in range(width+1):
        posDict.clear()
        if (x-1 >= 0 and y-1 >= 0):
            posDict[1] = (x-1, y-1)
        if (x-1 >= 0):
            posDict[2] = (x-1, y)
        if (x-1 >= 0 and y+1 <= width):
            posDict[3] = (x-1, y+1)
        if (y-1 >= 0):
            posDict[4] = (x, y-1)
        if (y+1 <= width):
            posDict[5] = (x, y+1)
        if (x+1 <= length and y-1 >= 0):
            posDict[6] = (x+1, y-1)
        if (x+1 <= length):
            posDict[7] = (x+1, y)
        if (x+1 <= length and y+1 <= width):
            posDict[8] = (x+1, y+1)
        for i in posDict:
            if (len(posDict) == 3):
                #make constraints
            elif (len(posDict) == 5):
                #make constraints
            elif (len(posDict) == 8):
                #make constraints
            else:
                print >> sys.stderr, "dictionary error"

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BasicPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
@proposition(E)
class FancyPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# Call your variables whatever you want
S = BasicPropositions("S")
Q1 = BasicPropositions("Q1")
Q2 = BasicPropositions("Q2")
Q3 = BasicPropositions("Q3")
B = BasicPropositions("B")
U = BasicPropositions("U")



# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    # Add custom constraints by creating formulas with the variables you created. 
    E.add_constraint((a | b) & ~x)
    # Implication
    E.add_constraint(y >> z)
    # Negate a formula
    E.add_constraint((x & y).negate())
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)

    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
