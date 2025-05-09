import pygame
from constants import *
from player import Player

def main():
    result = "Starting Asteroids!"
    print(result)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    running = True
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        screen.fill((0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
    return result
if __name__ =="__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")