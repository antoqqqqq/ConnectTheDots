import pygame
from sprite import *
from business import *
from enumaration import *

class GameMenu:
    def __init__(self, setting_option, stage_number):
        self.setting_option = setting_option
        self.width, self.height, self.board_width, self.board_height = self.get_setting_config(setting_option)
        self.background_color = (22, 72, 99)
        self.stage_number = stage_number
        self.board_length = 500
        self.board = self.create_game(stage_number)
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
        self.sprite_list.add(Sprite(0, 0, "resources/images/background.jpg", self.width, self.height))
        self.sprite_list.add(Sprite(37, 37, "resources/images/green_box.png", 225, 187))
        self.sprite_list.add(Sprite(56, 243, "resources/images/pink_box.png", 187, 56))
        self.sprite_list.add(Sprite(56, 318, "resources/images/pink_box.png", 187, 56))
        self.sprite_list.add(Sprite(56, 393, "resources/images/pink_box.png", 187, 56))
        
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

    def get_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        return x, y
    
    def create_game(self, stage_number):
        n_tiles_perRow = 6
        tile_length = self.board_length / n_tiles_perRow
        dot_radius = int(tile_length * 0.3)
        tiles_with_dot = []
        tiles_with_dot.append(((0,0), (1,2), Color.RED.value))
        tiles_with_dot.append(((2,0), (2,2), Color.YELLOW.value))

        new_board = Board(n_tiles_perRow, tile_length, dot_radius, tiles_with_dot)
        new_board.setTileLineDir(0, 0, Direction.Right.value)
        new_board.setTileLineDir(0, 1, Direction.Down.value, Direction.Left.value)
        new_board.setTileLineDir(1, 1, Direction.Right.value, Direction.Up.value)
        new_board.setTileLineDir(1, 2, Direction.Left.value)

        new_board.setTileLineColor(0, 0, Color.RED.value)
        new_board.setTileLineColor(0, 1, Color.RED.value)
        new_board.setTileLineColor(1, 1, Color.RED.value)
        new_board.setTileLineColor(1, 2, Color.RED.value)

        new_board.setTileLineDir(2, 0, Direction.Right.value)
        new_board.setTileLineDir(2, 1, Direction.Right.value, Direction.Left.value)
        new_board.setTileLineDir(2, 2, Direction.Left.value)

        new_board.setTileLineColor(2, 0, Color.YELLOW.value) 
        new_board.setTileLineColor(2, 1, Color.YELLOW.value) 
        new_board.setTileLineColor(2, 2, Color.YELLOW.value) 
        return new_board

    def save_score(self, file_path):
        pass

    def get_score(self, file_path):
        pass

    def event(self):
        #check if user press the exit button on the top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.quit()
                quit(0)

    def update(self):
        pass
    
    def draw_board(self):
        x_start, y_start = 350, 37
        board_length = self.board_length
        tile_length = self.board.tile_length
        border_width = 5
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
                        
                    
                    rect_x = x + (exit_dir[0] * tile_length)
                    rect_y = y + (exit_dir[1] * tile_length)
                    rect_width = rect_length
                    rect_height = rect_length

                    if(exit_dir == Direction.Up.value or exit_dir == Direction.Down.value):
                        rect_height += 5
                    elif(exit_dir == Direction.Left.value or exit_dir == Direction.Right.value):
                        rect_width += 5
                    pygame.draw.rect(self.screen, line_color, [rect_x, rect_y, rect_width, rect_height])
            
                


    def draw(self):
        self.screen.fill(self.background_color)
        self.sprite_list.draw(self.screen)
        for button in self.button_list:
            button.draw(self.screen)
        self.draw_board()
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
        self.background_color = (225, 255, 255)

        #pygame variables
        pygame.init()
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
        #self.button_list.append(Button(75, 487, "resources/images/level_1.png", "Home", 100, 60))
        #self.button_list.append(Button(39,157,"resources/images/Beginer.jpg","Home",100,60))
        #self.button_list.append(Button(39,298,"resources/images/Beginer.jpg","Home",100,60))
        #self.button_list.append(Button(39,452,"resources/images/Beginer.jpg","Home",100,60))
        self.button_list.append(Button(91,  240, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(228, 240, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(365, 240, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(502, 240, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(639, 240, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(776, 240, "resources/images/level_1.png", "Home", 54, 37))
    
        self.button_list.append(Button(91,  388, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(228, 388, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(365, 388, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(502, 388, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(639, 388, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(776, 388, "resources/images/level_1.png", "Home", 54, 37))

        self.button_list.append(Button(91, 518, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(228, 518, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(365, 518, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(502, 518, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(639, 518, "resources/images/level_1.png", "Home", 54, 37))
        self.button_list.append(Button(776, 518, "resources/images/level_1.png", "Home", 54, 37))
        pass
    def init_all_sprites(self):
        self.sprite_list = pygame.sprite.Group()
        self.sprite_list.add(Sprite(39, 157, "resources/images/Beginer.jpg", scaler=0.5))
        self.sprite_list.add(Sprite(39, 298, "resources/images/Beginer.jpg", 100, 60))
        self.sprite_list.add(Sprite(39, 452, "resources/images/Beginer.jpg", 100, 60))
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
        Label(250, 59, "Stage Menu", font_size= 80, color = (255, 145, 48)).draw(self.screen)

    def draw(self):
        self.screen.fill(self.background_color)
        self.draw_labels()
        for button in self.button_list:
            button.draw(self.screen)
        self.sprite_list.draw(self.screen)

        pygame.display.flip()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()
