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