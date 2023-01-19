from pygame.sprite import Sprite
import pygame

class Gwiazdy(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.image = pygame.image.load('selfmade/gwiazdy/star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        