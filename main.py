import pygame
from constants import *

def main():
    pygame.init()
    pygame.display.set_mode(size=[SCREEN_WIDTH, SCREEN_HEIGHT])
    while True:
        pygame.Surface.fill(pygame.Color(0, 0, 0), rect=None, special_flags=0) # DOES NOT CURRENTLY WORK


if __name__ == "__main__":
    main()