import pygame

class Label:
    # x and y are row and col coordinates
    # text is the display text content on the screen
    # default font is Consolas
    # color takes in (r, g b) value
    def __init__(self, x, y, text, font='Consolas', font_size=30, color=(252, 245, 237)):
        self.x, self.y = x, y
        self.text = text
        self.font = font
        self.font_size = font_size
        self.color = color

    #draw the label on a given screen
    def draw(self, screen):
        font = pygame.font.SysFont(self.font, self.font_size)

        #Antialias - drawing with smooth edges
        text = font.render(self.text, True, self.color)
        screen.blit(text, (self.x, self.y))