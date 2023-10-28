# this file will create the game and run it
# don't code in this file yet!!
import pygame
from sprite import Label

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

game_paused = False
menu_state = "main"

label1 = Label(200, 200, "Connect the Dots", font_size=50, color=(206, 90, 103))
run = True

while run:
    screen.fill((52, 78, 91))
    label1.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()