import pygame, sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('Jömpnrän')
window_size = (1200, 900)
screen = pygame.display.set_mode(window_size)

gravity = 0.5
player_image = pygame.image.load('evoli.png')

player_location = [50, 50]

player_speed = 10

moving_right = False
moving_left = False

player_y_momentum = 0

player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(500, 400, 100, 50)

def player_movement():
    global moving_right
    global moving_left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            moving_right = True
        if event.key == pygame.K_a:
            moving_left = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            moving_right = False
        if event.key == pygame.K_a:
            moving_left = False

def player_x_movement_exe():
    if moving_right == True:
        player_location[0] += player_speed
    if moving_left == True:
        player_location[0] -= player_speed

def player_y_movement():
    global player_y_momentum
    if player_location[1] >= window_size[1] - player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += gravity
    player_location[1] += player_y_momentum

def player_X_boarders():
    global moving_right
    global moving_left
    if player_location[0] <= -29:
        moving_left = False
    if player_location[0] >= window_size[0] - 219:
        moving_right = False

def player_collision():
    global player_rect
    global test_rect
    global player_y_momentum
    player_rect.x = player_location[0]
    player_rect.y = player_location[1]
    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
        #player_y_momentum = -gravity
    else:
        pygame.draw.rect(screen, (0, 0, 0), test_rect)




while True: #Game loop
    screen.fill((200, 200, 69))
    #Closing the game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        player_movement()
    player_X_boarders()
    player_x_movement_exe()
    player_y_movement()
    player_collision()

    screen.blit(player_image, player_location)
    pygame.display.update()
    clock.tick(60)
