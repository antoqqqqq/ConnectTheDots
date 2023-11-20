import pygame
from data import *
from sprite import *
from business import *
from puzzle import Puzzle
from threading import *
import time

class GameMenu:
    def __init__(self, setting_option, stage_number):
        self.setting_option = setting_option
        self.width, self.height, self.board_length = self.get_setting_config(setting_option)
        self.background_color = (85, 88, 67)
        self.stage_number = stage_number
        self.board_topLeft = [350, 37]
        self.board_border = 5
        self.board = self.create_game(self.stage_number)
        self.gameClear = False
        self.showCongratulation = True
        high_score = read_score('resources/score/level'+str(stage_number)+'.txt')
        self.best_num_moves = high_score[1]
        self.best_num_turn  = high_score[2]
        self.best_num_time = high_score[3]
        #self.get_score()
        self.cur_num_moves = 0
        self.cur_num_turn  = 0
        self.cur_num_time = 0

        self.go_to_next_stage = False

        #variables for processing user mouse inputs on board 
        self.Algorithm_solved = False
        self.is_connecting_dot = False
        self.previous_passed_tile_rc = None
        self.current_held_tile_rc = None
        self.current_held_color = None
        self.start_tile_rc = None

        #pygame variables
        pygame.init()
        #screen to draw 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect the Dots  - Group 1")
        self.clock = pygame.time.Clock()
        self.init_all_sprites()
        self.button_list = []
        self.text_button_list = []
        self.button_win= []
        self.init_all_buttons()
        self.selectedAlgorithm = "BFS"

    def init_all_buttons(self):        
        self.init_all_text_buttons()

    def init_all_text_buttons(self):
        self.text_button_list.append(TextButton(175, 31, 100, 80 - 30, "Solve", font_size = 28,color=(245, 238, 200), hover_color=(0, 21, 36), text_color=(0, 21, 36)))
        self.text_button_list.append(TextButton(39, 31, 100, 80 - 30, "Change", font_size = 28,color=(245, 238, 200), hover_color=(0, 21, 36), text_color=(0, 21, 36)))
        self.text_button_list.append(TextButton(39, 461 + 40, 100, 80, "Home", font_size = 35,color=(245, 238, 200), hover_color=(0, 21, 36), text_color=(0, 21, 36)))
        self.text_button_list.append(TextButton(175, 461 + 40, 100, 80, "Reset", font_size = 35,color=(245, 238, 200), hover_color=(0, 21, 36), text_color=(0, 21, 36)))

    def drawInitalMenu(self):
        self.draw()

    def init_all_sprites(self):
        self.sprite_list = pygame.sprite.Group()
        #self.sprite_list.add(Sprite(0, 0, "resources/images/background1.jpg", self.width, self.height))

    def draw_TextButton(self):
        TextButton(39, 174, 236, 70, "LEVEL " + str(self.stage_number), font_size = 50,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(134, 10, 53)).draw(self.screen)
        TextButton(39, 238 + 40, 103, 189, "", font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255)).draw(self.screen)
        TextButton(39, 238 + 65, 103, 0, "Current", font_size = 27,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(25, 38, 85)).draw(self.screen)
        TextButton(39, 238 + 100, 103, 0, "Move", font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)
        TextButton(39, 238 + 120, 103, 0, str(self.cur_num_moves), font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)
        TextButton(39, 238 + 145, 103, 0, "Turns", font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)
        TextButton(39, 238 + 165, 103, 0, str(self.cur_num_turn), font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)
        TextButton(39, 238 + 190, 103, 0, "Time", font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)
        TextButton(39, 238 + 210, 103, 0, str(self.cur_num_time), font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)

        TextButton(175, 238 + 40, 103, 189, "", font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255)).draw(self.screen)
        TextButton(175, 238 + 65, 103, 0, "Best", font_size = 27,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(25, 38, 85)).draw(self.screen)
        TextButton(175, 238 + 100, 103, 0, "Move", font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)
        TextButton(175, 238 + 120, 103, 0, str(self.best_num_moves), font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)
        TextButton(175, 238 + 145, 103, 0, "Turns", font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)
        TextButton(175, 238 + 165, 103, 0, str(self.best_num_turn), font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)
        TextButton(175, 238 + 190, 103, 0, "Time", font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)
        TextButton(175, 238 + 210, 103, 0, str(self.best_num_time), font_size = 20,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)
        TextButton(39, 100, 236, 50, "Algorithm: " + self.selectedAlgorithm, font_size = 28,color=(245, 238, 200), hover_color=(255, 255, 255), text_color=(0, 21, 36)).draw(self.screen)

        for button in self.text_button_list:
            button.draw(self.screen)
  
    def get_setting_config(self, setting_option):
        width = 900
        height = 600
        board_length = 500

        if(setting_option == 1):
            pass
        elif(setting_option == 2):
            pass
        elif(setting_option == 3):
            pass
        
        return width, height, board_length

    def resetGame(self):
        self.cur_num_moves = 0
        self.cur_num_turn  = 0
        self.cur_num_time = 0
        high_score= read_score('resources/score/level'+str(self.stage_number)+'.txt')
        self.best_num_moves = high_score[1]
        self.best_num_turn  = high_score[2]
        self.best_num_time = high_score[3]
        self.button_win=[]
        self.board = self.create_game(self.stage_number)
        self.gameClear = False
        self.showCongratulation = True
        self.Algorithm_solved = False
        self.is_connecting_dot = False
        self.previous_passed_tile_rc = None
        self.current_held_tile_rc = None
        self.current_held_color = None
        self.start_tile_rc = None

    def get_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        return x, y
    
    def create_game(self, stage_number):
        info_stage=read_stage('resources/level/level'+str(stage_number)+'.txt')
        n_tiles_perRow=info_stage[1]
        tile_length = self.board_length / n_tiles_perRow
        dot_radius = int(tile_length * 0.3)
        tiles_with_dot=info_stage[3]

        new_board = Board(n_tiles_perRow, tile_length, dot_radius, tiles_with_dot)
        self.puzzle_solver = Puzzle(new_board.tiles, new_board.DotTiles, new_board.n_tiles_perRow, algorithm='UCS')
        self.beginTime = round(time.time(), 3)
        return new_board

    def save_score(self, file_path):
        data=[]
        data= readfile(file_path)
        i=0
        for row in data:
            if (self.stage_number == row[0] and self.num_moves<=row[1] and self.num_turn<=row[2] and self.num_time<=row[3]):
                write_file(file_path,str(self.stage_number)+"-"+str(self.num_moves)+"-"+str(self.num_turn)+"-"+str(self.num_time))                           
                break
            i=+1        

    def get_score(self, file_path):
        data=[]
        data= readfile(file_path)
        i=0
        for row in data:
            if (self.stage_number == row[0]):
                self.best_num_moves = data[i][1]
                self.best_num_turn  = data[i][2]
                self.best_num_time  = data[i][3]
                break
            i=+1

    def cursor_in_Board(self, mouse_x, mouse_y) -> bool:
        if (mouse_x >= self.board_topLeft[0] and mouse_x < self.board_topLeft[0] + self.board_length 
            and mouse_y >= self.board_topLeft[1] and mouse_y <= self.board_topLeft[1] + self.board_length):
            return True
        return False

    def get_Tile_pos(self, mouse_x, mouse_y) -> Tuple[int, int] | None:
        x_startLeft, y_startTop = self.board_topLeft[0] + self.board_border, self.board_topLeft[1] + self.board_border
        x_startRight, y_startBottom= x_startLeft + self.board.tile_length, y_startTop + self.board.tile_length

        for c in range(self.board.n_tiles_perRow):
            tile_topLeft = [x_startLeft + c * self.board.tile_length, y_startTop]
            tile_bottomRight = [x_startRight + c * self.board.tile_length, y_startBottom]
            for r in range(self.board.n_tiles_perRow):
                tile_topLeft[1] = y_startTop + r * self.board.tile_length
                tile_bottomRight[1] = y_startBottom + r * self.board.tile_length
                
                if (mouse_x >= tile_topLeft[0] and mouse_x < tile_bottomRight[0]
                   and mouse_y >= tile_topLeft[1] and mouse_y < tile_bottomRight[1]):
                    print(str(r) + " " + str(c))
                    return [r, c]
        
        return None
    
    def event(self):
        #check if user press the exit button on the top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = self.get_mouse_pos()
                if(self.is_connecting_dot == False and self.gameClear == False):
                    if self.cursor_in_Board(mouse_x, mouse_y):
                        r, c = self.get_Tile_pos(mouse_x, mouse_y)
                        if(self.board.getTileDot(r, c) != None):
                            self.is_connecting_dot = True
                            self.current_held_color = self.board.getTileDot(r, c).color  
                            self.start_tile_rc = [r, c]

                if self.gameClear and self.showCongratulation:
                    

                    for button in self.button_win:
                        if(button.click(self.get_mouse_pos()) == False):
                            continue  
                        if(button.getButtonText() == "Try Again"):
                            self.resetGame()
                        if(button.getButtonText() == "Next Level"):
                            self.playing = False
                            self.go_to_next_stage = True
                        if(button.getButtonText() == "See Result"):
                            self.showCongratulation = False

                for text_button in self.text_button_list:
                    if text_button.click((mouse_x, mouse_y)) == False:
                        continue

                    if text_button.getButtonText() == "Solve" and self.gameClear == False:
                        self.Algorithm_solved = True
                        self.puzzle_solver.selectedAlgorithm = self.selectedAlgorithm
                        self.startAlgorithmTime = time.time()
                        self.puzzle_solver.solve()

                    if(text_button.getButtonText() == "Reset"):
                        self.resetGame()
                    if(text_button.getButtonText() == "Home"):
                        self.playing = False
                    if(text_button.getButtonText() == "Change"):
                        if self.selectedAlgorithm == "BFS":
                            self.selectedAlgorithm = "UCS"
                        elif self.selectedAlgorithm == "UCS":
                            self.selectedAlgorithm = "BFS"
                                  
            if event.type == pygame.MOUSEBUTTONUP:
                self.is_connecting_dot = False
              
    def getDirectionName(self, r_dif, c_dif):
        #go right
        if(r_dif, c_dif) == (0, 1):
            return "Right"
        #go left
        elif(r_dif, c_dif) == (0, -1):
            return "Left"
        #go down
        elif(r_dif, c_dif) == (1, 0):
            return "Down"
        #go up
        elif(r_dif, c_dif) == (-1, 0):
            return "Up"
    
    def getMoveValue(self, move: str):
        r = 0
        c = 0
        if(move == "Right"):
            c = 1
        elif(move == "Left"):
            c = -1
        elif(move == "Up"):
            r = -1
        elif(move == "Down"):
            r = 1
        return r, c
    
    def processPressedTile(self, pressedTile_pos):
        if(pressedTile_pos == None):
            return
        
        #first click
        if(self.current_held_tile_rc == None):
            self.board.resetTilesMovement(pressedTile_pos[0], pressedTile_pos[1])
            otherDotPos = self.board.getOtherDotTile(pressedTile_pos[0], pressedTile_pos[1])
            self.board.resetTilesMovement(otherDotPos[0], otherDotPos[1])
            self.current_held_tile_rc = pressedTile_pos
            return
        
        #stop processing movement if user hasn't moved cursor to a different Tile
        if(self.current_held_tile_rc == pressedTile_pos):
            return
        
        #prevent moving diagonally or other types of movement, can only move 1 step in row or column at a time
        if(abs(pressedTile_pos[0] - self.current_held_tile_rc[0]) + abs(pressedTile_pos[1] - self.current_held_tile_rc[1]) >= 2):
            return
        
        #check if Tile has Dot
        if self.board.hasDot(pressedTile_pos[0], pressedTile_pos[1]):
            #prevent moving to Dot Tile with different color
            if(self.board.getTileDot(pressedTile_pos[0], pressedTile_pos[1]).color != self.current_held_color):
                return

        #move from first dot to next tile
        if(self.previous_passed_tile_rc == None):
            #prevent moving if the next Tile has line color already
            if self.board.hasLineColor(pressedTile_pos[0], pressedTile_pos[1]):
                return
            
            self.previous_passed_tile_rc = self.current_held_tile_rc
            self.current_held_tile_rc = pressedTile_pos

            r_dif = self.current_held_tile_rc[0] - self.previous_passed_tile_rc[0]
            c_dif = self.current_held_tile_rc[1] - self.previous_passed_tile_rc[1]
            directionName = self.getDirectionName(r_dif, c_dif) 
            previous_to_current_Exitdirection = directionName

            r_dif = self.previous_passed_tile_rc[0] - self.current_held_tile_rc[0]
            c_dif = self.previous_passed_tile_rc[1] - self.current_held_tile_rc[1]
            directionName = self.getDirectionName(r_dif, c_dif) 
            current_to_previous_Enterdirection = directionName

            self.board.setTileExitDir(self.previous_passed_tile_rc[0], self.previous_passed_tile_rc[1], Direction[previous_to_current_Exitdirection].value)
            self.board.setTileLineColor(self.previous_passed_tile_rc[0], self.previous_passed_tile_rc[1], color=self.current_held_color)
            self.board.setTileEnterDir(self.current_held_tile_rc[0], self.current_held_tile_rc[1], Direction[current_to_previous_Enterdirection].value)
            self.board.setTileLineColor(self.current_held_tile_rc[0], self.current_held_tile_rc[1], color=self.current_held_color)
            return
        
        #stop moving if connect with the second dot
        if self.board.hasDot(self.current_held_tile_rc[0], self.current_held_tile_rc[1]) and pressedTile_pos != self.previous_passed_tile_rc:
            return
   
        #from second move onward
        if pressedTile_pos != self.current_held_tile_rc and pressedTile_pos != self.previous_passed_tile_rc:
            #prevent moving to the origin Dot Tile
            if pressedTile_pos == self.start_tile_rc:
                return
            
            #prevent moving if the next Tile has line color already
            if self.board.hasLineColor(pressedTile_pos[0], pressedTile_pos[1]):
                return
            
            self.previous_passed_tile_rc = self.current_held_tile_rc
            self.current_held_tile_rc = pressedTile_pos

            r_dif = self.current_held_tile_rc[0] - self.previous_passed_tile_rc[0]
            c_dif = self.current_held_tile_rc[1] - self.previous_passed_tile_rc[1]
            directionName = self.getDirectionName(r_dif, c_dif) 
            previous_to_current_Exitdirection = directionName

            r_dif = self.previous_passed_tile_rc[0] - self.current_held_tile_rc[0]
            c_dif = self.previous_passed_tile_rc[1] - self.current_held_tile_rc[1]
            directionName = self.getDirectionName(r_dif, c_dif) 
            current_to_previous_Enterdirection = directionName

            self.board.setTileExitDir(self.previous_passed_tile_rc[0], self.previous_passed_tile_rc[1], Direction[previous_to_current_Exitdirection].value)
            self.board.setTileEnterDir(self.current_held_tile_rc[0], self.current_held_tile_rc[1], Direction[current_to_previous_Enterdirection].value)
            self.board.setTileLineColor(self.current_held_tile_rc[0], self.current_held_tile_rc[1], color=self.current_held_color)
            return

        #tracing back moves
        if(pressedTile_pos == self.previous_passed_tile_rc):
            self.board.setTileEnterDir(self.current_held_tile_rc[0], self.current_held_tile_rc[1], None)
            self.board.setTileLineColor(self.current_held_tile_rc[0], self.current_held_tile_rc[1], None)
            self.board.setTileExitDir(self.previous_passed_tile_rc[0], self.previous_passed_tile_rc[1], None)

            self.current_held_tile_rc = pressedTile_pos
            previous_enter_dir, previous_exit_dir = self.board.getTileLineDir(self.previous_passed_tile_rc[0], self.previous_passed_tile_rc[1])
            if(previous_enter_dir == None):
                self.previous_passed_tile_rc = None
                return
            rol_offset, col_offset = self.getMoveValue(Direction(previous_enter_dir).name)
            self.previous_passed_tile_rc[0] += rol_offset
            self.previous_passed_tile_rc[1] += col_offset
            return
        
    def update(self):
        mouse_pos = self.get_mouse_pos()
        self.cur_num_moves , self.cur_num_turn = self.board.getMove_turn()
        for text_button in self.text_button_list:
            text_button.hover(mouse_pos)

        if self.board.IsGameClear() and self.gameClear == False:
            self.gameClear=True
            self.button_win.append(TextButton(225, 375, 100, 75, "Next Level", font_size=25))
            self.button_win.append(TextButton(400, 375, 100, 75, "Try Again", font_size=25))
            self.button_win.append(TextButton(575, 375, 100, 75, "See Result", font_size=25))
        elif self.gameClear:
            for button in self.button_win:
                button.hover(self.get_mouse_pos())

        if self.is_connecting_dot:
            mouse_x, mouse_y = self.get_mouse_pos()
            pressed_Tile_pos = self.get_Tile_pos(mouse_x, mouse_y)
            self.processPressedTile(pressed_Tile_pos)
        else:
            self.current_held_tile_rc = None
            self.previous_passed_tile_rc = None
            self.current_held_color = None
            self.start_tile_rc = None

        if self.gameClear == False:
            self.cur_num_time = round(time.time() - self.beginTime, 3)

        if self.puzzle_solver.isSolved and self.gameClear == False:
            self.board.tiles=self.puzzle_solver.solution[-1]
            self.cur_num_time = round(time.time() - self.startAlgorithmTime, 3)
        if self.puzzle_solver.isSolved==False and self.gameClear == True:
            if self.cur_num_turn< int(self.best_num_turn) or int(self.best_num_moves)==0:
                write_file('resources/score/level'+str(self.stage_number)+'.txt', str(self.stage_number)+'-'+str(self.cur_num_moves)+'-'+str(self.cur_num_turn)+'-'+str(self.cur_num_time))
            elif self.cur_num_turn== int(self.best_num_turn):
                if self.cur_num_moves < int(self.best_num_moves):
                    write_file('resources/score/level'+str(self.stage_number)+'.txt', str(self.stage_number)+'-'+str(self.cur_num_moves)+'-'+str(self.cur_num_turn)+'-'+str(self.cur_num_time))
                elif self.cur_num_moves == int(self.best_num_moves):
                    if self.cur_num_time < float(self.best_num_time):
                        write_file('resources/score/level'+str(self.stage_number)+'.txt', str(self.stage_number)+'-'+str(self.cur_num_moves)+'-'+str(self.cur_num_turn)+'-'+str(self.cur_num_time))
   
    def draw_board(self):
        x_start, y_start = self.board_topLeft[0], self.board_topLeft[1]
        board_length = self.board_length
        tile_length = self.board.tile_length
        border_width = self.board_border
        rect_length = tile_length * 0.5

        #draw the the Board's top and left sides
        pygame.draw.line(self.screen, Color.SILVER.value, (x_start, y_start), (x_start + board_length, y_start), width=border_width)
        pygame.draw.line(self.screen, Color.SILVER.value, (x_start, y_start), (x_start, y_start + board_length), width=border_width)

        y = y_start
        
        for r in range(self.board.n_tiles_perRow):
            x = x_start
            y += tile_length
            for c in range(self.board.n_tiles_perRow):
                x += tile_length
                #draw Tiles right and bottom sides
                pygame.draw.line(self.screen, Color.SILVER.value, (x, y - tile_length), (x, y), width=border_width)
                pygame.draw.line(self.screen, Color.SILVER.value, (x - tile_length, y), (x, y), width=border_width)

                #draw Dot
                if(self.board.getTileDot(r, c) != None):
                    pygame.draw.circle(self.screen, self.board.getTileDot(r, c).color, (x - tile_length/2, y - tile_length/2), self.board.dot_radius, width = 0)
                #draw Line
                if self.board.containsLine(r, c):
                    enter_dir, exit_dir, line_color = self.board.getTileLineDir_LineColor(r, c)
                    if(enter_dir != None):
                        rect_x = x + (enter_dir[0] * tile_length)
                        rect_y = y + (enter_dir[1] * tile_length)
                        rect_width = rect_length
                        rect_height = rect_length
                        pygame.draw.rect(self.screen, line_color, [rect_x, rect_y, rect_width, rect_height])
                        pygame.draw.circle(self.screen, line_color, (x - tile_length * 0.5, y - tile_length * 0.5), rect_length / 2)
                        
                    if(exit_dir != None):
                        rect_x = x + (exit_dir[0] * tile_length)
                        rect_y = y + (exit_dir[1] * tile_length)
                        rect_width = rect_length
                        rect_height = rect_length
                        if(exit_dir == Direction.Up.value):
                            rect_y -= 5
                            rect_height += 5
                        if(exit_dir == Direction.Down.value):
                            rect_height += 5
                        if(exit_dir == Direction.Left.value):
                            rect_x -= 5
                            rect_width += 5
                        if(exit_dir == Direction.Right.value):
                            rect_width += 5
                        pygame.draw.rect(self.screen, line_color, [rect_x, rect_y, rect_width, rect_height])
        
    def draw(self):        
        self.screen.fill(self.background_color)
        self.sprite_list.draw(self.screen)
        self.draw_board()
        self.draw_TextButton()

        if self.gameClear and self.showCongratulation:
            TextButton(200, 100, 500, 400, "", color=(255, 144, 194)).draw(self.screen)

            TextButton(200, 150, 250, 0, "Move", font_size=40, color=(255, 144, 194)).draw(self.screen)
            TextButton(200, 200, 250, 0, str(self.cur_num_moves), font_size=40, color=(255, 144, 194)).draw(self.screen)
            TextButton(200, 250, 250, 0, "Turns", font_size=40, color=(255, 144, 194)).draw(self.screen)
            TextButton(200, 300, 250, 0, str(self.cur_num_turn), font_size=40, color=(255, 144, 194)).draw(self.screen)

            TextButton(450, 150, 250, 0, "Time", font_size=40, color=(255, 144, 194)).draw(self.screen)
            TextButton(450, 200, 250, 0, str(self.cur_num_time), font_size=40, color=(255, 144, 194)).draw(self.screen)

            if(self.puzzle_solver.isSolved):
                TextButton(450, 250, 250, 0, "Nodes Visted", font_size=40, color=(255, 144, 194)).draw(self.screen)
                TextButton(450, 300, 250, 0, str(self.puzzle_solver.nodesVisted), font_size=40, color=(255, 144, 194)).draw(self.screen)

            for button in self.button_win:
                button.draw(self.screen)

        pygame.display.flip()
          
    def run(self):
        self.playing = True
        self.drawInitalMenu()

        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()

        if self.go_to_next_stage:
            gameMenu = GameMenu(0, self.stage_number+1)
            gameMenu.run()

class StageMenu:
    def __init__(self, setting_option):
        self.setting_option = setting_option
        self.width, self.height, self.board_width, self.board_height = self.get_setting_config(setting_option)
        self.background_color = (242, 255, 233)

        #pygame variables
        pygame.init()
        #screen to draw 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect the Dots - Group 1")
        self.clock = pygame.time.Clock()

        # self.init_all_sprites()
        self.button_list = []
        self.init_all_buttons()
        self.text_button_list = []
        self.init_all_text_buttons()

    def get_setting_config(self, setting_option):
        width = 900
        height = 600
        board_width = 500
        board_height = 500

        if(setting_option == 1):
            pass
        elif(setting_option == 2):
            pass
        elif(setting_option == 3):
            pass

        return width, height, board_width, board_height
    
    def init_all_buttons(self):        
        pass
    
    def init_all_text_buttons(self):
        self.text_button_list.append(TextButton(50 + 118, 172, 83, 54, "Level 1", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 264, 172, 83, 54, "Level 2", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 410, 172, 83, 54, "Level 3", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 556, 172, 83, 54, "Level 4", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 702, 172, 83, 54, "Level 5", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 118, 338, 83, 54, "Level 6", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 264, 338, 83, 54, "Level 7", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 410, 338, 83, 54, "Level 8", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 556, 338, 83, 54, "Level 9", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 702, 338, 83, 54, "Level 10", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 118, 503, 83, 54, "Level 11", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 264, 503, 83, 54, "Level 12", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 410, 503, 83, 54, "Level 13", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 556, 503, 83, 54, "Level 14", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))
        self.text_button_list.append(TextButton(50 + 702, 503, 83, 54, "Level 15", font_size = 25,color=(85, 124, 85), hover_color=(250, 112, 112), text_color=(250, 112, 112)))

        self.text_button_list.append(TextButton(750, 0, 150, 100, "Go Back", font_size = 35,color=(25, 38, 85), hover_color=(225, 170, 116), text_color=(225, 170, 116)))

      
    def drawInitalMenu(self):
        self.draw()

    def get_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        return x, y  

    def event(self):
        #check if user press the exit button on the top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.text_button_list:
                    if(button.click(self.get_mouse_pos()) == False):
                        continue
                    
                    if(button.getButtonText()) == "Go Back":
                        self.playing = False
                    if(button.getButtonText() == "Level 1"):
                        gameMenu = GameMenu(0, 1)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 2"):
                        gameMenu = GameMenu(0, 2)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 3"):
                        gameMenu = GameMenu(0, 3)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 4"):
                        gameMenu = GameMenu(0, 4)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 5"):
                        gameMenu = GameMenu(0, 5)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 6"):
                        gameMenu = GameMenu(0, 6)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 7"):
                        gameMenu = GameMenu(0, 7)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 8"):
                        gameMenu = GameMenu(0, 8)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 9"):
                        gameMenu = GameMenu(0, 9)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 10"):
                        gameMenu = GameMenu(0, 10)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 11"):
                        gameMenu = GameMenu(0, 11)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 12"):
                        gameMenu = GameMenu(0, 11)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 13"):
                        gameMenu = GameMenu(0, 11)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 14"):
                        gameMenu = GameMenu(0, 11)
                        gameMenu.run()
                    if(button.getButtonText() == "Level 15"):
                        gameMenu = GameMenu(0, 11)
                        gameMenu.run()

    def update(self):
        for text_button in self.text_button_list:
            text_button.hover(self.get_mouse_pos())
    
    def draw_labels(self):
        Label(190, 0, "Select Stage", font_size= 80, color = (250, 112, 112)).draw(self.screen)

    def draw_Textbutton(self):
      TextButton(34, 77, 100, 80, "BASIC", font_size = 30,color=(218, 12, 129), hover_color=(255, 255, 255)).draw(self.screen)
      TextButton(34, 242, 100, 80, "MEDIUM", font_size = 30,color=(148, 11, 146), hover_color=(255, 255, 255)).draw(self.screen)
      TextButton(34, 407, 100, 80, "HARD", font_size = 30,color=(97, 12, 159), hover_color=(255, 255, 255)).draw(self.screen)

      for text_button in self.text_button_list:
          text_button.draw(self.screen)
    
    def draw(self):
        self.screen.fill(self.background_color)
        for button in self.button_list:
            button.draw(self.screen)
        self.draw_labels()
        self.draw_Textbutton()

        pygame.display.flip()
    
    def run(self):
        self.playing = True

        self.drawInitalMenu()
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()


class HomeMenu:
    def __init__(self, setting_option):
        self.setting_option = setting_option
        self.width, self.height, self.board_width, self.board_height = self.get_setting_config(setting_option)
        self.background_color = (255,222,173)

        #pygame variables
        pygame.init()
        #screen to draw 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect the Dots - Group 1")
        self.clock = pygame.time.Clock()

        # self.init_all_sprites()
        self.button_list = []
        self.text_button_list = []
        self.init_all_buttons()
        self.init_all_text_buttons()

    def get_setting_config(self, setting_option):
        width = 900
        height = 600
        board_width = 500
        board_height = 500

        if(setting_option == 1):
            pass
        elif(setting_option == 2):
            pass
        elif(setting_option == 3):
            pass

        return width, height, board_width, board_height

    def drawInitalMenu(self):
            self.draw()
            
    def get_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        return x, y  

    def event(self):
        #check if user press the exit button on the top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:

                    for text_button in  self.text_button_list:
                        if text_button.click(self.get_mouse_pos())  == False:
                            continue

                        if text_button.getButtonText() == "PLAY GAME":
                            stageMenu = StageMenu(0)
                            stageMenu.run()
                        elif text_button.getButtonText() == "QUIT GAME":
                            self.playing = False
                            pygame.quit()
                            quit(0)

    def update(self):
        for text_button in self.text_button_list:
            text_button.hover(self.get_mouse_pos())

    def init_all_buttons(self):        
        self.button_list.append(Button(0, 0, "resources/images/Logo.png", "Logo", scaler=0.08))

    def init_all_text_buttons(self):
        self.text_button_list.append(TextButton(220, 434, 200, 125, "PLAY GAME", font_size = 45,color=(0, 0, 0), hover_color=(255, 255, 255)))
        self.text_button_list.append(TextButton(506, 434, 200, 125, "QUIT GAME", font_size = 45,color=(0, 0, 0), hover_color=(255, 255, 255)))
    
    def draw_labels(self):
        Label(600, 25, "NHÓM 1", font_size= 40, color = (0,0,0)).draw(self.screen)
        Label(450, 70, "Dương Đức Khải 21110775", font_size= 30, color = (0,0,0)).draw(self.screen)
        Label(450, 120, "Tô Đức AN 21110002", font_size= 30, color = (0,0,0)).draw(self.screen)
        Label(450, 170, "Trần Hữu Tuấn 21110810", font_size= 30, color = (0,0,0)).draw(self.screen)

        Label(110, 10, "Trường Đại Học", font_size= 15, color = (0,191,255)).draw(self.screen)
        Label(110, 30, "Sư Phạm Kỹ Thuật Thành Phố HCM", font_size= 20, color = (0,0,255)).draw(self.screen)
        Label(110, 60, "HCMC Univercity of Technology and Education", font_size= 10, color = (210,105,30)).draw(self.screen)

        Label(270, 331, "LINK GAME", font_size= 80, color = (0,0,0)).draw(self.screen)

        Label(20, 150, "Final Projects", font_size= 20, color = (65,105,225)).draw(self.screen)
        Label(30, 180, "Giảng Viên Hướng Dẫn", font_size= 30, color = (30,144,255)).draw(self.screen)
        Label(50, 230, "Hoàng Văn Dũng", font_size= 40, color = (0,0,255)).draw(self.screen)

    def draw_TextButton(self):
        for text_button in self.text_button_list:
            text_button.draw(self.screen)

    def draw(self):
        self.screen.fill(self.background_color)
        for button in self.button_list:
            button.draw(self.screen)
        self.draw_labels()
        self.draw_TextButton()

        pygame.display.flip()
    
    def run(self):
        self.playing = True
        
        self.drawInitalMenu()
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()
