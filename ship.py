import pygame


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

        # Draw a simple triangle
        self.art = pygame.Surface(self.rect.size)
        self.art.set_colorkey(pygame.Color('Black'))  # "Transparent" color
        self.color = pygame.Color('Yellow')           # Ship color
        polygon = [(0, 0), (34, 10), (0, 20), (5, 10)]
        pygame.draw.polygon(self.art, self.color, polygon)

        # First version of the image is the permanent ship graphic
        self.image = self.art
        self.angle = 0  # Initial angle is cartesian coordinates 0

        # Movement
        self.vx = 0
        self.vy = 0


    def update(self):
        """Update the position and orientation of the ship.

        Should be called every frame, by the main game loop to allow the
        ship to move. Movements consist of x, y translation, and cartesian
        rotation (0 degrees = 3 o'clock).
        """

        # movement 
        self.rect.move_ip(self.vx, self.vy)
        screen_width, screen_height = (1024, 738)

        if (self.rect.center[0] < 0):
            self.rect.move_ip(screen_width, 0)
        elif (self.rect.center[0] >= screen_width):
            self.rect.move_ip(-screen_width, 0)

        if (self.rect.center[1] <0):
            self.rect.move_ip(0, screen_height)
        elif (self.rect.center[1] >= screen_height):
            self.rect.move_ip(0, -screen_height)

        # Set the image and rect, based on instance parameters
        # The image is a transform of the ship "art"
        self.image = pygame.transform.rotate(self.art, self.angle)
        # The rect is a rectangle centered on the x, y of the ship
        self.rect = self.image.get_rect(center=self.rect.center)


    def turnLeft(self):
        self.angle += 15
        if self.angle > 360:
            self.angle += 15


    def turnRight(self):
        self.angle -= 15 
        if self.angle < 0:
            self.angle = 345


    def thrust(self):
        self.vx = -3
        self.vy = -1

    def stop(self):
        self.vx = 0
        self.vy = 0
