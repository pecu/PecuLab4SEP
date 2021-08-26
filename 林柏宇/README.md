# PecuLab4SEP
PyGame

Empty.py 第一個程式

# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()





方向鍵控制正方形的大小
# Simple pygame program


# Import and initialize the pygame library

import pygame

pygame.init()



# Set up the drawing window

screen = pygame.display.set_mode([500, 500])

X = 250
Y = 250
surfX = 100
surfY = 100
    
# Run until the user asks to quit

running = True

while running:

    #============接收指令區塊============    

    #等待使用者給予指令
    for event in pygame.event.get():
        #當接收到畫布上的離開時，直接跳開while，結束程式
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                surfX = surfX + 10
                surfY = surfX + 10
            
            if event.key == pygame.K_LEFT:
                surfX = surfX - 10
                surfY = surfY - 10

    #============畫布區塊============    
 
    #畫布的顏色
    screen.fill((0, 255, 255))


    #畫圓形
    pygame.draw.circle(screen, (255, 0, 255), (X, Y), 100)

    #畫四方形
    if surfX <= 0:
        surfX = 0
    if surfY <= 0:
        surfY = 0
    surf = pygame.Surface((surfX, surfY)) #四方型的長寬
    surf.fill((0, 255, 0)) #四方型的顏色
    rect = surf.get_rect()
    screen.blit(surf, (X-surfX/2, Y-surfY/2)) #四方形左上角的座標


    #============畫布區塊============

    #將所有圖形顯示在畫布上
    pygame.display.flip()
pygame.quit()






TufOfWar.py 拔河的遊戲

# Simple pygame program


# Import and initialize the pygame library

import pygame

pygame.init()


# Set up the drawing window

screen = pygame.display.set_mode([500, 500])

X = 250
Y = 250

# Run until the user asks to quit

running = True

while running:


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
            
                X = X + 2
            
            if event.key == pygame.K_LEFT:
            
                X = X - 2


    # Fill the background with white

    screen.fill((255, 255, 255))


    # Draw a solid blue circle in the center

    
    pygame.draw.circle(screen, (255, 0, 0), (350, Y), 5)
    pygame.draw.circle(screen, (255, 0, 0), (150, Y), 5)


    
    surf = pygame.Surface((500, 1))
    surf.fill((0,0,0))
    rect = surf.get_rect()
    screen.blit(surf, (0, Y))
    
    surf = pygame.Surface((1, 100))
    surf.fill((0,0,0))
    rect = surf.get_rect()
    screen.blit(surf, (250, 200))


    pygame.draw.circle(screen, (0, 0, 255), (X, Y), 10)


    # Flip the display

    pygame.display.flip()


# Done! Time to quit.

pygame.quit()





play.py 打方塊的遊戲
drew.py 是打方塊遊戲中自定義的套件 [drew]
8/19 複習8/14的課程
