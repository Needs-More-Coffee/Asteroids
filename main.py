import pygame
from constants import *
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while running:
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                running = False
            
        log_state()
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60)

if __name__ == "__main__":
    main()
