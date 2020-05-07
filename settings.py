class Settings:
    """Class for the game settings storing"""

    def __init__(self):
        # Screen parameters
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_limit = 3

        # Bullet parameters
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Alien settings
        self.fleet_drop_speed = 50
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.alien_speed_factor = 0.3
        self.bullet_speed_factor = 1
        self.ship_speed_factor = 1.5
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increases speed settings and value of the aliens"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
