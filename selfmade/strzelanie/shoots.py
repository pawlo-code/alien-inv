import sys

import pygame
from pygame.sprite import Sprite
from bullet import Bullet

class Game(Sprite):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 720))
        self._create_ship()
        self.bullets = pygame.sprite.Group()

    def _create_ship(self):
        self.ship = pygame.image.load('selfmade/strzelanie/ship.bmp')
        self.ship_rect = self.ship.get_rect()
        self.ship_rect.midleft = self.screen.get_rect().midleft
        self.moving_up = False
        self.moving_down = False

    def _move_ship(self):
        if self.moving_up:
            self.ship_rect.y -= 1
        if self.moving_down:
            self.ship_rect.y += 1
        
    def _set_ship(self):
        self.screen.blit(self.ship, self.ship_rect)

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def run_game(self):
        while True:
            self._check_events()


            self.screen.fill((0,0,0))
            self._set_ship()
            self._move_ship()
            self._bullets_update()
            
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False

    def _bullets_update(self):
        self.bullets.update()
            
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        print(len(self.bullets.sprites()))

        for bullet in self.bullets.copy():
            if bullet.bullet_rect.x >= 1200:
                self.bullets.remove(bullet)

        

if __name__ == "__main__":
    game = Game()
    game.run_game()