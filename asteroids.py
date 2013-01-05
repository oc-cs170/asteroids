#!/usr/bin/env python
# Asteroids
import pygame
import random

from ship import Ship

WINDOW_TITLE = 'Asteroids'
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768


class Asteroids(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Fill the screen with black while space is being created
        self.screen.fill(pygame.Color('Black'))
        pygame.display.flip()
        self.background = self.create_background(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Use a clock to control frame rate
        self.clock = pygame.time.Clock()

    def create_background(self, width, height):
        """A black background, filled with stars... The Final Frontier.

        The background is randomly filled with 1x1 pixel white "stars" whose
        alpha (transparency) varies from 6-50%.
        """
        # Copy space from the main screen surface
        space = self.screen.copy()
        space.fill(pygame.Color('Black'))

        # Create a single pixel "star"
        star = pygame.Surface((1, 1))
        star.fill(pygame.Color('White'))

        # Randomly choose coordinates to blit a randomly bright "star"
        for i in range(0, width, 2):
            for j in range(0, height, 2):
                if random.randint(1, 1000) <= 3:             # 0.3% is a star
                    star.set_alpha(random.randint(16, 128))  # Random brightness
                    space.blit(star, (i, j))
        return space

    def play(self):
        # Game objects
        self.ship = Ship(self.screen)
        self.hero = pygame.sprite.Group()
        # self.hero.add(self.ship)

        running = True
        while running:
            self.clock.tick(30)  # Max frames per second

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False

            # Draw the scene
            self.screen.blit(self.background, (0, 0))
            # self.hero.draw(self.screen)
            self.screen.blit(self.ship.image, self.ship.rect)
            pygame.display.flip()

            # Update game objects
            self.ship.update()


if __name__ == '__main__':
    game = Asteroids()
    game.play()