from enum import Enum
class Direction(Enum):
    Right =[-0.5, -0.75]
    Left =[-1, -0.75]
    Up =[-0.75, -1]
    Down =[-0.75, -0.5]
            
class DirectionUtil:
    @staticmethod
    def getMoveValue(direction_value):
        moveName = Direction(value=direction_value).name
        if(moveName == "Right"):
            return (0, 1)
        elif(moveName == "Left"):
            return (0, -1)
        elif(moveName == "Down"):
            return (1, 0)
        elif(moveName == "Up"):
            return (-1, 0)
        
    @staticmethod
    def getMoveValueFromName(direction_name):
        if(direction_name == "Right"):
            return (0, 1)
        elif(direction_name == "Left"):
            return (0, -1)
        elif(direction_name == "Down"):
            return (1, 0)
        elif(direction_name == "Up"):
            return (-1, 0)
    
class Color(Enum):
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    YELLOW =(255,255,0)
    FUCHSIA =(255,0,255)
    AQUA =(0,255,255)
    BLACK = (0,0,0)
    SILVER =(192,192,192)
    DEEPPINK =(255,20,147)
    ORANGE =(255,165,0)