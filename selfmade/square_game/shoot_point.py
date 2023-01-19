#moduł shoot_point.py --
import pygame

class ShootPoint:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.settings = ai_game.settings

        self.square_color = (253, 221, 141)
        self.rect = pygame.Rect(0, 0, 80, 160)
        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)
        self.square_direction = 1

    def center_rect(self):
        self.rect.midright = self.screen_rect.midright

    def update(self):
        self.y = self.y + (self.settings.square_speed * self.square_direction)
        self.rect.y = self.y

    def draw(self):
        self.screen.fill(self.square_color, self.rect)

