
import pygame
import time
import random
pygame.init()

display_width = 900
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Speedracer Game')

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,255)

car_width = 73
car_height = 82
#pixAr = pygame.PixelArray(gameDisplay)
#pixAr[5][10] = green

clock = pygame.time.Clock()
crashed = False
PlayerImg = pygame.image.load('racecar.png')
ZombieImg = pygame.image.load('zombie danger.png')

def dangers_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

####### Defining the objects the player must avoid
def dangers(dangers_x, dangers_y, dangers_w, dangers_h, zombie):
    pygame.draw.rect(gameDisplay, zombie, [dangers_x, dangers_y, dangers_w, dangers_h])
#######

###### Defining the zombie image to include as dangers
def zombie(x,y):
    gameDisplay.blit(ZombieImg, (x,y))

###### Defining the vehicle the player controls
def car(x,y):
    gameDisplay.blit(PlayerImg, (x,y))

#Defining the text objects
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash(): #Need to improve crash design - Allow player to try again after crash
    message_display('You Crashed! Game Over....')

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        

        #button("Play Again",150,450,100,50,green,bright_green,game_loop)
        #button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("The Speedracer!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        if 200+100 > mouse[0] > 200 and 700+50 > mouse[1] > 700:
            pygame.draw.rect(gameDisplay, bright_green,(200,700,100,50))
        else:
            pygame.draw.rect(gameDisplay, green,(200,700,100,50))
        #to create buttons interactions during intro screen
        if 600+100 > mouse[0] > 600 and 700+50 > mouse[1] > 700:
            pygame.draw.rect(gameDisplay, bright_red,(600,700,100,50))
        else:
            pygame.draw.rect(gameDisplay, red,(600,700,100,50))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("RACE!", smallText)
        textRect.center = ( (200+(100/2)), (700+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("QUIT...", smallText)
        textRect.center = ( (600+(100/2)), (700+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(10)

game_intro()

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        
        #button("Continue",150,450,100,50,green,bright_green,unpause)
        #button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)



x = (display_width * 0.4)
y = (display_height * 0.8)
x_change = 0
y_change = 0
car_speed = 1

thing_startx = random.randrange(0, display_width)
thing_starty = -600
thing_speed = 4
thing_width = 100
thing_height = 100

dangerCount = 1
dodged = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #####################################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -7
            elif event.key == pygame.K_RIGHT:
                x_change = 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = 2
            elif event.key == pygame.K_DOWN:
                y_change = -2
        if event.type == pygame.KEYDOWN: ### This line assigns the pause function to the key "p"
            if event.key == pygame.K_p:
                pause = True
                paused()
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
    dangers(thing_startx, thing_starty, thing_width, thing_height, red)
    thing_starty += thing_speed
    car(x,y)
    dangers_dodged(dodged)
    #zombie(x,y)
    
    ##### To Define the boundaries where the car and go within the screen
    if x > display_width - car_width or x < 0:
        crash()
    if y > display_height - car_height or y < 0:
        crash()

    if thing_starty > display_height:
        thing_starty = 0 - thing_height
        thing_startx = random.randrange(0,display_width)
        dodged += 1
        thing_speed += .2
        thing_width += (dodged * .9)

    if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()