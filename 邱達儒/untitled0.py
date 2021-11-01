# -*- coding: utf-8 -*-


# Simple pygame program


# Import and initialize the pygame library

import pygame

pygame.init()


# Set up the drawing window

screen = pygame.display.set_mode([500, 500])

w = 250 #y
s = 250
Colorone = 400 
Colortwo = 400 
surfX = 20
surfY = 20
circle_size = 15


# Run until the user asks to quit

running = True

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
            if event.key == pygame.K_s:#下鍵改變
                    w = w + 10
            if event.key == pygame.K_a:#左鍵改變
                    s = s - 10
            if event.key == pygame.K_d:#右鍵改變
                    s = s + 10 
            if event.key == pygame.K_UP:#上鍵改變
                    Colorone = Colorone - 10
            if event.key == pygame.K_DOWN:#下鍵改變
                    Colorone = Colorone + 10 
            if event.key == pygame.K_RIGHT: #右箭頭
                    Colortwo = Colortwo + 10
            if event.key == pygame.K_EFT: #左箭頭
                    Colortwo = Colortwo - 10
            if event.key == pygame.K_v:
                    circle_size = circle_size - 10
            if event.key == pygame.K_c:
                    circle_size = circle_size + 10
    #============畫布區塊============    

    #畫布的顏色
    screen.fill((255, 255, 255))


    #畫圓形
    if w <= 0:
        w = 0
    if s <= 0:
        s = 0
    
    if w >= 500:
        w = 500
    if s >= 500:
        s = 500
    pygame.draw.circle(screen,(Colorone, Colortwo, 255), (s, w), circle_size)
           
    #============畫布區塊============

    #將所有圖形顯示在畫布上
    pygame.display.flip()
pygame.quit() 
