import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class reproduces single alien"""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('pictures/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """Saving actual alien position"""
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Moves alien to the right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)

        print("updated: x = " + str(self.x))
        self.rect.x = self.x

    def check_edges(self):
        """Returns True if alien in the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            print("reached right edge " + str(self.rect.right))
            return True
        elif self.rect.left <= 0:
            print("reached left edge: " + str(self.rect.left))
            return True