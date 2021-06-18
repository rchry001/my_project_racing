
import pygame


pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
PlayerImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(PlayerImg, (x,y))

x =  (display_width * 0.4)
y = (display_height * 0.8)
x_change = 0
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        #####################################
    ##################
    x += x_change
    ##################
    gameDisplay.fill(white)
    car(x,y)

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()