import pygame

class GameMenu:
    def __init__(self, setting_option, stage_number):
        self.setting_option = setting_option
        self.width, self.height, self.board_width, self.board_height = self.get_setting_config(setting_option)
        self.background_color = (22, 72, 99)
        self.stage_number = stage_number
        #self.board = self.create_game(stage_number)
        self.button_list = []
        self.sprite_list = []

        #pygame variables
        pygame.init()
        #screen to draw 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect the Dots")
        self.clock = pygame.time.Clock()

    def get_setting_config(self, setting_option):
        width = 1200
        height = 800
        board_width = 500
        board_height = 500

        if(setting_option == 1):
            pass
        elif(setting_option == 2):
            pass
        elif(setting_option == 3):
            pass

        return width, height, board_width, board_height

    def draw(self):
        pass

    def get_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        return x, y
    
    def create_game(self, stage_number):
        pass

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

    def draw(self):
        self.screen.fill(self.background_color)
        pygame.display.flip()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()

gameMenu = GameMenu(0, 0)
gameMenu.run()
