import pygame
from constants import *
from player import *

def main():
    pygame.init()

    screen = pygame.display.set_mode(size=[SCREEN_WIDTH, SCREEN_HEIGHT])


    dt = 0
    dt_clock = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    pygame.sprite.Group.add(updatable, player)
    pygame.sprite.Group.add(drawable, player)

    print(pygame.sprite.Group.has(updatable, player))
    print(pygame.sprite.Group.has(drawable, player))
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0, 0, 0))
        for objects in drawable:
            objects.draw(screen)

        for objects in updatable:
            objects.update(dt)

        pygame.display.flip()
        dt = dt_clock.tick(60)/1000



if __name__ == "__main__":
    main()