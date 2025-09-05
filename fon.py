import pygame

class Fon():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('fon_image2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.count_alien = 0

    def blitme(self):
        """прорисовка фона"""
        self.screen.blit(self.image, self.rect)