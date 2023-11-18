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

                

    