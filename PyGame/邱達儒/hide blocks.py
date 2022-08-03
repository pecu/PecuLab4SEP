# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 19:14:43 2022

@author: user
"""

# Simple pygame program


# Import and initialize the pygame library

import pygame
import time
import random 

pygame.init()

# Set up the drawing window

screen = pygame.display.set_mode([500, 500])
Fraction = 0
X = 25
Y = 500
Y1 = 250
X1 = 250
# Run until the user asks to quit

running = True
move =  True
while running:
    time.sleep(0.1)
    Y1=Y1+1
    if Y1 == 500:
        Y1 = 0    
    if Y1 == 0 :
        X1=random.randrange(10, 490)
    if X1==X and Y1==Y:
        Fraction=Fraction+1
        print(Fraction)
        Y1=500
        X1=random.randrange(10, 490)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                X = X + 10
            if event.key == pygame.K_LEFT:
                X = X - 10                
                
    # Fill the background with white

    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    
    surf = pygame.Surface((40, 20))
    surf.fill((0,0,0))
    rect = surf.get_rect()
    screen.blit(surf, (X1, Y1))
    Y1=Y1  

    pygame.draw.circle(screen, (0, 0, 255), (X, Y), 10)

    # Flip the display

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()