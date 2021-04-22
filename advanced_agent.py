import itertools

class AdvancedAgent:

    def __init__(self, d, n):

        #ARBITRARY, FIX
        self.d = d

        #begin with hidden array
        self.hidden = []
        self.hidcount = 0
        for i  in range(self.dimension):
            for j in range(self.dimension):
                self.hidden[self.hidcount] = ((i,j))

        #updating knowledge base per turn
        self.bluesclues = {}



    # Returns (x,y) for next cell to query
    def query_next(self):
        #value to initially assign
        allCondsSatisfied = False

        # all vars List contains every coordinate of a hidden square, from a clause, in a list
        allVarsList = []
        bluescluesItems = self.bluesclues.items()
        for everyVar in bluescluesItems:
            for everyCoord in everyVar[1]:
                if everyCoord not in allVarsList:
                    allVarsList.append(everyCoord)

        # all vars is a list of all hidden, to allow for easier access

        allPossibilities = [False, True]
        [list(i) for i in itertools.product(allPossibilities, repeat=len(allVarsList))]

        indexCounter = 0
        while indexCounter < len(allPossibilities) and not allCondsSatisfied:
            currentList = allPossibilities[indexCounter]

            for key in bluesclues:
                clueHides = self.bluesclues[key]
                if self.passConds(currentList,allVarsList,clueHides):
                    answer = currentList
                    allCondsSatisfied = True
                    break

            indexCounter+=1

        #if you want, you can add risk analysis here
        #otherwise, this is where you return any possible assignment from the
        #inferred version answer

        indexCounter = 0
        while indexCounter<len(answer)
            if answer[indexCounter] == True:
                return allVarsList[indexCounter]
            if indexCounter == (len(answer)-1) and answer[indexCounter] == False:
                return -1

    def passConds(self,assignments,hidden,clueHides):
        tempList = []
        counter = 0
        for item in clueHides[1]:
            #tempList append assignment at that index of hidden
            if assignments[hidden.index(item)] == True:
                counter +=1

        if counter == clueHides[0]:
            return True
        else:
            return False

    def count_adjacent(self, x, y):
        adj_any = 0
        adj_mine = 0
        adj_safe = 0
        adj_hidden = 0
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.d):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.d):
                    continue
                if (i == x) and (j == y):
                    continue
                adj_any += 1
                if (self.is_mine[i][j] == 1):
                    adj_mine += 1
                if (self.is_safe[i][j] == 1):
                    adj_safe += 1
                if (self.revealed[i][j] == 0):
                    adj_hidden += 1
        return adj_any, adj_mine, adj_safe, adj_hidden


# CHECK IF ENOUGH ASSIGNS ARE POSSIBLE TO MAKE IT True


    # Update KB given clue at given cell at (x,y)

    #COMMENTED FOR NOW, REWRITING
    #def update_kb(self, x, y, clue):
        #pass




    #ARBITRARY, FIX
    dimension = 8

    #begin with hidden array
    hidden = []
    hidcount = 0
    for i  in range(dimension):
        for j in range(dimension):
            hidden[hidcount] = ((i,j))

    #updating knowledge base per turn
    bluesclues = []
    commons = {}

    #update the kb to reflect a new clause based on the newly revelead square
    #this new additional clause can create potentially new conclusions
    #we can seek out contradictions efficiently by finding the least used variables (hidden squares)
    #to find this, we need to include the commons dictionary, which will include each clue value as a key with
    # the number of other clues that include this coordinate in their clauses

    def update_kb(self, x, y, clue):
        #you have now revealed this square
        self.revealed[x][y] = 1
        #add new square to list of clues.
        self.clues[x][y] = clue
        #neighbors who the clue applies to
        self.hiddenneighbors = self.get_unvisited_neighbors(self, x, y)
        #bluesclues is the dictionary of all clauses, with key being coordinate of clue
        # and values in bluesclues is a set of all the unvisited neighbors
        self.bluesclues[(x,y)] = [clue,set(hiddenneighbors)]
        #for every set of coordinates in the hidden neighbors of this clue



# TESTING STARTS HERE



        #clues dict: coordinate : number of surrounding mines
        #clause - coordinate of clue : set of clauses attached
        #clues array, track what exists
        #hidden array, track the unknown


        #self.commons = []
        #self.outOfCommons = []
        #self.tempassigns = {}
        #self.potentialwrong = {}


my_advancedagent = AdvancedAgent(8, 10)
