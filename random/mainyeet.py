import pygame, sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('Jömpnrän')
window_size = (1200, 900)
screen = pygame.display.set_mode(window_size)

player_image = pygame.image.load('shrek.png')
player_location = [50, 50]
player_speed = 42
moving_right = False
moving_left = False


def player_movement():
    global moving_right
    global moving_left
    if event.type == KEYDOWN:
        if event.key == pygame.K_d:
            moving_right = True
        if event.key == pygame.K_a:
            moving_left = True
    if event.type == KEYUP:
        if event.key == pygame.K_d:
            moving_right = False
        if event.key == pygame.K_a:
            moving_left = False
    if moving_right == True:
        player_location[0] += player_speed
    if moving_left == True:
        player_location[0] -= player_speed


while True: #Game loop
    #Closing the game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    player_movement()
    screen.blit(player_image, player_location)

    pygame.display.update()
    clock.tick(60)






