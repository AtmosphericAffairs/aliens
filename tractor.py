import pygame

class Tractor():
    def __init__(self, screen):
        """создание начальной позиции полярника"""
        self.screen = screen
        self.image1 = pygame.image.load('images/tractorR1.gif')
        self.face = pygame.image.load('images/murad_game.bmp')
        
        self.rect = self.image1.get_rect(y = 620)
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx

        self.rect_face = self.face.get_rect(y = 520)
        self.rect_face.centerx = self.screen_rect.centerx

        self.mooving_right = False #флаг вправо
        self.mooving_left = False #флаг влево
        self.position = 0
        self.count_move = 1
        self.speed = 4


    def click_face(self, number_lolar):
        if number_lolar == 1:
            self.face =  pygame.image.load('images/murad_game.gif')
        elif number_lolar == 2:
            self.face =  pygame.image.load('images/misha_game.gif')
        elif number_lolar == 3:
            self.face =  pygame.image.load('images/vadim_game.gif')
        elif number_lolar == 4:
            self.face =  pygame.image.load('images/nikita_game.gif')
        elif number_lolar == 5:
            self.face =  pygame.image.load('images/roma_game.gif')
        elif number_lolar == 6:
            self.face =  pygame.image.load('images/maxim_game.gif')
        elif number_lolar == 7:
            self.face =  pygame.image.load('images/lesha_game.gif')
        elif number_lolar == 8:
            self.face =  pygame.image.load('images/yura_game.gif')
        elif number_lolar == 9:
            self.face =  pygame.image.load('images/anton_game.gif')
        elif number_lolar == 10:
            self.face =  pygame.image.load('images/fedor_game.gif')
        elif number_lolar == 11:
            self.face =  pygame.image.load('images/zahar_game.gif')
        self.rect_face = self.face.get_rect(y = 670)
        self.rect_face.centerx = self.screen_rect.centerx
        if number_lolar == 11:
            self.speed = 6
        else:
            self.speed = 4

            
    def position_update(self):
        if self.position == 0:
            self.position = 1
        elif self.position == 1:
            self.position = 0



    def update(self):
        """обновляет позицию трактора с учетом флагов"""
        if self.mooving_right:
            if self.rect.centerx < 1130:
                self.rect.centerx += self.speed
                self.count_move += 1
            else:
                self.rect.centerx = 1130
        if self.mooving_left:
            if self.rect.centerx > 70:
                self.rect.centerx -= self.speed
                self.count_move += 1
            else:
                self.rect.centerx = 70

        if (self.count_move % 20 )==0:
            self.position_update()

        if self.position == 0:
            self.image1 = pygame.image.load('images/tractorR1.gif')
        elif self.position == 1:
            self.image1 = pygame.image.load('images/tractorL1.gif')
        self.rect_face.centerx = self.rect.centerx
    def blitme(self):
        """прорисовка полярника в текущей позиции"""
        self.screen.blit(self.image1, self.rect)
        self.screen.blit(self.face, self.rect_face)