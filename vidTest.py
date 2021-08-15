import webbrowser
#webbrowser.open("https://youtu.be/064vYoD1OCg")

import pygame
import sys
import os

# initializing the constructor
pygame.init()
pygame.font.init()
  
# screen resolution
res = (720, 520)
  
# opens up a window
screen = pygame.display.set_mode(res)
pygame.display.set_caption("ArithmeTank")
icon = pygame.image.load("tankIcon.png")
pygame.display.set_icon(icon)

# stores the width of the screen into a variable
width = screen.get_width()
  
# stores the height of the screen into a variable
height = screen.get_height()
  
# defining a font
smallfont = pygame.font.SysFont('segoeui',20)
  
#music
backgroundMusic = pygame.mixer.Sound("backgroundMusic.mp3")
backgroundMusic.play()

# rendering a text written in this font
textQuit = smallfont.render('Quit' , True , (255, 255, 255))
textMultiply =  smallfont.render('Multiplication' , True , (255, 255, 255))
textDivision = smallfont.render('Division' , True , (255, 255, 255))
textAddition = smallfont.render('Addition' , True , (255, 255, 255))
textSubtraction = smallfont.render('Subtraction' , True , (255, 255, 255))
gameStart = smallfont.render('Start' , True , (255, 255, 255))
instructions1 = smallfont.render('The four buttons "Addition", "Subtraction", "Division" and' , True , (255, 255, 255))
instructions2 = smallfont.render('"Multiplication" will lead you to videos teaching you how', True, (255, 255, 255))
instructions3 = smallfont.render('to perform those operations. The start button will open up', True, (255, 255, 255))
instructions4 = smallfont.render('a game to test your knowledge.', True, (255, 255, 255))
iconImg = pygame.image.load("icon.png")
iconImg = pygame.transform.scale(iconImg, (25, 25))
muteImg = pygame.image.load("mute.png")
unmuteImg = pygame.image.load("unmute.png")
muteImg = pygame.transform.scale(muteImg, (30, 30))
unmuteImg = pygame.transform.scale(unmuteImg, (30, 30))
global muted

muted = False

while True:
      
    for event in pygame.event.get():
          
        if event.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the button the game is terminated
            if 450 <= mouse[0] <= 590 and 300 <= mouse[1] <= 340: #quit
                pygame.quit()
            elif 150 <= mouse[0] <= 290 and 100 <= mouse[1] <= 140: #addition
                webbrowser.open("https://youtu.be/Vu4y2TIQa5Q")
            elif 450 <= mouse[0] <= 590 and 100 <= mouse[1] <= 140: #subtraction
                webbrowser.open("https://youtu.be/kSrfjQuASWc")
            elif 150 <= mouse[0] <= 290 and 200 <= mouse[1] <= 240: #multiplication
                webbrowser.open("https://youtu.be/_kLIMaddLwQ")
            elif 450 <= mouse[0] <= 590 and 200 <= mouse[1] <= 240: #division
                webbrowser.open("https://youtu.be/kw-toevjRxs")
            elif 10 <= mouse[0] <= 50 and 10 <= mouse[1] <= 50:
                if muted == True:
                    muted = False
                else:
                    muted = True
            elif 150 <= mouse[0] <= 290 and 300 <= mouse[1] <= 340: #Start
                pygame.display.quit()
                pygame.quit()
                exec(open('game.py').read())
                exit()

    screen.fill((23,24,31))
    
    # stores the (x,y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()
      
    # if mouse is hovered on a button it changes to lighter shade (Addition)
    if 140 <= mouse[0] <= 280 and 100 <= mouse[1] <= 140:
        pygame.draw.rect(screen, (170, 170, 170),[140,100,140,40], 3, 5)        
    else:
        pygame.draw.rect(screen, (108, 114, 203), [140,100,140,40], 3, 5)
      
    # if mouse is hovered on a button it changes to lighter shade (Subtraction)  
    if 440 <= mouse[0] <= 580 and 100 <= mouse[1] <= 140:
        pygame.draw.rect(screen,(170, 170, 170),[440,100,140,40], 3, 5)   
    else:
        pygame.draw.rect(screen, (108, 114, 203),[440,100,140,40], 3, 5)
    
        # if mouse is hovered on a button it changes to lighter shade (Multiplication)
    if 140 <= mouse[0] <= 280 and 200 <= mouse[1] <= 240:
        pygame.draw.rect(screen,(170, 170, 170),[140,200,140,40], 3, 5)        
    else:
        pygame.draw.rect(screen, (108, 114, 203),[140,200,140,40], 3, 5)
      
    # if mouse is hovered on a button it changes to lighter shade (Division)  
    if 440 <= mouse[0] <= 580 and 200 <= mouse[1] <= 240:
        pygame.draw.rect(screen,(170, 170, 170),[440,200,140,40], 3, 5)   
    else:
        pygame.draw.rect(screen, (108, 114, 203),[440,200,140,40], 3, 5)

        # if mouse is hovered on a button it changes to lighter shade (Start)
    if 140 <= mouse[0] <= 280 and 300 <= mouse[1] <= 340:
        pygame.draw.rect(screen, (87, 190, 108),[140,300,140,40], 3, 5)        
    else:
        pygame.draw.rect(screen, (108, 114, 203),[140,300,140,40], 3, 5)
      
    # if mouse is hovered on a button it changes to lighter shade (Quit)  
    if 440 <= mouse[0] <= 580 and 300 <= mouse[1] <= 340:
        pygame.draw.rect(screen, (215, 83, 100),[440,300,140,40], 3, 5)   
    else:
        pygame.draw.rect(screen, (108, 114, 203),[440,300,140,40], 3, 5)

     # if mouse is hovered on a button it changes to lighter shade (Quit)  
    if 10 <= mouse[0] <= 50 and 10 <= mouse[1] <= 50:
        pygame.draw.rect(screen, (170, 170, 170),[10,10,40,40], 3, 5)   
    else:
        pygame.draw.rect(screen, (108, 114, 203),[10,10,40,40], 3, 5)    
    
    # superimposing the text onto our button
    screen.blit(textAddition , (172,105))
    screen.blit(textSubtraction , (463,105))
    screen.blit(textMultiply, (154,205))
    screen.blit(textDivision, (476,205))
    screen.blit(gameStart, (189,305))
    screen.blit(textQuit, (490,305))
    screen.blit(instructions1, (120,380))
    screen.blit(instructions2, (122,410))
    screen.blit(instructions3, (114,440))
    screen.blit(instructions4, (230,470))
    screen.blit(iconImg, (70, 420))

    if muted == False:
        screen.blit(unmuteImg, (13, 13))
        backgroundMusic.set_volume(0.07)
    elif muted == True:
        screen.blit(muteImg, (13, 13))
        backgroundMusic.set_volume(0)
      
    title_font = pygame.font.SysFont("comicsans", 43)
    title_label = title_font.render("Welcome To ArithmeTank", 1, (255,255,255))
    screen.blit(title_label, (185, 30))
    # updates the frames of the game
    pygame.display.update()