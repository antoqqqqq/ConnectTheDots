# this file will create the game and run it
# don't code in this file yet!!
import pygame
from sprite import *

def draw(screen):
    background.draw(screen)
    sprite_1.draw(screen)
    label1.draw(screen)
    home_btn.draw(screen)

def logic():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run
            run = False
    
    if home_btn.isClicked():
        print("I am a fish")

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 880

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

game_paused = False
menu_state = "main"

label1 = Label(200, 200, "Connect the Dots", font_size=50, color=(206, 90, 103))
home_btn = Button(500, 600, 'resources/images/home_btn.png', 100, 400)
sprite_1 = Sprite(int(SCREEN_WIDTH/100), int(SCREEN_HEIGHT/100), 'resources/images/game-logo.png', int(SCREEN_WIDTH / 8), int(SCREEN_HEIGHT / 8))
background = Sprite(0, 0, 'resources/images/background.jpg', SCREEN_WIDTH, SCREEN_HEIGHT)

run = True

while run:
    screen.fill((255, 255, 255))
    draw(screen)
    logic()
    pygame.display.update()
pygame.quit()