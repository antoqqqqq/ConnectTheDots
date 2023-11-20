class Node:
    def __init__(self, state, parent, dotsConnectedState):
        self.state = state
        self.parent = parent
        self.dotsConnectedState = dotsConnectedState
        
class USC_node:
    def __init__(self, cost, node: Node):
        self.state = node.state
        self.parent = node.parent
        self.dotsConnectedState = node.dotsConnectedState
        self.cost = cost

    def __lt__(self, other):
        if(self.cost < other.cost):
            return True
        return False
    def __gt__(self, other):
        if(self.cost > other.cost):
            return True
        return False
    def __eq__(self, other):
        if(self.cost == other.cost):
            return True
        return False
    
class Astar_node:
    def __init__(self, cost, h_score, node):
        self.state = node.state
        self.parent = node.parent
        self.dotsConnectedState = node.dotsConnectedState
        self.cost = cost
        self.h_score = h_score

    def __lt__(self, other):
        if(self.cost + self.h_score < other.cost + self.h_score):
            return True
        return False
    def __gt__(self, other):
        if(self.cost + self.h_score > other.cost + self.h_score):
            return True
        return False
    def __eq__(self, other):
        if(self.cost + self.h_score == other.cost + self.h_score):
            return True
        return False

    

                

    