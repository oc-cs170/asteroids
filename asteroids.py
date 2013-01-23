#!/usr/bin/env python

"""Main file with game loop for Asteroids.

Uses Asteroid, Ship, and Alien(?) from external modules.
"""

import pygame
import random

from ship import Ship
from asteroid import Asteroid
from bullet import Bullet

WINDOW_TITLE = 'Asteroids'
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768


class Asteroids(object):
    """Create a game of Asteroids."""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Fill the screen with black while space is being created
        self.screen.fill(pygame.Color('Black'))
        pygame.display.flip()
        self.background = self.create_background(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # For ship movement
        self.angle = 0
        self.moving = 0
        
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
        """Start Asteroid program.

        Puts ship in the middle of the screen, generates some asteroids
        and gives them some random velocities.
        """
        # Game objects
        self.ship = Ship(self.screen)
        self.bullets = []
        self.hero = pygame.sprite.Group()
        # self.hero.add(self.ship)
        self.asteroids = []
        for i in range(3):
            self.asteroids.append(Asteroid(self.screen.get_size()))
        self.asteroids.append(Asteroid(self.screen.get_size(), 2))
        
        self.bullets = []
        
        # For on screen text
        font = pygame.font.SysFont("monospace", 15)
        
        running = True
        while running:
            self.clock.tick(30)  # Max frames per second

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.angle = -10
                if event.key == pygame.K_LEFT:
                    self.angle = 10
                if event.key == pygame.K_UP:
                    self.moving = .5
                if event.key == pygame.K_SPACE:
                    self.bullets.append(Bullet(self.screen.get_size(), self.ship.angle, self.ship.rect.center))
        
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or  event.key == pygame.K_LEFT:
                    self.angle = 0
                if event.key == pygame.K_UP:
                    self.moving = 0
            
            # Draw the scene
            self.screen.blit(self.background, (0, 0))
            # self.hero.draw(self.screen)
            self.screen.blit(self.ship.image, self.ship.rect)
            
            for bullet in self.bullets:
                self.screen.blit(bullet.art,bullet.rect)
                if bullet.update():
                    self.bullets.remove(bullet)
                contact = bullet.rect.collidelist(self.asteroids)
                if  contact >= 0:
                    del self.asteroids[contact]
                    self.bullets.remove(bullet)
                    
            for asteroid in self.asteroids:
                self.screen.blit(asteroid.image, asteroid.rect)
                asteroid.update()
                # If asteroid collides with the ship
                if asteroid.rect.colliderect(self.ship.rect):
                    self.screen.blit(font.render("BOOM", 2, (255,255,0)), (512,384))
            
            # Update ship
            self.ship.update(self.angle, self.moving)
            
            for asteroid in self.asteroids:
                if self.ship.rect.colliderect(asteroid.rect):
                    self.screen.blit(font.render("BOOM", 2, (255,255,0)), (512,384))
                    # running = False
                
                
            #Displays direction of ship in angle and radians
            
            ship_angle = font.render("Angle " + str(self.ship.angle), 2, (255,255,0))
            self.screen.blit(ship_angle, (0, 28))
            ship_radians = font.render("Radians " + str(self.ship.radians), 2, (255,255,0))
            self.screen.blit(ship_radians, (0, 14))
            
            pygame.display.flip()

            


if __name__ == '__main__':
    game = Asteroids()
    game.play()
