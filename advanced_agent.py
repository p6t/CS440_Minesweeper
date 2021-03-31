class AdvancedAgent:

    def __init__(self, d, n):
        '''
        clues dict: coordinate : number of surrounding mines 
        clause - coordinate of clue : set of clauses attached
        clues array, track what exists
        hidden array, track the unknown 
        '''

        #ARBITRARY, FIX
        self.dimension = d

        #begin with hidden array
        self.hidden = []
        self.hidcount = 0
        for i  in range(self.dimension):
            for j in range(self.dimension):
                self.hidden[self.hidcount] = ((i,j)) 
            
        #updating knowledge base per turn 
        self.bluesclues = {} 
        self.commons = []
        self.outOfCommons = []
        self.tempassigns = {}
        self.potentialwrong = {}

    #example clue value: ((x,y) = [(x1,y1),(x2,y2)])

    # Returns (x,y) for next cell to query
    def query_next(self):
        

    def decide_next(self):
        #value to initially assign
        allCondsSatisfied = False
        x = 0
        while(allCondsSatisfied==False):
            self.tempassigns[self.commons[x]] = True
            self.outOfCommons.append(self.commons.pop(x))
            x+=1
            for y in self.bluesclues:
                checkVal = self.bluesclues[0] # the amount of bombs around it
                tempArr = self.bluesclues[1] # the array of unopened square coords
                trueCount = 0 #count the amount of assigns in this clause
                for z in tempArr: 
                    if(self.tempassigns.has_key(z)): #if this variable has been assigned
                        if self.tempassigns[z] == True: 
                            trueCount+=1 #one more true
                #if contradiction formed
                if trueCount > checkVal:
                    #do something
                    self.potentialwrong.extend(self.tempassigns)
                    decide_next() # MUST INCLUDE THE VARATION

                    # WORK ON THIS FIRST, MOST IMPORTANT
                    #if there is a contradiction, the current list of temp assigns contains a contradiction
                    #the next call of decide next must use potential wrong assignments to keep switching through first
                    # good idea, sort through temp assigns for most appearances?? think about this, might be least 

            if not self.commons:
                allCondsSatisfied = True
                    

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
