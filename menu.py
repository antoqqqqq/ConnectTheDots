import pygame
from sprite import *
from business import *

class GameMenu:
    def __init__(self, setting_option, stage_number):
        self.setting_option = setting_option
        self.width, self.height, self.board_width, self.board_height = self.get_setting_config(setting_option)
        self.background_color = (22, 72, 99)
        self.stage_number = stage_number
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
        tiles_with_dot = []
        tiles_with_dot.append(((0,0), (1,2), "RED"))
        tiles_with_dot.append(((2,0), (2,2), "YELLOW"))
        new_board = Board(3,3,25,10, tiles_with_dot)
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
        pass

    def draw(self):
        self.screen.fill(self.background_color)
        self.sprite_list.draw(self.screen)
        for button in self.button_list:
            button.draw(self.screen)
        pygame.display.flip()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()

game = GameMenu(0, 0)
print("")
