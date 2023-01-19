import pygame
import sys

from gwiazdy import Gwiazdy

from random import randint

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

        self.gwiazdy = pygame.sprite.Group()

    def create_star(self):
        star = Gwiazdy(self)
        number_available_x = self.screen.get_width() // (2 * star.rect.width)
        number_available_y = self.screen.get_height()
        number_rows = number_available_y // (2 * star.rect.height)

        for row in range(number_rows):
            for number in range(number_available_x):
                star = Gwiazdy(self)
                rand_x = randint(0, self.screen.get_width())
                rand_y = randint(0, self.screen.get_height())
                star.rect.x = rand_x
                star.rect.y = rand_y
                self.gwiazdy.add(star)


    def run(self):
        self.create_star()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill((0,0,0))
            self.gwiazdy.draw(self.screen)
            print(len(self.gwiazdy))
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()