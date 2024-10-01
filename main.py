import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()

    screen = pygame.display.set_mode(size=[SCREEN_WIDTH, SCREEN_HEIGHT])

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    dt = 0
    dt_clock = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    asteroidField = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill(pygame.Color(0, 0, 0))
        for objects in drawable:
            objects.draw(screen)

        for objects in updatable:
            objects.update(dt)

        for objects in asteroids:
            if CircleShape.is_coliding(objects, player):
                sys.exit("Game over")

        for objects in asteroids:
            for bullet in shots:
                if CircleShape.is_coliding(bullet, objects):
                    objects.split()


        pygame.display.flip()
        dt = dt_clock.tick(60)/1000



if __name__ == "__main__":
    main()