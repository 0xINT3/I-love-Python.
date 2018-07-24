import pygame
import time
import random

display_width = 800
display_height = 600

black = (0,0,0)         #RGB Colour System (Red-Green-Blue)
white = (255,255,255)
red = (255,0,0)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Avoid Hurdles')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
def dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text,(0,0))

def blocks(x, y, width, height, colour):
    pygame.draw.rect(gameDisplay, colour, [x, y, width, height])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display("OOPS! You Crashed")

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0

    block_x = random.randrange(0, display_width)
    block_y = 0
    wid = 80
    hei = 80
    speed = 5
    col = red
    gameExit = False
    count = 0
    # blocks(x, y, widht, height, colour):

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    if event.key == pygame.K_UP:
                        y_change = -5
                    if event.key == pygame.K_DOWN:
                        y_change = 5
                    if event.key == pygame.K_RIGHT:
                        x_change = 5

            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)

        blocks(block_x, block_y, wid, hei, col)
        block_y += speed
        car(x,y)
        dodged(count)

        if x == display_width - 80 or x < 0:
            crash()

        if block_y > display_height:
            block_x = random.randrange(0 + wid, display_width - wid)
            block_y = 0 - hei
            count += 1
            speed += 1
            c_one = random.randint(0, 255)
            c_second = random.randint(0, 255)
            c_third = random.randint(0, 255)
            col = (c_one, c_second, c_third)

        if y < block_y + hei:
            if x > block_x and x < block_x + wid or x+ 100 > block_x and x + 100 < block_x + wid:
                crash()
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
