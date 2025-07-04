import pygame  # import pygame

from constants import *  # import all constants
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        Player.update(dt)
        screen.fill("black")
        pygame.display.flip()

        #limit theh framerate to 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()


