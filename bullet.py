import pygame
import math

class Bullet(pygame.sprite.Sprite):
    
    # Position is coordinates of ship when fired
    # Angle is the angle the ship is when fired. 
    def __init__(self, screen, angle, position):
        super(pygame.sprite.Sprite, self).__init__()
        
        self.angle = angle
        self.position = position
        self.rect = pygame.Rect((0,0), (5,5))
        
        self.screen_width, self.screen_height = screen
        

        self.art = pygame.Surface(self.rect.size)
        self.art.set_colorkey(pygame.Color('Black')) 
        color = pygame.Color('white')
        pygame.draw.circle(self.art, color, self.rect.center, self.rect.width /2)
        
        self.rect.center = self.position
        self.distance = 0
        
    def update(self):
        radians = math.radians(self.angle)
        xv = 20 * math.cos(radians)
        yv = 20 * math.sin(radians)
        
        self.distance += math.sqrt(xv**2 + yv**2)
        if self.distance > self.screen_height * .75:
            return True
        self.rect.move_ip(xv, -yv)
        
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
    