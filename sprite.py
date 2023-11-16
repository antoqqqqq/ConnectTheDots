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
        
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, width = None, height = None, scaler = 1):
        pygame.sprite.Sprite.__init__(self)
        #load the image with pygame
        loaded_image = pygame.image.load(image_path).convert_alpha()
        #scale the image to the desired width and height
        img_width = width
        img_height = height
        if(width == None or height == None):
            img_width = loaded_image.get_width()
            img_height = loaded_image.get_height()
        self.image = pygame.transform.scale(loaded_image, (img_width * scaler, img_height * scaler))
        #x and y coordinates
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # def draw(self, screen):
    #     screen.blit(self.image, (self.x, self.y))

class Button:
    #scale is the ratio we scale the width and height of the image
    #width and height are set to the image width, height
    def __init__(self, x, y, image_path, btn_name, width = None, height = None, scaler = 1):
        #load the image with pygame
        loaded_image = pygame.image.load(image_path).convert_alpha()
        #scale the image to the desired width and height
        img_width = width
        img_height = height
        if(width == None or height == None):
            img_width = loaded_image.get_width()
            img_height = loaded_image.get_height()
            
        self.image = pygame.transform.scale(loaded_image, (img_width * scaler, img_height  * scaler))
        #rect is used to check for collision with mouse cursor
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.name = btn_name
        #record if the Button is being clicked
        # self.clicked = False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def isClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if (pygame.mouse.get_pressed()[0]):
                return True
        return False
    
    def getName(self):
        return self.name


class TextButton:
    def __init__(self, x, y, width, height, text, font_size=30, color=(0,128,0), hover_color=(255,255,255), text_color=(255,255,255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False
        self.font = pygame.font.Font(None, self.font_size)

    def draw(self, screen):
        text_surface = self.font.render(self.text, 1, self.text_color)

        if self.is_hovered:
            pygame.draw.rect(screen, self.hover_color, (self.x, self.y, self.width, self.height))
            text_surface = self.font.render(self.text, 1, self.color)
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        # Tính toán vị trí để căn giữa văn bản trong hình chữ nhật
        text_x = self.x + (self.width - text_surface.get_width()) // 2
        text_y = self.y + (self.height - text_surface.get_height()) // 2

        screen.blit(text_surface, (text_x, text_y))

    def click(self, pos):
        x, y = pos
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height

    def hover(self, pos):
        x, y = pos
        self.is_hovered = self.x < x < self.x + self.width and self.y < y < self.y + self.height

    def getButtonText(self):
        return self.text