import pygame
from pygame.sprite import Sprite

class Deszcz(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('selfmade/krople/kropla.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        self.rect.y += 1
        