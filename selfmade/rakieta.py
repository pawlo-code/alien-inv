import sys

import pygame

class RocketGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,720))

        self.champ = pygame.image.load('selfmade/champ.bmp')
        self.champ_rect = self.champ.get_rect()


        self.champ_rect.center = self.screen.get_rect().center

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def show_champ(self):
        self.screen.blit(self.champ, self.champ_rect)

    def update_positions(self):
        if self.moving_up  and self.champ_rect.top > self.screen.get_rect().top:
            self.champ_rect.y -= 1
        if self.moving_down and self.champ_rect.bottom < self.screen.get_rect().bottom:
            self.champ_rect.y += 1
        if self.moving_left and self.champ_rect.left > self.screen.get_rect().left:
            self.champ_rect.x -= 1
        if self.moving_right and self.champ_rect.right < self.screen.get_rect().right:
            self.champ_rect.x += 1

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.moving_down = True
                    if event.key == pygame.K_LEFT:
                        self.moving_left = True
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.moving_down = False
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.moving_left = False

            self.update_positions()
            self.show_champ()
            pygame.display.flip()

ai = RocketGame()
ai.run_game()
        