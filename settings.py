class Settings():

    def __init__(self):
        # Screen parameters
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet parameters
        #self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Alien settings
        # self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 1
        self.ship_speed_factor = 1.5
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *=  self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
