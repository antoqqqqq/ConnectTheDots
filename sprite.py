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
        
class Sprite:
    def __init__(self, x, y, image_path, width, height):
        #load the image with pygame
        loaded_image = pygame.image.load(image_path).convert_alpha()
        #scale the image to the desired width and height
        self.image = pygame.transform.scale(loaded_image, (width, height))
        #x and y coordinates
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Button:
    #scale is the ratio we scale the width and height of the image
    #width and height are set to the image width, height
    def __init__(self, x, y, image_path, width, height):
        self.sprite = Sprite(x, y, image_path, width, height)
        #rect is used to check for collision with mouse cursor
        self.rect = self.sprite.image.get_rect()
        self.rect.topleft = (x, y)
        #record if the Button is being clicked
        self.clicked = False

    def draw(self, screen):
        self.sprite.draw(screen)

    def isClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if (pygame.mouse.get_pressed()[0] == 1 and self.clicked == False):
                self.clicked = True
                return True
            if(pygame.mouse.get_pressed()[0] == 0):
                self.clicked = False
        return False
            
