# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 22:24:00 2021

@author: user
"""

# Simple pygame program


# Import and initialize the pygame library

import pygame

pygame.init()



# Set up the drawing window

screen = pygame.display.set_mode([750, 750])

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
                surfX = surfX + 50
                surfY = surfX + 50
            
            if event.key == pygame.K_LEFT:
                surfX = surfX - 60
                surfY = surfY - 60

    #============畫布區塊============    
 
    #畫布的顏色
    screen.fill((0, 30, 30))


    #畫圓形
    pygame.draw.circle(screen, (150, 0, 150), (X, Y), 200)

    #畫四方形
    if surfX <= 0:
        surfX = 0
    if surfY <= 0:
        surfY = 0
    surf = pygame.Surface((surfX, surfY)) #四方型的長寬
    surf.fill((0, 255, 0)) #四方型的顏色
    rect = surf.get_rect()
    screen.blit(surf, (X-surfX/12, Y-surfY/3)) #四方形左上角的座標


    #============畫布區塊============

    #將所有圖形顯示在畫布上
    pygame.display.flip()
pygame.quit()