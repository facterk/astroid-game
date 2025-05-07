import pygame
from constants import *

def main():
    result = "Starting Asteroids!"
    print(result)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    running = True
    while running:
        screen.fill((0,0,0))
        pygame.display.flip()
    return result
if __name__ =="__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")