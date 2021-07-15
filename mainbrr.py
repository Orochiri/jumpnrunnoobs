import pygame, sys


pygame.init()

screen_height = 900
screen_width = 1400
screen = pygame.display.set_mode([screen_width, screen_height])

shrekimg = pygame.image.load('shrek.png')

fps = pygame.time.Clock()

width = 690
height = 420
x_shrek = 300
y_shrek = 300
speed = 10
speed_shrek_x_p = 0
speed_shrek_y_p = 0
speed_shrek_x_n = 0
speed_shrek_y_n = 0


run = True
while run: #main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


        #button mekäniks
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed_shrek_y_n = -speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                speed_shrek_y_n = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                speed_shrek_y_p = speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                speed_shrek_y_p = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                speed_shrek_x_p = speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                speed_shrek_x_p = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed_shrek_x_n = -speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                speed_shrek_x_n = 0

    #borders
    if x_shrek >= screen_width - width:
        speed_shrek_x_p = 0
    if x_shrek <= 0:
        speed_shrek_x_n = 0
    if y_shrek <= 0:
        speed_shrek_y_n = 0
    if y_shrek >= screen_height - height:
        speed_shrek_y_p = 0

    #shrek movement
    speed_shrek_x = speed_shrek_x_p + speed_shrek_x_n
    speed_shrek_y = speed_shrek_y_p + speed_shrek_y_n

    x_shrek += speed_shrek_x
    y_shrek += speed_shrek_y


    #draw
    screen.fill((69,69,69))
    'screen.blit(shrekimg, (x_shrek,y_shrek))' #not using it because it's harder
    pygame.draw.rect(screen, (230, 230, 250), (x_shrek, y_shrek, width, height))
    pygame.display.update()
    fps.tick(60)