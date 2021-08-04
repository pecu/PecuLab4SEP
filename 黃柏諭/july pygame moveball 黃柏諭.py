# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 08:43:11 2021

@author: user
"""

import pygame
from pygame.math import Vector2
screen = pygame.display.set_mode((640,480))
done = False
ballP = Vector2(10,10)
ballV = Vector2(5,3)
barW = 60
barH = 30
barY = 440
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True    
    screen.fill((0,255,0))
    ballP += ballV
    ballV.x *= -1 if ballP.x > screen.get_width() or ballP.x <0 else 1
    ballV.y *= -1 if ballP.y > screen.get_height() or ballP.y <0 else 1
    pygame.draw.circle(screen, (50,50,250),[int(ballP.x),int(ballP.y)],10)
    mouseX, mouseY = pygame.mouse.get_pos()
    pygame.draw.rect(screen,(0,128,128),[mouseX,barY,barW,barH])
    pygame.display.update()