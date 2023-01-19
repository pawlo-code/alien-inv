#modul sgame.py
import pygame

from shoot_point import ShootPoint
from weapon import Weapon
from bullet import Bullet
from button import Button
from settings import Settings

class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800,600))
        self.screen_rect = self.screen.get_rect()
        self.background = pygame.image.load("images/background.bmp")
        
        self.settings = Settings()
        self.weapon = Weapon(self)
        self.square = ShootPoint(self)
        self.button = Button(self, "Start Game")

        self.bullet_bool = False


    def _draw_bullet(self):
        if not self.bullet_bool:
            self.bullet = Bullet(self)
            self.bullet_bool = True

    def _check_collisions(self):
        if self.bullet.rect.colliderect(self.square.rect):
            self.bullet_bool = False
            self.settings.game_points += 1
            self.settings.increase_speed()
            pygame.time.delay(300)

    def _check_play_button(self, mousepos):
        if not self.settings.game_active:
            if self.button.rect.collidepoint(mousepos):
                self.settings.game_active = True

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.weapon.up_direction = True
                    elif event.key == pygame.K_DOWN:
                        self.weapon.down_direction = True
                    elif event.key == pygame.K_SPACE:
                        self._draw_bullet()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.weapon.up_direction = False
                    elif event.key == pygame.K_DOWN:
                        self.weapon.down_direction = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    self._check_play_button(mousepos)

            self.screen.blit(self.background, (0, 0))

            self._draw_sprites()

            if self.settings.game_active:
                self._update_events()
                self._check_win()

            pygame.display.flip()

    def _check_win(self):
        if self.settings.health_points == 0:
            pygame.time.delay(300)
            self._reset_game()

    def _reset_game(self):
        self.settings.initialize_dynamic_settings()
        self.weapon.center_weapon()
        self.square.center_rect()
        
    def _draw_sprites(self):
        self.square.draw()
        self.weapon.blitme()
        if not self.settings.game_active:
            self.button.draw()


    def _update_events(self):
        self.weapon.update()
        self.update_square()

        if self.bullet_bool:
            self.bullet.update()
            self.bullet.draw()
            self._check_collisions()


    def update_square(self):
        self.square.update()
        if self.square.rect.top < self.screen_rect.top:
            self.square.square_direction *= -1
        elif self.square.rect.bottom > self.screen_rect.bottom:
            self.square.square_direction *= -1

if __name__ == "__main__":
    game = Game()
    game.run_game()