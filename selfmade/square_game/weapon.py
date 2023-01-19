import pygame

class Weapon:
    def __init__(self, ai_game):
    
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/pistol.png')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.up_direction = False
        self.down_direction = False

    def center_weapon(self):
        self.rect.midleft = self.screen_rect.midleft

    def update(self):
        if self.up_direction:
            self.rect.y -= self.ai_game.settings.weapon_speed
        elif self.down_direction:
            self.rect.y += self.ai_game.settings.weapon_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

