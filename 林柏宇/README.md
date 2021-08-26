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





控制正方形的大小

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
