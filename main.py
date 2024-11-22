import os
import pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from constants import *

def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        black = (0, 0, 0)
        screen_surface = pygame.display.get_surface()
        screen_surface.fill(black)
        pygame.display.flip()

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop()

if __name__ == "__main__":
    main()
