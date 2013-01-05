import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self, screen):
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

    def update(self):
        """"""
        self.angle += 10
        self.image = pygame.transform.rotate(self.art, self.angle)
        if self.angle == 360:
            self.angle = 0
        self.rect = self.image.get_rect(center=self.rect.center)
