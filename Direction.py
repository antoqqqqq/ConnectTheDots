from enum import Enum

class Direction(Enum):
    Right ={0,1}
    Left ={0,-1}
    Up ={1,0}
    Down ={-1,0}

    def __init__(self, value):
        self.value = value