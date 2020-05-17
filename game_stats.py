import os


class GameStats:
    """Tracking game statistics"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        file_name = "hiscore.txt"
        if os.path.exists(file_name):
            file = open(file_name, "r")
            self.high_score = int(file.read())
        else:
            self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
