import sys

import pygame

from deszcz import Deszcz

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.krople = pygame.sprite.Group()
        self._create_rain()

    def _create_rain(self):
        rain = Deszcz()
        available_drops = self.screen_rect.width // (2 * rain.rect.width)
        available_rows = self.screen_rect.height // (2 * rain.rect.height)
        for row in range(available_rows):
            for drop in range(available_drops):
                rain = Deszcz()
                rain.rect.x = rain.rect.width + 2 * rain.rect.width * drop
                rain.rect.y = rain.rect.height + 2 * rain.rect.height * row
                self.krople.add(rain)

    def _update_drops(self):
        self.krople.draw(self.screen)
        self.krople.update()
        for kropla in self.krople.copy():
            if kropla.rect.y > self.screen_rect.bottom:
                kropla.rect.bottom = 0

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            self.screen.fill(pygame.Color('black'))
            self._update_drops()
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()