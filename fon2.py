import pygame

class Fon2():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/fon2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def blitme(self):
        """прорисовка фона"""
        self.screen.blit(self.image, self.rect)