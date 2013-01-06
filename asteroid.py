import pygame
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen_size, size=3):
        # Call inherited initialization
        super(pygame.sprite.Sprite, self).__init__()

        # Establish the size and location of the asteroid
        self.rect = pygame.Rect(0, 0, size * 20, size * 20)

        # Draw a simple circle
        self.image = pygame.Surface(self.rect.size)
        self.image.set_colorkey(pygame.Color('Black'))  # "Transparent" color
        color = pygame.Color('Gray')                    # Asteroid color
        pygame.draw.circle(self.image, color, self.rect.center,
                           self.rect.width / 2)

        # Initial location and velocity
        self.rect.left = random.randint(0, screen_size[0] - self.rect.width)
        self.vx = 0
        self.vy = random.randint(1, 3)

    def update(self, screen_size):
        """"""
        self.rect.move_ip(self.vx, self.vy)

        # Vertical "leading-edge" screen wrapping
        if self.rect.bottom > screen_size[1]:
            self.rect.top = 0
