import pygame

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 720))
        self.character = pygame.image.load("selfmade/champ.bmp")
        self.character_ract = self.character.get_rect()
        self.character_ract.center = self.screen.get_rect().center

    def show_champ(self):
        self.screen.blit(self.character, self.character_ract)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.show_champ()
            pygame.display.flip()

ai = Game()
ai.run_game()