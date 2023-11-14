from business import *
from BFS import BFS

class Puzzle:
    #constructor takes in the starting state
    #default algortithm is BFS, unless set otherwise (DFS, A*, UCS, Hill Climbing, ...)
    #max_total_moves and max_moves_per_line is set to -1 by default, means there's no constrain
    def __init__(self, start_state, dots_list, size, algorithm='BFS',max_total_moves=-1, max_moves_per_line=-1):
        self.start_state = start_state
        self.dots_list = dots_list
        self.size = size
        self.selectedAlgorithm = algorithm
        self.max_total_moves = max_total_moves
        self.max_moves_per_line = max_moves_per_line
        self.solution = list
        self.isSolved = False
    
    @staticmethod
    #try all possible moves for a dots pair that aren't connected
    #when a dots pair is connected, set the index of the dots pair in dotsConnectedState to true
    def getPossibleStates(state, dots_list, dotsConnectedState):
        #get the first index that it equals to False in dotsConnectedState
        #the index is -1 (doesn't chang) if all elements in the list are True
        dotPairIndex = -1
        for i in range(len(dotsConnectedState)):
            if dotsConnectedState[i] == False:
                dotPairIndex = i
                break
        
        if dotPairIndex == -1:
            return
        
        dotsPair = dots_list[dotPairIndex]

        possibleStates = list
        #traverse to the end of the line
        #check if it can go left, right, up, or down
        #add these possible_newStates in the list after moving
        #return the possibleStates list
        

    
    
    def BFS_solve(self):
        solver = BFS(self.start_state, self.dots_list, self.size)
        self.isSolved, self.solution = solver.solve()

    def DFS_solve(self):
        pass

    def HillClimbing_solve(self):
        pass
    
    def A_solve(self):
        pass