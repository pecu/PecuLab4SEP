# Simple pygame program


# Import and initialize the pygame library

import pygame

pygame.init()


# Set up the drawing window

screen = pygame.display.set_mode([500, 500])

X = 250
Y = 250

RX_right = 350
RX_left = 150

# Run until the user asks to quit

running = True

while running:


    # Did the user click the window close button?
    
    # 等待使用者給定鍵盤上的控制項
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        
        if event.type == pygame.KEYDOWN:
        # 藍色球移動的右左控制
            if event.key == pygame.K_RIGHT:
                X = X + 2
            if event.key == pygame.K_LEFT:
                X = X - 2
        # 紅色雙球移動的右左控制
            if event.key == pygame.K_x:
                RX_right = RX_right + 2
                RX_left = RX_left + 2
            if event.key == pygame.K_z:
                RX_right = RX_right - 2
                RX_left = RX_left - 2

    # Fill the background with white

    screen.fill((255, 255, 255))


    # Draw a solid blue circle in the center

    
    # 兩顆小紅球
    pygame.draw.circle(screen, (255, 0, 0), (RX_right, Y), 5)
    pygame.draw.circle(screen, (255, 0, 0), (RX_left, Y), 5)

    #畫直線
    pygame.draw.line(screen, (0, 255, 0), (RX_right, Y+5), (RX_left, Y+20), 10)
    
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