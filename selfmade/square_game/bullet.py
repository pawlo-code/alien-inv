import pygame

class Bullet():
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.ai_game = ai_game

        self.color = (0, 0, 0)
        self.rect = pygame.Rect(0, 0, 9, 9)
        self.rect.midleft = ai_game.weapon.rect.topright

    def update(self):
        self.rect.x += self.ai_game.settings.bullet_speed
        if self.rect.x > self.screen_rect.width:
            self.ai_game.bullet_bool = False
            self.settings.health_points -= 1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, 5)