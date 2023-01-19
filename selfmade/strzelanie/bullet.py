import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.ship = ai_game.ship_rect

        self.bullet_rect = pygame.Rect(0, 0, 35, 5)

        self.bullet_rect.midleft = self.ship.midright

    def draw_bullet(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.bullet_rect)

    def update(self):
        self.bullet_rect.x += 1

    
        