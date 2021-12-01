# -*- coding: utf-8 -*-


# Simple pygame program


# Import and initialize the pygame library

import pygame
import numpy as np

pygame.init()


# Set up the drawing window

screen = pygame.display.set_mode([500, 500])

w_add = []
s_add = []
w = 250
s = 250
x = 250
y = 250
ColorR = 0 #0~255
ColorG = 0 #0~255
surfX = 20
surfY = 20
circle_size = 15
num = 0

# Run until the user asks to quit

running = True
screen.fill((255, 255, 255))

while running:

    #============接收指令區塊============    

    #等待使用者給予指令
     #等待使用者給予指令
    for event in pygame.event.get():
 
        #當接收到畫布上的離開時，直接跳開while，結束程式
        if event.type == pygame.QUIT : 
            running = False   
        if event.type == pygame.KEYDOWN:
            
 
            if event.key == pygame.K_w:#上鍵改變
                    w = w - 10
                    screen.fill((255, 255, 255))

            if event.key == pygame.K_s:#下鍵改變
                    w = w + 10
                    screen.fill((255, 255, 255))
                    
            if event.key == pygame.K_a:#左鍵改變
                    s = s - 10
                    screen.fill((255, 255, 255))
                    
            if event.key == pygame.K_d:#右鍵改變
                    s = s + 10
                    screen.fill((255, 255, 255))

            if event.key == pygame.K_UP:#上鍵改變
                    ColorR = ColorR - 50
                    ColorG = ColorG - 50
            if event.key == pygame.K_DOWN:#下鍵改變
                    ColorR = ColorR + 50
                    ColorG = ColorG + 50
            if event.key == pygame.K_RIGHT: #右箭頭
                    x = x + 10
            if event.key == pygame.K_LEFT: #左箭頭
                    x = x - 10
            if event.key == pygame.K_v:
                    circle_size = circle_size - 10
                    y = y - 10
            if event.key == pygame.K_c:
                    num = num + 1
                    w_add = np.append(w_add, w)
                    s_add = np.append(s_add, s)
                    print(num)
            
            for i in range(num):
                print(s_add[i])
                pygame.draw.circle(screen, (ColorR, 0, 255), (s_add[i], w_add[i]), circle_size, 1)

            
    #============畫布區塊============    

    #畫布的顏色


    #畫圓形
    if w <= 0:
        w = 0
    if s <= 0:
        s = 0
    
    if w >= 500:
        w = 500
    if s >= 500:
        s = 500
    
    if x >= 500:
        x = 500
    if y >=500:
        y = 500
    
    if x <= 0 :
        x = 0
    if y <= 0:
        y = 0
        
    if ColorR <= 0:
        ColorR = 0
    if ColorR >= 255:
        ColorR = 255
    if ColorG <= 0:
        ColorG = 0
    if ColorG >= 255:
        ColorG = 255
    # pygame.draw.circle(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
    pygame.draw.circle(screen, (ColorR, 0, 255), (s, w), circle_size, 1) 
    

     
    #============畫布區塊============

    #將所有圖形顯示在畫布上
    pygame.display.flip()
pygame.quit() 
