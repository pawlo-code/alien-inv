class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.load_high_score()
        self.reset_stats()
        
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def load_high_score(self):
        with open("high_score.txt", "r") as f:
            try:
                self.high_score = int(f.read())
            except:
                self.high_score = 0

    def save_high_score(self, score):
        with open("high_score.txt", "w") as f:
            print(f.write(str(score)))