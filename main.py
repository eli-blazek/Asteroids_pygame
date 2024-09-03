import pygame
from constants import *
from player import *

def main():
    pygame.init()

    screen = pygame.display.set_mode(size=[SCREEN_WIDTH, SCREEN_HEIGHT])
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    dt = 0
    dt_clock = pygame.time.Clock()
    player = Player(x, y)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0, 0, 0))
        pygame.display.flip()
        player.draw(screen)
        dt = dt_clock.tick(60)/1000



if __name__ == "__main__":
    main()