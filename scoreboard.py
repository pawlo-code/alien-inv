import pygame.font
from pygame.sprite import Group

from ship import Ship
from game_stats import GameStats

class Scoreboard(Group):

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_lvl()
        self.prep_ships()

    def prep_score(self):
        self.stats = self.ai_game.stats
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        self.stats = self.ai_game.stats
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.top = 20
        self.high_score_rect.centerx = self.screen_rect.centerx

    def prep_lvl(self):
        self.stats = self.ai_game.stats
        lvl = str(self.stats.level)
        self.lvl_image = self.font.render(lvl, True, self.text_color, self.settings.bg_color)
        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.y = self.score_rect.bottom + 10
        self.lvl_rect.right = self.screen_rect.right - 20

    def prep_ships(self):
        self.stats = self.ai_game.stats
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.ships.draw(self.screen)