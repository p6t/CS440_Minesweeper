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
            return (1,1)
        #value to initially assign
        allCondsSatisfied = False
        # all vars List contains every coordinate of a hidden square, from a clause, in a list

        allVarsList = []
        bluescluesItems = self.bluesclues.values()

        for everyVar in bluescluesItems:
            for everyCoord in everyVar[1]:
                if everyCoord not in allVarsList:
                    allVarsList.append(everyCoord)


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
                save = self.passConds(allPossibilities[indexCounter],allVarsList,clueHides[0],clueHides[1])
                if not save:
                    allCondsSatisfied = False
                    indexCounter+=1
                    break

            if allCondsSatisfied:
                answer = allPossibilities[indexCounter]

        #if you want, you can add risk analysis here
        #otherwise, this is where you return any possible assignment from the
        #inferred version answer
        indexCounter = 0

        listtoremove = []

        while indexCounter<len(answer):
            if answer[indexCounter] == False:
                for key in self.bluesclues.keys():
                    if(allVarsList[indexCounter] in self.bluesclues[key][1]):
                        listtoremove.append([key,indexCounter])

                for item in listtoremove:
                    self.bluesclues[item[0]][1].remove(allVarsList[item[1]])
                    if self.bluesclues[item[0]][0] > 0:
                        self.bluesclues[item[0]][0]-=1
                    if len(self.bluesclues[item[0]][1]) == 0:
                        del self.bluesclues[item[0]]        
    
                return allVarsList[indexCounter]


            '''
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
            '''
    def update_kb(self, x, y, clue):

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
                            if self.bluesclues[(i,j)][0] > 0:
                                self.bluesclues[(i,j)][0]-=1
                            if len(self.bluesclues[(i,j)][1]) == 0 :
                                del self.bluesclues[(i,j)]                     

        else:
            self.score+=1
            self.is_mine[x][y] = 0
            self.revealed[x][y] = 1
            answerList = self.count_adjacent(x,y)
            self.bluesclues[(x,y)] = [clue,answerList]
            print(self.bluesclues)
            keysList = self.bluesclues.keys()
            for i in range(x - 1, x + 2):
                if (i < 0) or (i >= self.d):
                    continue
                for j in range(y - 1, y + 2):
                    if (j < 0) or (j >= self.d):
                        continue
                    if (i == x) and (j == y):
                        continue
                    if (i,j) in keysList and self.revealed[i][j] == 1:
                        if((i,j) in self.bluesclues[(i,j)][1]):
                            self.bluesclues[(i,j)][1].remove((i,j))

#            FINISH THIS, MUST USE COUNT ADJACENT (CHANGE TO RETURN TEMP ARRAYS)
#            WILL TAKE ARRAY AND ADD TO WHAT TO PUT IN BLUESCLUES
        #you have now revealed this square
        #neighbors who the clue applies to
        #bluesclues is the dictionary of all clauses, with key being coordinate of clue
        # and values in bluesclues is a set of all the unvisited neighbors

        return None


    def passConds(self,assignments,allVarsList,count,potential):
        counter = 0
        for cord in potential:
            #tempList append assignment at that index of hidden
            if assignments[allVarsList.index(cord)] == True:
                counter +=1
                if counter>count:
                    return False

        if counter == count:
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

    def get_score(self):
            final = (self.d**2)-self.score
            return final / self.n