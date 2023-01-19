import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/spacecraft.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.x = self.screen_rect.midbottom[0]

        self.x = float(self.rect.x)
            
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right - 10:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left + 10:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        self.x = float(self.screen_rect.midbottom[0])

    def blitme(self):
        self.screen.blit(self.image, self.rect)