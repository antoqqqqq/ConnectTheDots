from enum import Enum
class Direction(Enum):
    Right =[-0.5, -0.75]
    Left =[-1, -0.75]
    Up =[-0.75, -1]
    Down =[-0.75, -0.5]

# class Move(Enum):
#     Right = (0, 1)
#     Left = (0, -1)
#     Up = (-1, 0)
#     Down = (1, 0)
    
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