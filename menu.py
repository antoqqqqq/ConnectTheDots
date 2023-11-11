import pygame
from data import *
from sprite import *
from business import *

class GameMenu:
    def __init__(self, setting_option, stage_number):
        self.setting_option = setting_option
        self.width, self.height, self.board_length = self.get_setting_config(setting_option)
        self.background_color = (77, 77, 77)
        self.stage_number = stage_number
        self.board_topLeft = [350, 37]
        self.board_border = 5
        self.board = self.create_game(stage_number)
        self.gameClear = False

        #variables for processing user mouse inputs on board    
        self.is_connecting_dot = False
        self.previous_passed_tile_rc = None
        self.current_held_tile_rc = None
        self.current_held_color = None
        self.start_tile_rc = None

        #pygame variables
        pygame.init()
        #screen to draw 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect the Dots")
        self.clock = pygame.time.Clock()
        self.init_all_sprites()
        self.button_list = []
        self.init_all_buttons()

    def init_all_buttons(self):        
        self.button_list.append(Button(75, 487, "resources/images/home_btn_pink.png", "Home", 56, 56))
        self.button_list.append(Button(168, 487, "resources/images/reset_btn.png", "Reset", 56, 56))
    def init_all_sprites(self):
        self.sprite_list = pygame.sprite.Group()
        self.sprite_list.add(Sprite(0, 0, "resources/images/background1.jpg", self.width, self.height))
        self.sprite_list.add(Sprite(37, 37, "resources/images/green_box.png", 225, 187))
        self.sprite_list.add(Sprite(56, 243, "resources/images/pink_box.png", 187, 56))
        self.sprite_list.add(Sprite(56, 318, "resources/images/red_box.png", 187, 56))
        self.sprite_list.add(Sprite(56, 393, "resources/images/blue_box.png", 187, 56))
        
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

    def get_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        return x, y
    
    def create_game(self, stage_number):
        stage_number=1
        #info_stage=[int(stage),int(n_tiles_perRow),int(number_node),tiles_with_dot]
        info_stage=read_stage('resources/level/level'+str(stage_number)+'.txt')
        n_tiles_perRow=info_stage[1]
        tile_length = self.board_length / n_tiles_perRow
        dot_radius = int(tile_length * 0.3)
        tiles_with_dot=info_stage[3]

        #tiles_with_dot = []
        #tiles_with_dot.append(((0,0), (1,2), Color.RED.value))
        #tiles_with_dot.append(((2,0), (2,2), Color.YELLOW.value))
        #tiles_with_dot.append(((4,4), (0,4), Color.BLUE.value))


        new_board = Board(n_tiles_perRow, tile_length, dot_radius, tiles_with_dot)
        # new_board.setTileLineDir(0, 0, Direction.Right.value)
        # new_board.setTileLineDir(0, 1, Direction.Down.value, Direction.Left.value)
        # new_board.setTileLineDir(1, 1, Direction.Right.value, Direction.Up.value)
        # new_board.setTileLineDir(1, 2, Direction.Left.value)
        # new_board.setTileLineColor(0, 0, Color.RED.value)
        # new_board.setTileLineColor(0, 1, Color.RED.value)
        # new_board.setTileLineColor(1, 1, Color.RED.value)
        # new_board.setTileLineColor(1, 2, Color.RED.value)
        # new_board.setTileLineDir(2, 0, Direction.Right.value)
        # new_board.setTileLineDir(2, 1, Direction.Right.value, Direction.Left.value)
        # new_board.setTileLineDir(2, 2, Direction.Left.value)
        # new_board.setTileLineColor(2, 0, Color.YELLOW.value) 
        # new_board.setTileLineColor(2, 1, Color.YELLOW.value) 
        # new_board.setTileLineColor(2, 2, Color.YELLOW.value) 
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
                self.num_moves = data[i][1]
                self.num_turn  = data[i][2]
                self.num_time  = data[i][3]
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
                if(self.is_connecting_dot == False):
                    if self.cursor_in_Board(mouse_x, mouse_y):
                        r, c = self.get_Tile_pos(mouse_x, mouse_y)
                        if(self.board.getTileDot(r, c) != None):
                            self.is_connecting_dot = True
                            self.current_held_color = self.board.getTileDot(r, c).color  
                            self.start_tile_rc = [r, c]                   
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
        if self.board.IsGameClear():
            self.gameClear = True

        if self.is_connecting_dot:
            mouse_x, mouse_y = self.get_mouse_pos()
            pressed_Tile_pos = self.get_Tile_pos(mouse_x, mouse_y)
            self.processPressedTile(pressed_Tile_pos)
        else:
            self.current_held_tile_rc = None
            self.previous_passed_tile_rc = None
            self.current_held_color = None
            self.start_tile_rc = None
   
    def draw_board(self):
        x_start, y_start = self.board_topLeft[0], self.board_topLeft[1]
        board_length = self.board_length
        tile_length = self.board.tile_length
        border_width = self.board_border
        rect_length = tile_length * 0.5

        #draw the the Board's top and left sides
        pygame.draw.line(self.screen, Color.BLACK.value, (x_start, y_start), (x_start + board_length, y_start), width=border_width)
        pygame.draw.line(self.screen, Color.BLACK.value, (x_start, y_start), (x_start, y_start + board_length), width=border_width)

        y = y_start
        
        for r in range(self.board.n_tiles_perRow):
            x = x_start
            y += tile_length
            for c in range(self.board.n_tiles_perRow):
                x += tile_length
                #draw Tiles right and bottom sides
                pygame.draw.line(self.screen, Color.BLACK.value, (x, y - tile_length), (x, y), width=border_width)
                pygame.draw.line(self.screen, Color.BLACK.value, (x - tile_length, y), (x, y), width=border_width)

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
                        if(exit_dir == Direction.Down.value):
                            rect_height += 5
                        if(exit_dir == Direction.Left.value):
                            rect_x -= 5
                        if(exit_dir == Direction.Right.value):
                            rect_width += 5
                        pygame.draw.rect(self.screen, line_color, [rect_x, rect_y, rect_width, rect_height])
        
    def draw(self):
        self.screen.fill(self.background_color)
        self.sprite_list.draw(self.screen)
        for button in self.button_list:
            button.draw(self.screen)
        self.draw_board()

        if self.gameClear:
            Label(200, 200, "Congratulation").draw(self.screen)

        pygame.display.flip()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()

class StageMenu:
    def __init__(self, setting_option):
        self.setting_option = setting_option
        self.width, self.height, self.board_width, self.board_height = self.get_setting_config(setting_option)
        self.background_color = (102,205,170)

        #pygame variables
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect the Dots")
        #screen to draw 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect the Dots")
        self.clock = pygame.time.Clock()

        self.init_all_sprites()
        self.button_list = []
        self.init_all_buttons()

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
        self.button_list.append(Button(102, 172, "resources/images/Level_01.png", "Home", scaler = 0.3))
        self.button_list.append(Button(247, 172, "resources/images/Level_02.png", "Home", scaler = 0.3))
        self.button_list.append(Button(403, 172, "resources/images/Level_03.png", "Home", scaler = 0.3))
        self.button_list.append(Button(559, 172, "resources/images/Level_04.png", "Home", scaler = 0.3))
        self.button_list.append(Button(715, 172, "resources/images/Level_05.png", "Home", scaler = 0.3))

        self.button_list.append(Button(102, 344, "resources/images/Level_01.png", "Home", scaler =0.3))
        self.button_list.append(Button(247, 344, "resources/images/Level_02.png", "Home", scaler = 0.3))
        self.button_list.append(Button(403, 344, "resources/images/Level_03.png", "Home", scaler = 0.3))
        self.button_list.append(Button(559, 344, "resources/images/Level_04.png", "Home", scaler = 0.3))
        self.button_list.append(Button(715, 344, "resources/images/Level_05.png", "Home", scaler = 0.3))

        self.button_list.append(Button(102, 516, "resources/images/Level_01.png", "Home", scaler = 0.3))
        self.button_list.append(Button(247, 516, "resources/images/Level_02.png", "Home", scaler = 0.3))
        self.button_list.append(Button(403, 516, "resources/images/Level_03.png", "Home", scaler = 0.3))
        self.button_list.append(Button(559, 516, "resources/images/Level_04.png", "Home", scaler = 0.3))
        self.button_list.append(Button(715, 516, "resources/images/Level_05.png", "Home", scaler = 0.3))

    def init_all_sprites(self):
        self.sprite_list = pygame.sprite.Group()
        self.sprite_list.add(Sprite(0, 0, "resources/images/background5.jpg", self.width, self.height))
        self.sprite_list.add(Sprite(32, 85, "resources/images/BASIC0.png", scaler=0.5))
        self.sprite_list.add(Sprite(39, 258, "resources/images/SPECIAL0.png", scaler=0.5))
        self.sprite_list.add(Sprite(39, 430, "resources/images/DAILY0.png", scaler=0.5))

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
                clicked_btn_name = ""
                for button in self.button_list:
                    if(button.isClicked()):
                        clicked_btn_name = button.getName()
                
                if(clicked_btn_name == "Home"):
                    stageMenu = StageMenu(0)
                    StageMenu.run()


    def update(self):
        pass
    def draw_labels(self):
        Label(250, 0, "Stage Menu", font_size= 80, color = (51, 51, 255)).draw(self.screen)

    def draw(self):
        self.screen.fill(self.background_color)
        #self.draw_labels()
        self.sprite_list.draw(self.screen)
        for button in self.button_list:
            button.draw(self.screen)
        #self.sprite_list.draw(self.screen)
        self.draw_labels()

        pygame.display.flip()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()


class HomeMenu:
    def __init__(self, setting_option):
        self.setting_option = setting_option
        self.width, self.height, self.board_width, self.board_height = self.get_setting_config(setting_option)
        self.background_color = (255,255,255)

        #pygame variables
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect the Dots")
        #screen to draw 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect the Dots")
        self.clock = pygame.time.Clock()

        self.init_all_sprites()
        self.button_list = []
        self.init_all_buttons()

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
          self.button_list.append(Button(150, 450, "resources/images/BASIC0.png", "Home", scaler = 1))
          self.button_list.append(Button(380, 450, "resources/images/SPECIAL0.png", "Home", scaler = 1))
          self.button_list.append(Button(600, 450, "resources/images/DAILY0.png", "Home", scaler = 1))
          self.button_list.append(Button(350, 200, "resources/images/Level_04.png", "Home", scaler = 1))

    def init_all_sprites(self):
        self.sprite_list = pygame.sprite.Group()
        self.sprite_list.add(Sprite(0, 0, "resources/images/background5.jpg", self.width, self.height))

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
                clicked_btn_name = ""
                for button in self.button_list:
                    if(button.isClicked()):
                        clicked_btn_name = button.getName()
                
                if(clicked_btn_name == "Home"):
                    stageMenu = StageMenu(0)
                    StageMenu.run()


    def update(self):
        pass
    def draw_labels(self):
        Label(250, 40, "L", font_size= 150, color = (255,0,0)).draw(self.screen)
        Label(350, 40, "I", font_size= 150, color = (0,255,0)).draw(self.screen)
        Label(450, 40, "N", font_size= 150, color = (255,255,0)).draw(self.screen)
        Label(550, 40, "K", font_size= 150, color = (0,0,255)).draw(self.screen)
        Label(250, 400, "CHOOSE CATEGORY AND LEVEL", font_size= 30, color = (255,0,0)).draw(self.screen)

    def draw(self):
        self.screen.fill(self.background_color)
        self.draw_labels()
        self.sprite_list.draw(self.screen)
        for button in self.button_list:
            button.draw(self.screen)
        self.draw_labels()

        pygame.display.flip()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()
# class Button:
#      def __init__(self, color, x,y,width,height, text=''):
#         self.color = color
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.text = text