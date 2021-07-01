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
    screen.fill((255, 255, 255))


    #畫圓形
    pygame.draw.circle(screen, (0, 0, 255), (X, Y), 100)

    #畫四方形
    if surfX <= 0:
        surfX = 0
    if surfY <= 0:
        surfY = 0
    surf = pygame.Surface((surfX, surfY)) #四方型的長寬
    surf.fill((255, 255, 255)) #四方型的顏色
    rect = surf.get_rect()
    screen.blit(surf, (X-surfX/2, Y-surfY/2)) #四方形左上角的座標

    #============畫布區塊============

    #將所有圖形顯示在畫布上
    pygame.display.flip()
pygame.quit()