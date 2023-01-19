import pygame

class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 720))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.fill((0, 0, 255))
            
            pygame.display.flip()

ai = Game()
ai.run_game()
