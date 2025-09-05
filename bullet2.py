import pygame


class Bullet():

    def __init__(self, screen, tractor):
        self.y = 540
        self.screen = screen
        self.bullet = pygame.draw.circle(screen, (255, 255, 255), (tractor.rect.centerx, self.y), 7 )


    def snow_moove():
        self.bullet = pygame.draw.circle(screen, (255, 255, 255), (tractor.rect.centerx, self.y - 1), 7 )

