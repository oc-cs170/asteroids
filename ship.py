import pygame
import math


class Ship(pygame.sprite.Sprite):
    """A ship class that is aware of pygame.

    A yellow isosceles triangle that smoothly rotates about its center.
    Coordinates are the center of the smallest rectangle that encloses
    the ship.
    Angle is measured from 0 on the cartesian plane (3 o'clock).
    """
    def __init__(self, screen):
        """Create a ship object.

        Args:
            screen: a pygame surface, a pointer to the display buffer
        """
        # Call inherited initialization
        super(pygame.sprite.Sprite, self).__init__()

        # Establish the size and location of the ship
        self.rect = pygame.Rect(0, 0, 35, 21)
        self.rect.center = screen.get_rect().center
        self.screen_width, self.screen_height = screen.get_rect().size
        

        # Draw a simple triangle
        self.art = pygame.Surface(self.rect.size)
        self.art.set_colorkey(pygame.Color('Black'))  # "Transparent" color
        self.color = pygame.Color('Yellow')           # Ship color
        polygon = [(0, 0), (34, 10), (0, 20), (5, 10)]
        pygame.draw.polygon(self.art, self.color, polygon)

        # First version of the image is the permanent ship graphic
        self.image = self.art
        self.angle = 0  # Initial angle is cartesian coordinates 0
        self.radians = 0
        self.velocity = 0
        self.xv = 0
        self.yv = 0

    def update(self, angle, moving):
        """Update the position and orientation of the ship.

        Should be called every frame, by the main game loop to allow the
        ship to move. Movements consist of x, y translation, and cartesian
        rotation (0 degrees = 3 o'clock).
        """
         
        self.angle += angle
        if self.angle < 0:
            self.angle += 360
        elif self.angle == 360:
            self.angle = 0 
        self.radians = math.radians(self.angle)
        if moving:
            xv = moving * math.cos(self.radians)
            yv = moving * math.sin(self.radians)
            xv += self.xv
            yv += self.yv
            theta = math.atan2(yv, xv)
            self.velocity = math.sqrt(xv**2 + yv**2)
            self.velocity = min(self.velocity, 12)
            self.xv = self.velocity * math.cos(theta)
            self.yv = self.velocity * math.sin(theta)
        
        
        self.rect.move_ip(self.xv, -self.yv)
        
        
        # Vertical "leading-edge" screen wrapping
        if self.rect.bottom > self.screen_height:
            self.rect.top = 0

        elif self.rect.top < 0:
            self.rect.bottom = self.screen_height
        
        # Horizontal "leading-edge" screen wrapping
        elif self.rect.right > self.screen_width:
            self.rect.left = 0
        
        elif self.rect.left < 0:
            self.rect.right = self.screen_width
            
        # Set the image and rect, based on instance parameters
        # The image is a transform of the ship "art"
        self.image = pygame.transform.rotate(self.art, self.angle)
        # The rect is a rectangle centered on the x, y of the ship
        self.rect = self.image.get_rect(center=self.rect.center)








