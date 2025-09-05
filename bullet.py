import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_setting, screen, tractor):
        """Объект пули в позиции полярника"""
        super(Bullet, self).__init__()
        self.screen = screen
            #Создание пули в позиции (0.0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_setting.bullet.radius)
        self.rect.centerx = tractor.rect.centerx
        self.rect.top = tractor.rect.top

        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor


    def update(self):
        """Перемещение пули вверх по экрану"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def circle_bullet(self):
        pygame.draw.circle.rect(self.screen, self.color, self.rect)
