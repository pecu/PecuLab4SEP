
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 20:36:21 2021

@author: 寄軸
"""

# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
addgreen = 0

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                addgreen = 1

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    
    if addgreen == 1:
        pygame.draw.circle(screen, (0, 255, 0), (250, 250), 50)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()