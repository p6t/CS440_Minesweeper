import itertools

class AdvancedAgent:

    def __init__(self, d, n):
        '''
        clues dict: coordinate : number of surrounding mines 
        clause - coordinate of clue : set of clauses attached
        clues array, track what exists
        hidden array, track the unknown 
        '''

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
        '''
        self.commons = []
        self.outOfCommons = []
        self.tempassigns = {}
        self.potentialwrong = {}
        '''


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
        
        # all vars is a dictionary of all vars, to allow for easier access
        # key = coordinate, value = an index to connect to it

        allVars = {}
        indexCounter = 0
        for variable in allVarsList:
            allVars[variable] = indexCounter
            indexCounter+=1
        
        allPossibilities = [False, True]
        [list(i) for i in itertools.product(allPossibilities, repeat=len(allVarsList))]
        
        for arrayOfPotentials in allPossibilities:
            if not allCondsSatisfied:
                for everyClause in bluescluesItems:
                    #tempDict = {}
                    maxBombs = everyClause[0]
                    currentArr = everyClause[1]
                    #passes = True
                    trueCount = 0
                    for x in currentArr:
                        if arrayOfPotentials[allVars[x]] == True:
                            trueCount+=1
                    if trueCount is not maxBombs:
                        allCondsSatisfied = True
                        answer = arrayOfPotentials
            else:
                break
            
            # LAST LINE OF LOOPS
        
        if not allCondsSatisfied:
            # RETURN FAKE ANSWER OR SOMETHING ASK PETER
            return

        else:
            integerstore = 0
            for x in answer:
                if x == False:
                    return allVarsList[integerstore]
                else:
                    integerstore +=1

    

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

        
# CHECK IF ENOUGH ASSIGNS ARE POSSIBLE TO MAKE IT TRUE


    # Update KB given clue at given cell at (x,y)
    
    #COMMENTED FOR NOW, REWRITING
    #def update_kb(self, x, y, clue):
        #pass


    #KB = 
    '''

    clues dict: coordinate : number of surrounding mines 
    clause - coordinate of clue : set of clauses attached
    clues array, track what exists
    hidden array, track the unknown 

    '''
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
        for (x,y) in hiddenneighbors:
            #add or increment it in the dictionary, which will store the amount of times it occurs
            if((x,y)) in commons:
                commons[(x,y)] +=1
            else:
                commons[(x,y)] = 1

        #now that commons contains the most common terms that are mentioned, we have the most efficient
        # terms that can be checked for contradiction


        
        '''
        TO FIND A CONTRADICTION:
        1. Must have a sequence of values to choose for assignment, which allow for an eventual contradiction
        2. These values will either contradict or not contradict each other. 
        (question): 3 versions of a clause exist, and 2 of them are allowed, is it necessary to track
        3. track the email response for if subsequent contradiction applies to assignment
        '''

        '''
        santaclause will take bluesclues which will include a variety of clues that all include [count,vars]
        take commons lowest counts, keep assigning until a contradiction
        question: do you have to assign to satisfy an entire clause at once

        '''

# TESTING STARTS HERE

my_advancedagent = AdvancedAgent(8, 10)
