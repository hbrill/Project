import pygame #import the pygame module, which we will need to write the mini game 
from pygame.locals import *
import time


pygame.init() # This line will create the window where our game will display
### The next three lines will set the dimensions for the screen, being 800x800 for width and height ###
display_width = 800
display_height = 800
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Get the criminal down!") # This will be the tile of the game, what shows next to the game icon
clock = pygame.time.Clock() # The clock variable will be used to determine the FPS for our game, basically how smooth or game is going to run
thief_width = 73
### The next three lines will be used to set the colors, based on RGB ###
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bullet_width = 31
screen.fill(white) # This will fill the color of our screen with white
cop_width = 125
### We are now creating our images, which will be used to represent our characters in the game ###
imgCop = pygame.image.load("sss.png")
imgThief = pygame.image.load("thief.png")
imgShooter = pygame.image.load("bulletup.png")
gameOver = False
bulletSpeed = 0
newIcon = pygame.image.load("officer4.jpg") # This is used to change the default pygame icon to something more related to our game
pygame.display.set_icon(newIcon)

### Now we will create our functions, starting with the basic cop, thief and bullet(shoot)
# Each of those has x and y positional values, though they have different variable names to avoid confussion
### We use screen.blit to draw our characters in our canvas
def cop(x,y):
    screen.blit(imgCop, (x,y))

def thief(a,b):
    screen.blit(imgThief, (a,b))
    
def shoot(w,z):
    screen.blit(imgShooter, (w,z))

### The next function will be used for the text that will pop up once our character gets the opponent    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

### The next two functions will be used to draw squares around the bullet and the thief.
# This will be used to determine any sort of collision. I've colored the rectangles white so they can blend in with the background
### That way, we will also determine when the bullet "hits" the opponent
def squareOne(rectW, rectZ, oneWidth, oneHeight):
    pygame.draw.rect(screen, white,(rectW,rectZ,oneWidth,oneHeight))

def squareTwo(rectA, rectB, twoWidth, twoHeight):
    pygame.draw.rect(screen, white,(rectA,rectB,twoWidth,twoHeight))

### Using the text function that we created before for our text, we create another function that will actually draw the text onscreen
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',55)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

### This function will be called if the bullet "hits" the opponent
def fall():
    message_display('YOU GOT HIM!')

### Finally, we create our game_loop function, where all of our variables will be declared and all of our code will run
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.7)
    a = (display_width * 0.45) #360
    b = (display_height * 0.15) #120
    w = (display_width * 0.45)
    z = (display_height *0.7)
    rectW = (display_width * 0.45)
    rectZ = (display_height *0.7)
    rectA = (display_width * 0.48)
    rectB = (display_height * 0.15)
    x_change = 0
    y_change = 0
    a_change = 0
    z_change = 0
    w_change = 0
    oneWidth = 15
    oneHeight = 15
    twoWidth = 70
    twoHeight = 90
    rectA_change = 0
    rectZ_change = 0
    rectW_change = 0
    copWidth = twoWidth
    bulletCount = 5
    while not gameOver:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                        #a_change = -7
                        #rectA_change = -7
                        w_change = -5
                        rectW_change = -5
                    if event.key == pygame.K_RIGHT:
                        x_change = 5
                       # a_change = 7
                        #rectA_change = 7
                        w_change = 5
                        rectW_change = 5
                    if event.key == pygame.K_SPACE:
                        z_change = -5
                        rectZ_change = -5
                        if z <= b:
                           z = y
                           rectZ = z
          
                        

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                        w_change = 0
                        rectW_change = 0
                       
                    

                      

        x += x_change
        a += a_change
        z += z_change
        w += w_change
        rectZ += rectZ_change
        rectA += rectA_change
        rectW += rectW_change
        screen.fill(white)
        squareOne(rectW, rectZ, oneWidth, oneHeight)
        shoot(w,z)
        cop(x,y)
        squareTwo(rectA, rectB, twoWidth, twoHeight)
        thief(a,b)
        a_change = 7
        rectA_change = 7
        if a > 400 and rectA > 800:
            a = 10
            rectA = 10
        if rectZ > rectB and rectZ < rectB+twoHeight:
            if rectW > rectA and rectW < rectA+twoWidth:
                fall()
        

         

        pygame.display.update()
        clock.tick(60)

game_loop()
quit()
