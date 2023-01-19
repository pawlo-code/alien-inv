
class Settings():
    def __init__(self):
        self.game_active = False

        self.health_points = 3
        self.game_points = 0
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.game_active = False
        self.health_points = 3
        self.game_points = 0
        self.weapon_speed = 1
        self.bullet_speed = 2
        self.square_speed = 0.5

    def increase_speed(self):
        self.square_speed *= self.speedup_scale
        self.weapon_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale