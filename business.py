from typing import Optional , List, Tuple
from enum import Enum

class Dot:
    def __init__(self, value : int , color : str):
        self.value = value
        self.color = color
        pass
class Tile:
    def __init__(self, line_color = (int, int, int),  dot : Optional ['Dot'] = None):
        self.dot = dot
        self.line_enter_direction = None
        self.line_exit_direction = None
        self.line_color = line_color

        def GetDot(self):
            return self.dot
        pass

class Board:
    def __init__(self, n_rowTiles, n_colTiles, tile_length , dot_radius, tiles_with_dot):
        self.n_rowTiles = n_rowTiles
        self.n_colTiles = n_colTiles
        self.tiles = []
        for i in range(self.n_rowTiles):
            for j in range(self.n_colTiles):
                new_tile = Tile(None, None)
                for pos1, pos2, color in tiles_with_dot:
                    if (i, j) == pos1 or (i, j) == pos2:
                        new_tile.dot = Dot(1, color)
                self.tiles.append(new_tile)

    def IsGameClear(self):
        pass

    def getTile(self, row: int, col: int) -> Tile:
        return self.tiles[row][col]
    
    def getTileFromMousePos(self, mousePos: Tuple[int, int]) -> Tile:
        pass
    
    def setTileLineDir(self, row, col, enter_dir, exit_dir):
        self.tiles[row][col].line_enter_direction = enter_dir
        self.tiles[row][col].line_exit_direction = exit_dir

    def setTileLineColor(self, row, col, color):
        self.tiles[row][col].line_color = color

    def getTileWithDotPos(self):
        return [(row, col, dot.color) for row, col in enumerate(self.tiles) for dot in col if dot is not None]
    
# board = Board()
# test = 0
# test = 1
# print("")
# print("")
