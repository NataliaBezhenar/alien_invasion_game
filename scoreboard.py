import pygame.font


class Scoreboard:
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 34)
        self.top_indent = 20
        self.font1 = pygame.font.SysFont(None, 20)
        self.text_color_annot = (200, 50, 10)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Converts the current points into a graphic image"""
        score_annot = "Current score"
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_annot_image = self.font1.render(score_annot, True, self.text_color_annot,
                                                   self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_annot_image_rect = self.score_annot_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_annot_image_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.top_indent + self.score_annot_image_rect.height
        self.score_annot_image_rect.top = self.top_indent

    def prep_high_score(self):
        """Converts the high score into a graphic image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        high_score_annotation = "High score"
        self.high_score_image_annot = self.font1.render(high_score_annotation, True, self.text_color_annot,
                                                       self.ai_settings.bg_color)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_image_annot_rect = self.high_score_image_annot.get_rect()
        self.high_score_rect.top = self.top_indent + self.high_score_image_annot_rect.height
        self.high_score_image_annot_rect.centerx = self.screen_rect.centerx
        self.high_score_image_annot_rect.top = self.top_indent

    def prep_level(self):
        """Converts current game level into a graphic image"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        prep_level_annot = "Level"
        self.prep_level_annot_image= self.font1.render(prep_level_annot, True, self.text_color_annot,
                                                        self.ai_settings.bg_color)
        self.prep_level_annot_image_rect = self.prep_level_annot_image.get_rect()
        self.prep_level_annot_image_rect.right = self.score_rect.right
        self.prep_level_annot_image_rect.top = self.score_rect.bottom
        self.level_rect.top = self.prep_level_annot_image_rect.bottom

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.high_score_image_annot, self.high_score_image_annot_rect)
        self.screen.blit(self.score_annot_image, self.score_annot_image_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.prep_level_annot_image, self.prep_level_annot_image_rect)

