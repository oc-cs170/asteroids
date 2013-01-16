import pygame
import random


class Asteroid(pygame.sprite.Sprite):
    """An asteroid that is aware of pygame.

    A round piece of space debris that comes in 3 sizes.
    Coordinates are the center of the asteroid.
    """
    def __init__(self, screen_size, size=3):
        """Create an asteroid.

        Args:
            screen_size: a 2-int tuple, the width and height of the screen
            size: an int (optional), ranging from 1-3 to determine asteroid size
        """
        # Call inherited initialization
        super(pygame.sprite.Sprite, self).__init__()

        # Creation parameters
        self.screen_width, self.screen_height = screen_size

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

    def update(self):
        """Update the position of the asteroid.

        Object moves through space at a constant velocity, wrapping when its
        leading-edge leaves the screen.
        """
        self.rect.move_ip(self.vx, self.vy)

        # Vertical "leading-edge" screen wrapping
        if self.rect.bottom > self.screen_height:
            self.rect.top = 0
