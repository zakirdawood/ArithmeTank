import pygame
import random
import ctypes
import os
import sys
from subprocess import call
from pygame.constants import MOUSEBUTTONDOWN

pygame.init()

screen = pygame.display.set_mode((900,600))

pygame.display.set_caption("ArithmeTank")
icon = pygame.image.load("tankIcon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

counter, textTime = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

#Background Image
background_image = pygame.image.load("background.jpg").convert()
background_image = pygame.transform.scale(background_image, (900, 600))

#player image icon
playerImage = pygame.image.load("tank.png")
playerImage = pygame.transform.scale(playerImage, (70, 80))
playerX = 540
playerY = 480

#enemy tank
enemyImage = pygame.image.load("enemytank.png")
enemyImage = pygame.transform.scale(enemyImage, (70, 80))
#player missle
missleImage = pygame.image.load("cannonball.png")
missleX = 0
missleY = playerY 
missle = False
bullet_state = "ready"


#function to display player icon
def player():
    screen.blit(playerImage, (playerX, playerY))

def enemyLocation():
    screen.blit(enemyImage, (20, 70))
    screen.blit(enemyImage, (280, 70))
    screen.blit(enemyImage, (540, 70))
    screen.blit(enemyImage, (800, 70))
    

#function to display random sum/product
def randQUestionAnswer():
    screen.blit(text, textRect)

def randQUestionAnswerTwo(one, two):
    screen.blit(one, two)

def moveTankLeft():
    global playerX
    if playerX == 20:
        playerX = playerX
    else:
        playerX -= 260

def moveTankRight():
    global playerX
    if playerX == 800:
        playerX = playerX
    else:
        playerX += 260

def appearMissle(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(missleImage, (x + 15, y - 100))

def shootMissle():
    global missleY
    missleY = playerY


#Randomizing Questions
def genAdd():
    n = random.randint(0, 20)
    n2 = random.randint(0, 20)
    stringAdd = str(n) + " + " + str(n2)
    questionArr.append(stringAdd)
    return n + n2

def genSub():
    n = random.randint(0, 20)
    n2 = random.randint(0, 20)
    
    if n >= n2:
        stringSub = str(n) + " - " + str(n2)
        questionArr.append(stringSub)
        return n - n2
    else:
        stringSub = str(n2) + " - " + str(n)
        questionArr.append(stringSub)
        return n2 - n

def genMult():
    n = random.randint(0, 12)
    n2 = random.randint(0, 12)

    stringMult = str(n) + " x " + str(n2)
    questionArr.append(stringMult)
    return n * n2

def genDiv():
    n = random.randint(1, 36)
    n2 = random.randint(1, 144)

    temp = n2 % n
    n2 -= temp

    stringDiv = str(n2) + " / " + str(n)
    questionArr.append(stringDiv)
    return int(n2 / n)

def genQuestion():
    n = random.randint(0, 3)

    if n == 0:
        return genAdd()
    elif n == 1:
        return genSub()
    elif n == 2:
        return genMult()
    elif n == 3:
        return genDiv()


running = True
occurred = False
occurredTwo = False 
global hit
hit = False

global mainAnswer

global incorrect
incorrect = False
incorrectAnswer = 0

global score
score = 0

while running:

    #screen.fill((80,208,255))
    screen.blit(background_image, [0,0])
    font3 = pygame.font.Font('freesansbold.ttf', 32)
    text3 = font3.render('Score: ' + str(score), True, (0,0,0), (255,255,0))
    textRect3 = text3.get_rect()
    textRect3.center = (800,570)
    randQUestionAnswerTwo(text3, textRect3)

    font4 = pygame.font.Font('freesansbold.ttf', 20)
    text4 = font4.render('Quit', True, (0,0,0), None)
    textRect4 = text4.get_rect()
    textRect4.center = (450, 22)
    randQUestionAnswerTwo(text4, textRect4)

    mouse = pygame.mouse.get_pos()

    if 390 <= mouse[0] <= 520 and 5 <= mouse[1] <= 40:
        pygame.draw.rect(screen, (170, 170, 170),[390,5,130,30], 3, 5)        
    else:
        pygame.draw.rect(screen, (108, 114, 203), [390,5,130,30], 3, 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                moveTankRight()
            if event.key ==pygame.K_LEFT:
                moveTankLeft()
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    missleX = playerX
                    appearMissle(missleX, missleY)
                    bullet_state = 'fire'

        if event.type == pygame.KEYUP:
            playerX += 0
        
        if event.type == pygame.USEREVENT: 
            counter -= 1
            if counter > 0: 
                textTime = str(counter).rjust(3)
            else:
                textTime = 'BOOM!'
                counter = 11
                incorrectAnswer += 1
                occurred = False
        if event.type == pygame.QUIT: 
            run = False

        if event.type == MOUSEBUTTONDOWN:
            if 390 <= mouse[0] <= 520 and 5 <= mouse[1] <= 40:
                pygame.display.quit()
                pygame.quit()
                exec(open('vidTest.py').read())
                exit()


    if missleY <= 0:
        missleY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        appearMissle(missleX, missleY)
        missleY -= 10

    if missleY <= 160:
        missleY = 480
        bullet_state = "ready"

        if thisdict[missleX - 1] == mainAnswer:
            #
            #
            # play "correct answer" sound 
            score += 1
            counter = 11
            hit = True
            occurred = False    
        else:
            incorrectAnswer +=1
            counter = 11
            occurred = False

    #3 white circles displayed to visualize # of strikes
    if incorrectAnswer == 0:
        pygame.draw.circle(screen, (144,238,144), [400, 100], 25)
        pygame.draw.circle(screen, (144,238,144), [450, 100], 25)
        pygame.draw.circle(screen, (144,238,144), [500, 100], 25)
    if incorrectAnswer == 1:
        pygame.draw.circle(screen, (255,0,0), [400, 100], 25)
        pygame.draw.circle(screen, (144,238,144), [450, 100], 25)
        pygame.draw.circle(screen, (144,238,144), [500, 100], 25)
    elif incorrectAnswer == 2:
        pygame.draw.circle(screen, (255,0,0), [400, 100], 25)
        pygame.draw.circle(screen, (255,0,0), [450, 100], 25)
        pygame.draw.circle(screen, (144,238,144), [500, 100], 25)

    #turn all circles red, 3 strikesssss            
    elif incorrectAnswer == 3:
        pygame.draw.circle(screen, (255,0,0), [400, 100], 25)
        pygame.draw.circle(screen, (255,0,0), [450, 100], 25)
        pygame.draw.circle(screen, (255,0,0), [500, 100], 25)
        incorrect = True
        pygame.display.update()

    if incorrect == True:
        ctypes.windll.user32.MessageBoxW(0, "3 STRIKES!!", "YOU LOSE!!", 1)
        incorrect = False
        score = 0
        counter = 11

    if hit == True:
        hit = False
        
    if incorrectAnswer == 3:
        incorrectAnswer = 0
        counter = 11

    #Generate questions
    if occurred == False:
        global questionArr
        questionArr = []
        global answerArr
        answerArr = []
        answerArr.append(genQuestion())
        answerArr.append(genQuestion())
        answerArr.append(genQuestion())
        answerArr.append(genQuestion())

        thisdict = {}

        occurred = True

        n = random.randint(0, 3)
        mainAnswer = answerArr[n]
        font = pygame.font.Font('freesansbold.ttf', 26)
        font1 = pygame.font.Font('freesansbold.ttf', 55)
        text = font1.render(str(mainAnswer), True, (255,0,0), None)
        textRect = text.get_rect()
        textRect.center = (450,340)

    count = 1
    for element in questionArr:
        textTwo = font.render(element, True, (0,0,0), None)
        textRectTwo = text.get_rect()
        num = (260 * (count - 1)) + 19
        thisdict[num] = answerArr[count - 1]
        textRectTwo.center = ((260 * (count - 1)) + 48, 48)
        count += 1
        randQUestionAnswerTwo(textTwo, textRectTwo)
        if occurredTwo == False:
            print(thisdict)

    occurredTwo = True
        
    count = 1

    screen.blit(font.render('Timer:' + str(textTime), True, (128, 0, 128)), (392, 45))

    #pygame.display.flip()
    clock.tick(60)
    player() 
    enemyLocation()
    randQUestionAnswer()
    pygame.display.update()
