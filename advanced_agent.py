class AdvancedAgent:

    def __init__(self, d, n):
        pass

    # Returns (x,y) for next cell to query
    def query_next(self):
        pass

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
        hiddenneighbors = get_unvisited_neighbors(self, x, y)
        #bluesclues is the dictionary of all clauses, with key being coordinate of clue
        # and values in bluesclues is a set of all the unvisited neighbors
        bluesclues[(x,y)] = [clue,set(hiddenneighbors)]
        #for every set of coordinates in the hidden neighbors of this clue
        for (x,y) in hiddenneighbors:
            #add or increment it in the dictionary, which will store the amount of times it occurs
            if((x,y)) in commons:
                commons[(x,y)] +=1
            else:
                commons[(x,y)] = 1

        #now that commons contains the most common terms that are mentioned, we have the most efficient
        # terms that can be checked for contradiction



        #PROBABLY CALLED SOMEWHERE ELSE, LIKE THE MAIN
        self.santaclause(bluesclues)        


    def santaclause(bluesclues):
        value = bluesclues.values()
        for value in bluesclues.values():
            if(value[1])

        
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