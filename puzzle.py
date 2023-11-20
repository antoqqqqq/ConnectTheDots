from business import *
from collections import deque
from queue import PriorityQueue
from enumaration import DirectionUtil
from enumaration import Direction
from node import *
import random
import copy

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
        self.nodesVisted = 0
    
    @staticmethod
    #try all possible moves for a dots pair that aren't connected
    #when a dots pair is connected, set the index of the dots pair in dotsConnectedState to true
    def getPossibleStates(state, dots_list, dotsConnectedState, size, cost = 0):
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
        dotColor = dotsPair[2]

        possibleStates = list()
        #traverse to the end of the line
        cur_pos = [pos for pos in dotsPair[0]]
        
        while state[cur_pos[0] * size + cur_pos[1]].line_exit_direction != None:
            row_offset, col_offset =  DirectionUtil.getMoveValue(state[cur_pos[0] * size + cur_pos[1]].line_exit_direction)
            cur_pos[0] += row_offset
            cur_pos[1] += col_offset

        #check if it can go left, right, up, or down
        #if yes, add the new state to the possible states list
        move = "Left"
        next_pos = cur_pos.copy()
        row_offset, col_offset = DirectionUtil.getMoveValueFromName(move)
        next_pos[0] += row_offset
        next_pos[1] += col_offset
        left_cost=cost 
        if(next_pos[0] >= 0 and next_pos[0] < size and next_pos[1] >= 0 and next_pos[1] < size
           and state[next_pos[0] * size + next_pos[1]].line_color == None):
            if state[next_pos[0] * size + next_pos[1]].dot == None or state[next_pos[0] * size + next_pos[1]].dot.color == dotColor:
                newDotsConnedtedState = dotsConnectedState.copy()
                new_state = state.copy()
                new_state[cur_pos[0] * size + cur_pos[1]] = new_state[cur_pos[0] * size + cur_pos[1]].copy()
                new_state[next_pos[0] * size + next_pos[1]] = new_state[next_pos[0] * size + next_pos[1]].copy()
                
                new_state[cur_pos[0] * size + cur_pos[1]].line_exit_direction = Direction.Left.value
                new_state[cur_pos[0] * size + cur_pos[1]].line_color = dotColor
                new_state[next_pos[0] * size + next_pos[1]].line_enter_direction = Direction.Right.value
                new_state[next_pos[0] * size + next_pos[1]].line_color = dotColor
                if new_state[cur_pos[0] * size + cur_pos[1]].line_enter_direction !=None:
                    if new_state[cur_pos[0] * size + cur_pos[1]].line_enter_direction==new_state[next_pos[0] * size + next_pos[1]].line_enter_direction:
                        left_cost+=1
                    else:
                        left_cost+=2
                else:left_cost+=1
                if state[next_pos[0] * size + next_pos[1]].dot != None and state[next_pos[0] * size + next_pos[1]].dot.color == dotColor:
                    newDotsConnedtedState[dotPairIndex] = True

                possibleStates.append((new_state, newDotsConnedtedState,left_cost))

        move = "Right"
        # next_pos = DirectionUtil.getMoveValueFromName(move)
        next_pos = cur_pos.copy()
        row_offset, col_offset = DirectionUtil.getMoveValueFromName(move)
        next_pos[0] += row_offset
        next_pos[1] += col_offset
        right_cost=cost
        if (next_pos[0] >= 0 and next_pos[0] < size and next_pos[1] >= 0 and next_pos[1] < size
           and state[next_pos[0] * size + next_pos[1]].line_color == None):
            if state[next_pos[0] * size + next_pos[1]].dot == None or state[next_pos[0] * size + next_pos[1]].dot.color == dotColor:
                newDotsConnedtedState = dotsConnectedState.copy()
                new_state = state.copy()
                new_state[cur_pos[0] * size + cur_pos[1]] = new_state[cur_pos[0] * size + cur_pos[1]].copy()
                new_state[next_pos[0] * size + next_pos[1]] = new_state[next_pos[0] * size + next_pos[1]].copy()

                new_state[cur_pos[0] * size + cur_pos[1]].line_exit_direction = Direction.Right.value
                new_state[cur_pos[0] * size + cur_pos[1]].line_color = dotColor
                new_state[next_pos[0] * size + next_pos[1]].line_enter_direction = Direction.Left.value
                new_state[next_pos[0] * size + next_pos[1]].line_color = dotColor
                if new_state[cur_pos[0] * size + cur_pos[1]].line_enter_direction !=None:
                    if new_state[cur_pos[0] * size + cur_pos[1]].line_enter_direction==new_state[next_pos[0] * size + next_pos[1]].line_enter_direction:
                        right_cost +=1
                    else:
                        right_cost +=2
                else:right_cost +=1

                if state[next_pos[0] * size + next_pos[1]].dot != None and state[next_pos[0] * size + next_pos[1]].dot.color == dotColor:
                    newDotsConnedtedState[dotPairIndex] = True
                
                possibleStates.append((new_state, newDotsConnedtedState,right_cost))

        move = "Up"
        # next_pos = DirectionUtil.getMoveValueFromName(move)
        next_pos = cur_pos.copy()
        row_offset, col_offset = DirectionUtil.getMoveValueFromName(move)
        next_pos[0] += row_offset
        next_pos[1] += col_offset
        up_cost=cost
        if(next_pos[0] >= 0 and next_pos[0] < size and next_pos[1] >= 0 and next_pos[1] < size
           and state[next_pos[0] * size + next_pos[1]].line_color == None):
            if state[next_pos[0] * size + next_pos[1]].dot == None or state[next_pos[0] * size + next_pos[1]].dot.color == dotColor:
                newDotsConnedtedState = dotsConnectedState.copy()
                new_state = state.copy()
                new_state[cur_pos[0] * size + cur_pos[1]] = new_state[cur_pos[0] * size + cur_pos[1]].copy()
                new_state[next_pos[0] * size + next_pos[1]] = new_state[next_pos[0] * size + next_pos[1]].copy()

                new_state[cur_pos[0] * size + cur_pos[1]].line_exit_direction = Direction.Up.value
                new_state[cur_pos[0] * size + cur_pos[1]].line_color = dotColor
                new_state[next_pos[0] * size + next_pos[1]].line_enter_direction = Direction.Down.value
                new_state[next_pos[0] * size + next_pos[1]].line_color = dotColor
                if new_state[cur_pos[0] * size + cur_pos[1]].line_enter_direction !=None:
                    if new_state[cur_pos[0] * size + cur_pos[1]].line_enter_direction==new_state[next_pos[0] * size + next_pos[1]].line_enter_direction:
                        up_cost +=1
                    else:
                        up_cost +=2
                else:up_cost +=1
                if state[next_pos[0] * size + next_pos[1]].dot != None and state[next_pos[0] * size + next_pos[1]].dot.color == dotColor:
                    newDotsConnedtedState[dotPairIndex] = True

                possibleStates.append((new_state, newDotsConnedtedState,up_cost))

        move = "Down"
        # next_pos = DirectionUtil.getMoveValueFromName(move)
        next_pos = cur_pos.copy()
        row_offset, col_offset = DirectionUtil.getMoveValueFromName(move)
        next_pos[0] += row_offset
        next_pos[1] += col_offset
        down_cost=cost
        if(next_pos[0] >= 0 and next_pos[0] < size and next_pos[1] >= 0 and next_pos[1] < size
           and state[next_pos[0] * size + next_pos[1]].line_color == None):
            if state[next_pos[0] * size + next_pos[1]].dot == None or state[next_pos[0] * size + next_pos[1]].dot.color == dotColor:
                newDotsConnedtedState = dotsConnectedState.copy()
                new_state = state.copy()
                new_state[cur_pos[0] * size + cur_pos[1]] = new_state[cur_pos[0] * size + cur_pos[1]].copy()
                new_state[next_pos[0] * size + next_pos[1]] = new_state[next_pos[0] * size + next_pos[1]].copy()

                new_state[cur_pos[0] * size + cur_pos[1]].line_exit_direction = Direction.Down.value
                new_state[cur_pos[0] * size + cur_pos[1]].line_color = dotColor
                new_state[next_pos[0] * size + next_pos[1]].line_enter_direction = Direction.Up.value
                new_state[next_pos[0] * size + next_pos[1]].line_color = dotColor
                if new_state[cur_pos[0] * size + cur_pos[1]].line_enter_direction !=None:
                    if new_state[cur_pos[0] * size + cur_pos[1]].line_enter_direction==new_state[next_pos[0] * size + next_pos[1]].line_enter_direction:
                        down_cost +=1
                    else:
                        down_cost +=2
                else:down_cost +=1
                if state[next_pos[0] * size + next_pos[1]].dot != None and state[next_pos[0] * size + next_pos[1]].dot.color == dotColor:
                        newDotsConnedtedState[dotPairIndex] = True

                possibleStates.append((new_state, newDotsConnedtedState,down_cost))

        #return the possibleStates list
        random.shuffle(possibleStates)
        return possibleStates
        
    def solve(self):
        if(self.selectedAlgorithm == 'BFS'):
            self.BFS_solve()
        if(self.selectedAlgorithm == 'UCS'):
            self.UCS_solve()
        
    def BFS_solve(self):
        solver = BFS(self.start_state, self.dots_list, self.size)
        self.isSolved, self.solution = solver.solve()
        self.nodesVisted = solver.node_counter

    def UCS_solve(self):
        solver = UCS(self.start_state, self.dots_list, self.size)
        self.isSolved, self.solution = solver.solve()
        self.nodesVisted = solver.node_counter

    def HillClimbing_solve(self):
        pass
    
    def A_solve(self):
        pass

class BFS:
    def __init__(self, start_state, dots_list, size):
        self.start_state = start_state
        self.dots_list = dots_list
        self.size = size
        self.solution = list()
        self.node_counter = 0

    def trace_back_solution(self, node: Node):
        if node is None:
            return
        self.trace_back_solution(node.parent)
        if node.state is not None:
            self.solution.append(node.state)

    def solve(self):
        #insert the root node in queue
        initial_dots_state = [False for i in range(len(self.dots_list))]
        initial_node = Node(self.start_state, None, initial_dots_state)
        queue = deque()
        queue.append(initial_node)

        while queue:
            #get the first added node (FIFO)
            current_node = queue.popleft()
            self.node_counter += 1

            #check if all dots are connected - game is cleared
            if all(current_node.dotsConnectedState) == True:
                self.trace_back_solution(current_node)
                return True, self.solution
            
            #generate leaf childs
            possible_newStates = Puzzle.getPossibleStates(current_node.state, self.dots_list, current_node.dotsConnectedState, self.size)
            for new_state, new_dotsState, cost in possible_newStates:
                new_node = Node(new_state, current_node, new_dotsState)
                queue.append(new_node)

class UCS:
    def __init__(self, start_state, dots_list, size):
        self.start_state = start_state
        self.dots_list = dots_list
        self.size = size
        self.solution = list()
        self.node_counter = 0 
    def trace_back_solution(self, node: Node):
        if node is None:
            return
        self.trace_back_solution(node.parent)
        if node.state is not None:
            self.solution.append(node.state)
    def solve(self):
        #insert the root node in queue
        initial_dots_state = [False for i in range(len(self.dots_list))]
        initial_node = Node(self.start_state, None, initial_dots_state)
        initial_ucsnode= USC_node(0,initial_node)
        Priority_Queue = PriorityQueue()
        Priority_Queue.put((0, initial_ucsnode))
        while Priority_Queue:
            node = Priority_Queue.get()[1]
            self.node_counter += 1
            
            if all(node.dotsConnectedState) == True:
                self.trace_back_solution(node)
                return True, self.solution
            possible_newStates = Puzzle.getPossibleStates(node.state, self.dots_list, node.dotsConnectedState, self.size, int(node.cost))
            for new_state, new_dotsState,new_cost in possible_newStates:
                new_node = Node(new_state, node, new_dotsState)
                New_node = USC_node( new_cost,new_node)
                Priority_Queue.put((new_cost, New_node))

class A_star:
    def __init__(self, start_state, dots_list, size):
        self.start_state = start_state
        self.dots_list = dots_list
        self.size = size
        self.solution = list()
        self.node_counter = 0 

    def trace_back_solution(self, node: Node):
        if node is None:
            return
        self.trace_back_solution(node.parent)
        if node.state is not None:
            self.solution.append(node.state)

    def get_heuristic(self, node: Node):
        h = 0
        for dots in self.dots_list:
            #get the pos of the first Dot and the second Dot
            cur_pos = [pos for pos in dots[0]]
            goal_pos = [pos for pos in dots[1]]
            while node.state[cur_pos[0] * self.size + cur_pos[1]].line_exit_direction != None:
                row_offset, col_offset =  DirectionUtil.getMoveValue(node.state[cur_pos[0] * self.size + cur_pos[1]].line_exit_direction)
                cur_pos[0] += row_offset
                cur_pos[1] += col_offset

            h += abs(goal_pos[0] - cur_pos[0]) + abs(goal_pos[1] - cur_pos[1])
        return h

    def solve(self):
        #insert the root node in queue
        initial_dots_state = [False for i in range(len(self.dots_list))]
        initial_node = Node(self.start_state, None, initial_dots_state)
        initial_Anode= Astar_node(0, 0, initial_node)
        initial_Anode.h_score = self.get_heuristic(initial_Anode)
        Priority_Queue = PriorityQueue()
        Priority_Queue.put((0, initial_Anode))
        while Priority_Queue:
            node = Priority_Queue.get()[1]
            self.node_counter += 1
            
            if all(node.dotsConnectedState) == True:
                self.trace_back_solution(node)
                return True, self.solution
            possible_newStates = Puzzle.getPossibleStates(node.state, self.dots_list, node.dotsConnectedState, self.size, int(node.cost))
            for new_state, new_dotsState,new_cost in possible_newStates:
                new_node = Node(new_state, node, new_dotsState)
                New_node = Astar_node(new_cost,new_node)
                Priority_Queue.put((new_cost, New_node))
