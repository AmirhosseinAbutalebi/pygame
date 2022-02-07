import pygame
import time
import random
# use library pygame
pygame.init()
Sound_Gameover = pygame.mixer.Sound("2.wav")
#pygame.mixer.music.load("1.wav")
# width and height for display window
display_width=800
display_height=600
# colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
gray = (45,43,43)
green = (15,211,0)
blue = (0,10,211)
yellow = (255,222,0)
orange = (255,138,0)
pink = (255,0,240)
# instruction for display
Display = pygame.display.set_mode((display_width,display_height))
# instruction for title window's game
pygame.display.set_caption('Game')
# image car or goal
image_goal = pygame.image.load("car.png")
image_obstacls = pygame.image.load("obstacl.png")
image_wall = pygame.image.load("narde.png")
# width image goal or car
width_Img = 69
# width image obstracle
width_Img2 = 66
# width image wall
width_Img3 = 25
# function for button
def button(msg,x,y,w,h,ic,c,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y :
        pygame.draw.rect(Display,ic,(x,y,w,h))
        if click[0] == 1 and action != None :
            if action == "Play" :
                game_Show()
            elif action == "Quit" :
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(Display,c,(x,y,w,h))
    text_s = pygame.font.Font('freesansbold.ttf',20)
    Textsurface , TextRect = text_objects(msg,text_s)
    TextRect.center = ((x+(w/2)),(y+(h/2)))
    Display.blit(Textsurface,TextRect)
# function for first page
def introduction():
    intro = True
    while intro :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Display.fill(yellow)
        font = pygame.font.Font('freesansbold.ttf',50)
        Textsurface , TextRect = text_objects("Let's Go",font)
        TextRect.center = ((display_width/2),(display_height/2))
        Display.blit(Textsurface,TextRect)
        button("Play",150,450,100,50,green,yellow,"Play")
        button("Quit",550,450,100,50,red,yellow,"Quit")
        pygame.display.update()
# function for calculation score
def score (counter):
    font = pygame.font.SysFont(None , 25)
    text = font.render('Score : '+ str(counter), True , red)
    Display.blit(text,(width_Img3 + 5 , 0))
# function for coordinates goal or car
def Show_img_goal(x,y):
    Display.blit(image_goal,(x,y))
# function for coordinates obtacls
def Show_img_obtacls(x,y):
    Display.blit(image_obstacls,(x,y))
# function for draw road
def Show_Road(x,y,w,h,c):
    pygame.draw.rect(Display,c,[x,y,w,h])   
# function for show wall 
def Show_wall(x,y):
    Display.blit(image_wall,(x,y)) 
# function for font and text
def text_objects(text,font):
    Textsurface = font.render(text,True,black)
    return Textsurface , Textsurface.get_rect()
# funtion for show massege
def show_text(text):
    font = pygame.font.Font('freesansbold.ttf',50)
    Textsurface , TextRect = text_objects(text,font)
    TextRect.center = ((display_width/2),(display_height/2))
    Display.blit(Textsurface,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_Show()
# function for crash to obstacles
def crash():
    #pygame.mixer.music.stop()
    pygame.mixer.Sound.play(Sound_Gameover)
    font = pygame.font.Font('freesansbold.ttf',50)
    Textsurface , TextRect = text_objects("!!! You Crashed !!!",font)
    TextRect.center = ((display_width/2),(display_height/2))
    Display.blit(Textsurface,TextRect)
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Try Again",150,450,100,50,green,gray,"Play")
        button("Quit",550,450,100,50,red,gray,"Quit")
        pygame.display.update()
#function for show game
def game_Show():  
    #pygame.mixer.music.play(-1)
    # coordinate variable
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_w1 = 0
    x_w2 = display_width - width_Img3
    y_w = 0
    # move by key
    move_shape = 0
    obstacles_Speed = 5
    x_obs = random.randrange(width_Img3 , display_width - width_Img2 - width_Img3)
    y_obs = -1000
    counter = 0 
    # variable for road
    x_r = 225
    x_r_2 = 525
    y_r = -700
    y_r_1 = -300 
    w = 20
    h = 100
    # instruction for speed game
    Clock = pygame.time.Clock()
    Close = True
    while Close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Close = False 
    # instruction for move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        move_shape = -5
                if event.key == pygame.K_RIGHT:
                        move_shape = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                    move_shape = 0    
        x += move_shape              
        if x < width_Img3 or x > display_width - width_Img - width_Img3:
            crash()
        # instruction for show
        Display.fill(gray)
        Show_wall(x_w1,y_w)
        Show_wall(x_w2,y_w)
        Show_Road(x_r,y_r_1,w,h,white)
        Show_Road(x_r,y_r,w,h,white)
        Show_Road(x_r_2,y_r_1,w,h,white)
        Show_Road(x_r_2,y_r,w,h,white)  
        Show_img_goal(x,y)
        score(counter)
        if y_r_1 > display_height :
            y_r_1 = -250
        if y_r > display_height :
            y_r = -250
        if y_obs > display_height :
            y_obs = -500
            x_obs = random.randrange(width_Img3,display_width-width_Img2-width_Img3)
            counter += 1
            if (counter % 5 == 0):
                obstacles_Speed += 1
        if y < y_obs + width_Img2 :
            if x > x_obs and  x < x_obs + width_Img2 or x + width_Img > x_obs and x + width_Img < x_obs + width_Img2 :
                crash()
        Show_img_obtacls(x_obs,y_obs)
        y_obs += obstacles_Speed 
        y_r_1 += obstacles_Speed
        y_r += obstacles_Speed      
        pygame.display.update()
        Clock.tick(60) 
introduction()        
game_Show()
pygame.quit()
quit()