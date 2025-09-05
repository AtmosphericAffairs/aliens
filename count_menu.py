import pygame
import random
import time

class Count_Menu():

    def __init__(self, screen):
        self.screen = screen
        self.beer_hp = pygame.image.load('images/beer_hp.gif')
        self.vodka = pygame.image.load('images/vodka.gif')
        
        self.count_alien = 0
        self.point = 0
        self.level = 0
        self.event_alien = 1500
        self.game_level = 1
        self.hit_points = 3
        self.setting_count = pygame.font.SysFont('Comic Sans MS', 18)
        self.beer_cords = [600, 700, random.randint(1, 2)]
        self.timer_vodka = 0
        self.count_timer = 3
        self.bonus_count = 3
        self.bonus = False
        self.text_level = False
        self.text_level_time = 0


    def click_bonus(self):
        if self.bonus_count:
            self.bonus_count -= 1



    def f_text_level(self):
        self.text_level_time += 1
        if self.text_level_time == 600:
            self.text_level = False
            self.text_level_time = 0

        


    def beer_moove(self, aliens, snow):
        """Движение пива"""
        if self.beer_cords[2] == 1:
            self.beer_cords[0] += 5
            if self.beer_cords[0] > 1150:
                self.beer_cords[2] = 2
        elif self.beer_cords[2] == 2:
            self.beer_cords[0] -= 5
            if self.beer_cords[0] < 50:
                self.beer_cords[2] = 1
        self.beer_cords[1] -= 1
        if self.beer_cords[1] < 10:
            aliens.moove_aliens = True
            self.beer_cords = [600, 700, random.randint(1, 2)]
        for i in snow.count_snow:
            if i[0] < (self.beer_cords[0] + 40) and i[0] > (self.beer_cords[0]) and i[1] < (self.beer_cords[1]+46) and i[1] > self.beer_cords[1]:
                snow.count_snow.remove(i)
                aliens.moove_aliens = True
                self.beer_cords = [600, 700, random.randint(1, 2)]
                self.hit_points += 1

        

    def blitme(self, aliens):
        """прорисовка пива, количество тарелок"""
        self.count_screen = self.setting_count.render(('Сбито тарелок: ' + str(self.count_alien)), True, ('black'))
        self.screen.blit(self.count_screen, (1000, 10))
        self.count_screen1 = self.setting_count.render('Жизни: ', True, ('black'))
        self.screen.blit(self.count_screen1, (50, 10))
        self.count_screen2 = self.setting_count.render('40 градусный пулемёт: ', True, ('black'))
        self.screen.blit(self.count_screen2, (685, 10))
        self.count_screen3 = self.setting_count.render('Выжрано! ', True, ('red'))
        #прорисовка жизней
        if self.hit_points > 0:
            x = 110
            for i in range(self.hit_points):
                self.screen.blit(self.beer_hp, (x, (-3)))
                x += 20
        #прориовка водки
        if self.bonus_count:
            x = 900
            for i in range(self.bonus_count):
                self.screen.blit(self.vodka, (x, 5))
                x += 20

        if self.bonus_count == 0:
            self.screen.blit(self.count_screen3, (900, 10))
        if aliens.moove_aliens == False:
            self.screen.blit(self.beer_hp, (self.beer_cords[0], self.beer_cords[1]))
        if self.text_level:
            lvl = self.setting_count.render(('Уровень ' + str(self.game_level)), True, ('black'))
            self.screen.blit(lvl, (550, 500))


