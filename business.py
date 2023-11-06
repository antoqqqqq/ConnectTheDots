from typing import Optional , List, Tuple
from enumaration import *

class Dot:
    def __init__(self, value : int , color : str):
        self.value = value
        self.color = color
        
class Tile:
    def __init__(self, line_color = (int, int, int),  dot : Optional ['Dot'] = None):
        self.dot = dot
        self.line_enter_direction = None
        self.line_exit_direction = None
        self.line_color = line_color

    def getDot(self):
        return self.dot
        

class Board:
    def __init__(self, n_tiles_perRow, tile_length , dot_radius, tiles_with_dot):
        self.n_tiles_perRow = n_tiles_perRow
        self.tile_length = tile_length
        self.dot_radius = dot_radius
        self.tiles = []
        for i in range(self.n_tiles_perRow):
            for j in range(self.n_tiles_perRow):
                new_tile = Tile(None, None)
                for pos1, pos2, color in tiles_with_dot:
                    if (i, j) == pos1 or (i, j) == pos2:
                        new_tile.dot = Dot(1, color)
                self.tiles.append(new_tile)

    def IsGameClear(self):
        pass

    def getTile(self, row: int, col: int) -> Tile:
        return self.tiles[row * self.n_tiles_perRow + col]
    
    def getTileFromMousePos(self, mousePos: Tuple[int, int]) -> Tile:
        pass
    
    def setTile(self, row, col, direction, assigned_dir = "Enter", line_color = None):
        if assigned_dir == "Enter": 
            self.tiles[row * self.n_tiles_perRow + col].line_enter_direction = direction
        elif assigned_dir == "Exit":
            self.tiles[row * self.n_tiles_perRow + col].line_exit_direction = direction
        self.tiles[row * self.n_tiles_perRow + col].line_color = line_color
        
        
        

    def setTileLineDir(self, row, col, exit_dir, enter_dir = None):
        self.tiles[row * self.n_tiles_perRow + col].line_enter_direction = enter_dir
        self.tiles[row * self.n_tiles_perRow + col].line_exit_direction = exit_dir
    
    def getTileLineDir_LineColor(self, row, col) -> Tuple[Direction, Direction, Color]:
        enter_dir = self.tiles[row * self.n_tiles_perRow + col].line_enter_direction
        exit_dir = self.tiles[row * self.n_tiles_perRow + col].line_exit_direction
        line_color = self.tiles[row * self.n_tiles_perRow + col].line_color
        return enter_dir, exit_dir, line_color

    def containsLine(self, row, col) -> bool:
        return self.tiles[row * self.n_tiles_perRow + col].line_exit_direction != None or self.tiles[row * self.n_tiles_perRow + col].line_enter_direction != None

    def setTileLineColor(self, row, col, color):
        self.tiles[row * self.n_tiles_perRow + col].line_color = color

    def getTileDot(self, row, col):
        return self.tiles[row * self.n_tiles_perRow + col].getDot()

    def getTileWithDotPos(self):
        return [(row, col, dot.color) for row, col in enumerate(self.tiles) for dot in col if dot is not None]
    
# board = Board()
# test = 0
# test = 1
# print("")
# print("")
