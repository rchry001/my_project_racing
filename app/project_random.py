
import pygame
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Speedracer')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73
car_height = 82


clock = pygame.time.Clock()
crashed = False
PlayerImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(PlayerImg, (x,y))

#Defining the text objects
def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed! Game Over....')


x = (display_width * 0.4)
y = (display_height * 0.8)
x_change = 0
y_change = 0
car_speed = 1


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #####################################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = 5
            elif event.key == pygame.K_DOWN:
                y_change = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 0
        #####################################
    ##################
    x += x_change
    y += y_change
    ##################
    gameDisplay.fill(white)
    car(x,y)

    if x > display_width - car_width or x < 0:
        crash()
    if y > display_height - car_height or y < 0:
        crash()            
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()