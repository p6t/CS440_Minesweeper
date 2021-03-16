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

    def update_kb(self, x, y, clue):
        if DEBUG:
            print("SAFE CELL, UPDATING KNOWLEDGE BASE")
        self.revealed[x][y] = 1
        self.clues[x][y] = clue

        hiddenneighbors = get_unvisited_neighbors(self, x, y)
        bluesclues[(x,y)] = [clue,set(hiddenneighbors)]
        for (x,y) in hiddenneighbors:
            if((x,y)) in commons:
                commons[(x,y)] +=1

        #PROBABLY CALLED SOMEWHERE ELSE, LIKE THE MAIN
        self.santaclause()        


    def santaclause(bluesclues,x,y):
        value = bluesclues.values()
        for value in a_dict.values():
            print(value)

    
    