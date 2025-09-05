import pygame

class Setting():
    """Класс для хранения настроек"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.start_game = 0
        self.sound1 = pygame.mixer.Sound('sound/vistrel.wav')
        self.sound2 = pygame.mixer.Sound('sound/bam.wav')
       