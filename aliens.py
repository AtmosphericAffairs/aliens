import pygame

import random

class Alien():
    def __init__(self, screen):
        self.x = 600
        self.y = 70
        """создание начальной позиции корабля"""
        self.screen = screen
        self.image3 = pygame.image.load('images/plate2.gif')
        self.rect = self.image3.get_rect()
        self.image4 = pygame.image.load('images/faer1.gif')
        self.rect1 = self.image4.get_rect()

        self.moove_aliens = True
        
        self.rect.x = self.x
        self.rect.y = self.y

        self.rect1.x = 0
        self.rect1.y = 0

        self.count_aliens = []
        self.count_faer_aliens = []

        self.speed_x = 2
        self.speed_y = 1

        self.count = 0

    def add_aliens(self):
        """Появление пришельцев"""
        self.moove = random.randint(1, 2)
        self.x = random.randint(100, 900)
        self.count_aliens.append([self.x, self.y, random.randint(1, 2)])
        
    def delete_aliens(self, count_menu, ai_setting):
        """Касание земли"""
        for i in self.count_aliens.copy():
            if i[1] >= 660:
                self.count_aliens.remove(i)
                count_menu.hit_points -=1
                print(str(count_menu.hit_points) + 'количество жизней')
                if count_menu.hit_points == (-1):
                    ai_setting.start_game = 1

    def update(self):
        """Скорость пришельцев"""
        for i in self.count_aliens:
            i[1] += self.speed_y
            if i[2] == 1:
                i[0] += self.speed_x
                if i[0] > 1100:
                    i[2] =2
            elif i[2] ==2:
                i[0] -= self.speed_x
                if i[0] < 20:
                    i[2] =1

    def blitme(self, i): 
        """прорисовка корабля в текущей позиции"""
        self.screen.blit(self.image3, (i[0], i[1]))
    
    def blitme_faer(self, i): 
        """прорисовка взрыва"""
        self.screen.blit(self.image4, (i[0], i[1]))
        self.count += 1
        if self.count == 199:
            self.count_faer_aliens.pop()
        elif self.count == 200:
            self.count = 0