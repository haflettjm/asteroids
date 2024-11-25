import os
import pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def game_loop(gameClock, dt, updateable, drawable, asteroids, PlayerX, shots):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for sprite in updateable:
            sprite.update(dt)
        for asteroid in asteroids:
            collided = asteroid.collisioncheck(PlayerX)
            if collided == True:
                print("game overrrrr")
            for bullet in shots:
                collided = asteroid.collisioncheck(bullet)
                if collided == True:
                    asteroid.split()
                    bullet.kill()

        black = (0, 0, 0)
        screen_surface = pygame.display.get_surface()
        screen_surface.fill(black)
        drawables = drawable.sprites()
        for sprite in drawables:
            sprite.draw(screen)
        pygame.display.flip()
        framerate = 60
        dt = (gameClock.tick(framerate))/1000

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameClock = pygame.time.Clock()
    dt = 0
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    PlayerX = Player(SCREEN_WIDTH /2 , SCREEN_HEIGHT / 2)
    asteroidsfield = AsteroidField()
    game_loop(gameClock, dt, updatable, drawable, asteroids, PlayerX, shots)

if __name__ == "__main__":
    main()
