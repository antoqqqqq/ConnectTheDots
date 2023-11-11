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
        self.DotTiles = tiles_with_dot
        #init self.tiles
        for i in range(self.n_tiles_perRow):
            for j in range(self.n_tiles_perRow):
                new_tile = Tile(None, None)
                for pos1, pos2, color in tiles_with_dot:
                    if (i, j) == pos1 or (i, j) == pos2:
                        new_tile.dot = Dot(1, color)
                self.tiles.append(new_tile)

    def IsGameClear(self) -> bool:
        tiles_with_dot= self.DotTiles
        for i in range(len(tiles_with_dot)):
            pos1 = []
            firstDot = tiles_with_dot[i][0]
            secondDot = tiles_with_dot[i][1]
            if self.hasExitDir(firstDot[0], firstDot[1]):
                pos1.append( firstDot[0])
                pos1.append( firstDot[1])
            elif self.hasExitDir(secondDot[0], secondDot[1]):
                pos1.append( secondDot[0])
                pos1.append( secondDot[1])
            else:
                return False

            while self.hasExitDir(pos1[0], pos1[1]):
                    cur_pos = (pos1[0], pos1[1])
                    pos1[0] += DirectionUtil.getMoveValue(self.getTileExitDir(cur_pos[0],cur_pos[1]))[0]
                    pos1[1] += DirectionUtil.getMoveValue(self.getTileExitDir(cur_pos[0],cur_pos[1]))[1]


            if self.hasDot(pos1[0], pos1[1]) == False:
                    return False
                # elif self.hasExitDir(pos1[0],pos1[1]) != True:
                    # return False
        return True
        pass

    def new_method(self):
        i=1

    def getTile(self, row: int, col: int) -> Tile:
        return self.tiles[row * self.n_tiles_perRow + col]
    
    def getTileFromMousePos(self, mousePos: Tuple[int, int]) -> Tile:
        pass
    
    def setTile(self, row, col, enter_direction, exit_direction, line_color):
        self.tiles[row * self.n_tiles_perRow + col].line_enter_direction = enter_direction
        self.tiles[row * self.n_tiles_perRow + col].line_exit_direction = exit_direction
        self.tiles[row * self.n_tiles_perRow + col].line_color = line_color
        
    def setTileLineDir(self, row, col, exit_dir, enter_dir = None):
        self.tiles[row * self.n_tiles_perRow + col].line_enter_direction = enter_dir
        self.tiles[row * self.n_tiles_perRow + col].line_exit_direction = exit_dir
    
    def setTileEnterDir(self, row, col, enter_dir):
        self.tiles[row * self.n_tiles_perRow + col].line_enter_direction = enter_dir

    def setTileExitDir(self, row, col, exit_dir):
        self.tiles[row * self.n_tiles_perRow + col].line_exit_direction = exit_dir

    def getTileLineDir_LineColor(self, row, col) -> Tuple[Direction, Direction, Color]:
        enter_dir = self.tiles[row * self.n_tiles_perRow + col].line_enter_direction
        exit_dir = self.tiles[row * self.n_tiles_perRow + col].line_exit_direction
        line_color = self.tiles[row * self.n_tiles_perRow + col].line_color
        return enter_dir, exit_dir, line_color
    
    def getTileLineDir(self, row, col) -> Tuple[Direction, Direction]:
        enter_dir = self.tiles[row * self.n_tiles_perRow + col].line_enter_direction
        exit_dir = self.tiles[row * self.n_tiles_perRow + col].line_exit_direction
        return enter_dir, exit_dir

    def getTileExitDir(self, row, col) -> Direction:
        return self.tiles[row * self.n_tiles_perRow + col].line_exit_direction
    
    def containsLine(self, row, col) -> bool:
        return self.tiles[row * self.n_tiles_perRow + col].line_exit_direction != None or self.tiles[row * self.n_tiles_perRow + col].line_enter_direction != None

    def setTileLineColor(self, row, col, color):
        self.tiles[row * self.n_tiles_perRow + col].line_color = color

    def getTileLineColor(self, row, col):
        return self.tiles[row * self.n_tiles_perRow + col].line_color
    
    def getTileDot(self, row, col):
        return self.tiles[row * self.n_tiles_perRow + col].getDot()

    def hasDot(self, row, col) -> bool:
        dot = self.getTileDot(row, col)
        if(dot == None):
            return False
        return True

    def hasLineColor(self, row, col) -> bool:
        if self.tiles[row * self.n_tiles_perRow + col].line_color == None:
            return False
        return True
    
    def hasExitDir(self, row, col) -> bool:
        return self.tiles[row * self.n_tiles_perRow + col].line_exit_direction != None
    
    def hasEnterDir(self, row, col) -> bool:
        return self.tiles[row * self.n_tiles_perRow + col].line_enter_direction != None

    def getTileWithDotPos(self):
        return [(row, col, dot.color) for row, col in enumerate(self.tiles) for dot in col if dot is not None]
    
    def getOtherDotTile(self, row, col):
        if self.hasDot(row, col) == False:
            return None
        
        dotColor = self.getTileDot(row, col).color
        for dotPair in self.DotTiles:
            if(dotPair[2] == dotColor):
                if((row, col) != dotPair[0]):
                    return dotPair[0]
                else:
                    return dotPair[1]
        
    #set all the connected tiles directions, line_color to None
    #pass in the starting Dot Tile
    def resetTilesMovement(self, row, col):
        if self.hasDot(row, col) == False:
            return
        
        cur_row, cur_col = row, col
        while self.hasExitDir(cur_row, cur_col):
            dir_value = self.getTileExitDir(cur_row, cur_col)
            self.setTile(cur_row, cur_col, None, None, None)

            offset_r, offset_c = DirectionUtil.getMoveValue(dir_value)
            cur_row += offset_r
            cur_col += offset_c
        self.setTile(cur_row, cur_col, None, None, None)

