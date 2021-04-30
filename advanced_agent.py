import itertools
import numpy as np


class AdvancedAgent:
    def __init__(self, d,n):

        self.d = d
        self.n = n
        self.score = 0
        self.firstmove = True

        self.is_mine = np.zeros((d, d))
        self.is_safe = np.zeros((d, d))
        self.revealed = np.zeros((d, d))

        #updating knowledge base per turn
        self.bluesclues = {}
        self.allVarsList = []


    # Returns (x,y) for next cell to query
    def query_next(self):
        if self.firstmove == True:
            self.firstmove = False
            return ((1,1))
        #value to initially assign
        allCondsSatisfied = False
        # all vars List contains every coordinate of a hidden square, from a clause, in a list

        allVarsList = []
        print("bluesclues in query")
        print(self.bluesclues)
        bluescluesItems = self.bluesclues.values()
        
        print("blues clues items")
        print(bluescluesItems)
        for everyVar in bluescluesItems:
            for everyCoord in everyVar[1]:
                if everyCoord not in allVarsList:
                    allVarsList.append(everyCoord)

        print("all vars list")
        print(allVarsList)
        # all vars is a list of all hidden, to allow for easier access

        truefalse = [False, True]
        repitition = len(allVarsList)
        allPossibilities = list(itertools.product(truefalse, repeat=repitition))

        answer = []
        indexCounter = 0
        while indexCounter < len(allPossibilities) and not allCondsSatisfied:

            allCondsSatisfied = True

            for key in self.bluesclues.keys():
                clueHides = self.bluesclues[key]
                if not self.passConds(allPossibilities[indexCounter],allVarsList,clueHides):
                    allCondsSatisfied = False
                    indexCounter+=1
                    break

            if allCondsSatisfied:
                answer = allPossibilities[indexCounter]

        #if you want, you can add risk analysis here
        #otherwise, this is where you return any possible assignment from the
        #inferred version answer

        indexCounter = 0
        while indexCounter<len(answer):
            if answer[indexCounter] == False:
                return allVarsList[indexCounter]
            else:
                target = random.randrange(0, self.n_hidden)
                counter = 0
                for i in range(self.d):
                    for j in range(self.d):
                        if (self.revealed[i][j] == 0):
                            if (counter == target):
                                return (i, j)
                            else:
                                counter += 1

    def update_kb(self, x, y, clue):
        print("clue")
        print(clue)
        if (clue == "mine"):
            # Hit a mine
            self.is_mine[x][y] = 1
            self.revealed[x][y] = 1
            for i in range(x - 1, x + 2):
                if (i < 0) or (i >= self.d):
                    continue
                for j in range(y - 1, y + 2):
                    if (j < 0) or (j >= self.d):
                        continue
                    if (i == x) and (j == y):
                        continue

                    if (i,j) in self.bluesclues and self.revealed[i][j] == 1:
                        if((i,j) in self.bluesclues[(i,j)][1]):
                            if len(self.bluesclues[((i,j))][1]) == 0:
                                del self.bluesclues[((i,j))]
                            self.bluesclues[((i,j))][0]-=1

        else:
            self.is_mine[x][y] = 0
            self.revealed[x][y] = 1
            answerList = self.count_adjacent(x,y)
            self.bluesclues[((x,y))] = [clue,answerList]

#            FINISH THIS, MUST USE COUNT ADJACENT (CHANGE TO RETURN TEMP ARRAYS)
#            WILL TAKE ARRAY AND ADD TO WHAT TO PUT IN BLUESCLUES
        print("blues clues in kb")
        print(self.bluesclues)
        #you have now revealed this square
        self.revealed[x][y] = 1
        #neighbors who the clue applies to
        #bluesclues is the dictionary of all clauses, with key being coordinate of clue
        # and values in bluesclues is a set of all the unvisited neighbors
        self.bluesclues = {}

        return None



    def passConds(assignments,allVarsList,cluesItem):
        counter = 0
        for cord in cluesItem[1]:
            #tempList append assignment at that index of hidden
            if assignments[allVarsList.index(cord)] == True:
                counter +=1

        if counter == cluesItem[0]:
            return True
        else:
            return False

    def count_adjacent(self, x, y):
        allHidden = []
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.d):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.d):
                    continue
                if (i == x) and (j == y):
                    continue

                if (self.revealed[i][j] == 0):
                    allHidden.append((i,j))


        return allHidden
