from collections import deque
from puzzle import Puzzle

class Node:
    def __init__(self, state, parent, dotsConnectedState):
        self.state = state
        self.parent = parent
        self.dotsConnectedState = dotsConnectedState
        

class BFS:
    def __init__(self, start_state, dots_list, size):
        self.start_state = start_state
        self.dots_list = dots_list
        self.size = size
        self.solution = list
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
            possible_newStates = Puzzle.getPossibleStates(current_node.state, self.dots_list, current_node.dotsConnectedState)
            for new_state in possible_newStates:
                new_dotsConnectedState = current_node.dotsConnectedState.copy()
                new_node = Node(new_state, current_node, new_dotsConnectedState)
                

    