import pygame

class Fon3():
    def __init__(self, screen):
        self.text = 'Выберите полярника, который примет неравный бой против пришельцев с Нибиру'
        self.text_mouse = '(Используйте мышь)'
        self.number_lolar = False
        self.lst_name = ['Мурад', 'Михаил' , 'Вадим', 'Никита', 'Рома', 'Максим', 'Алексей', 'Юрий', 'Антон', 'Федор', 'Захар']
        self.text_murad = ' - Мурад Аскеров,'
        self.text_murad1 = ' зав. производством'
        self.text_misha = ' - Михаил Филиппов'
        self.text_misha1 = ' механик ДЭС'
        self.text_vadim = ' - Вадим Сабодаш'
        self.text_vadim1 = ' врач-хирург'
        self.text_nikita = ' - Никита Смирнов'
        self.text_nikita1 = ' метеоролог'
        self.text_roma = ' - Роман Абрамов'
        self.text_roma1 = ' механик-водитель'
        self.text_maxim = 'Максим Шереметов - '
        self.text_maxim1 = ' магнитолог'
        self.text_lesha = 'Алексей Климов - '
        self.text_lesha1 = 'Инженер - электромеханик '
        self.text_yura = 'Юрий Серов - '
        self.text_yura1 = 'геофизик '
        self.text_anton = 'Антон Першин - '
        self.text_anton1 = 'Главный механик '
        self.text_fedor = 'Федор Шипулин - '
        self.text_fedor1 = 'Врач анастезиолог '
        self.text_z = 'Акулов '
        self.text_z1 = 'Захар '
        self.text_z2 = 'Валерьевич'
        self.text_z3 = 'Начальник cтанции'
        self.text_z4 = '"ВОСТОК"'
        self.screen = screen

        
        self.font = pygame.font.SysFont('Comic Sans MS', 27)
        self.font_name = pygame.font.SysFont('Comic Sans MS', 20)
        
        self.murad = pygame.image.load('images/murad.bmp')
        self.misha = pygame.image.load('images/misha.bmp')
        self.vadim = pygame.image.load('images/vadim.bmp')
        self.nikita = pygame.image.load('images/batya.bmp')
        self.roma = pygame.image.load('images/roma.bmp')
        self.maxim = pygame.image.load('images/maxim.bmp')
        self.lesha = pygame.image.load('images/lesha.bmp')
        self.yura = pygame.image.load('images/yura.bmp')
        self.anton = pygame.image.load('images/anton.bmp')
        self.fedor = pygame.image.load('images/fedya.bmp')
        self.zahar = pygame.image.load('images/zahar.bmp')


        self.rect_mu = pygame.Rect(70, 100, 100, 100)
        self.rect_mi = pygame.Rect(70, 195, 100, 100)
        self.rect_va = pygame.Rect(70, 300, 100, 100)
        self.rect_ni = pygame.Rect(70, 405, 100, 100)
        self.rect_ro = pygame.Rect(70, 510, 100, 100)
        self.rect_ma = pygame.Rect(1030, 100, 100, 100)
        self.rect_le = pygame.Rect(1030, 205, 100, 100)
        self.rect_yu = pygame.Rect(1030, 307, 100, 100)
        self.rect_an = pygame.Rect(1030, 405, 100, 100)
        self.rect_fe = pygame.Rect(1030, 510, 100, 100)
        self.rect_za = pygame.Rect(500, 250, 150, 186)

    def blitme(self, tractor):
        self.screen.fill((120, 200, 120))

            #настройки текста
        self.text_screen = self.font.render(self.text, True, (0, 0, 255))
        self.text_screen_mouse = self.font.render(self.text_mouse, True, (0, 0, 255))
        self.text_screen1 = self.font_name.render(self.text_murad, True, (0, 0, 255))
        self.text_screen2 = self.font_name.render(self.text_murad1, True, (0, 0, 255)) 
        self.text_screen3 = self.font_name.render(self.text_misha, True, (0, 0, 255)) 
        self.text_screen4 = self.font_name.render(self.text_misha1, True, (0, 0, 255))
        self.text_screen5 = self.font_name.render(self.text_vadim, True, (0, 0, 255))
        self.text_screen6 = self.font_name.render(self.text_vadim1, True, (0, 0, 255))
        self.text_screen7 = self.font_name.render(self.text_nikita, True, (0, 0, 255))
        self.text_screen8 = self.font_name.render(self.text_nikita1, True, (0, 0, 255))
        self.text_screen9 = self.font_name.render(self.text_roma, True, (0, 0, 255))
        self.text_screen10 = self.font_name.render(self.text_roma1, True, (0, 0, 255))
        self.text_screen11 = self.font_name.render(self.text_maxim, True, (0, 0, 255))
        self.text_screen12 = self.font_name.render(self.text_maxim1, True, (0, 0, 255))
        self.text_screen13 = self.font_name.render(self.text_lesha, True, (0, 0, 255))
        self.text_screen14 = self.font_name.render(self.text_lesha1, True, (0, 0, 255))
        self.text_screen15 = self.font_name.render(self.text_yura, True, (0, 0, 255))
        self.text_screen16 = self.font_name.render(self.text_yura1, True, (0, 0, 255))
        self.text_screen17 = self.font_name.render(self.text_anton, True, (0, 0, 255))
        self.text_screen18 = self.font_name.render(self.text_anton1, True, (0, 0, 255))
        self.text_screen19 = self.font_name.render(self.text_fedor, True, (0, 0, 255))
        self.text_screen20 = self.font_name.render(self.text_fedor1, True, (0, 0, 255))

        self.text_screen21 = self.font_name.render(self.text_z, True, (170, 0, 0))
        self.text_screen22 = self.font_name.render(self.text_z1, True, (170, 0, 0))
        self.text_screen23 = self.font_name.render(self.text_z2, True, (170, 0, 0))
        self.text_screen24 = self.font_name.render(self.text_z3, True, (170, 0, 0))
        self.text_screen25 = self.font_name.render(self.text_z4, True, (170, 0, 0))


        self.screen.blit(self.text_screen_mouse, (490, 45))
        self.screen.blit(self.text_screen, (55, 20))
            #прорисовка фото
        self.screen.blit(self.murad, (70, 100))
        self.screen.blit(self.misha, (70, 195))
        self.screen.blit(self.vadim, (70, 300))
        self.screen.blit(self.nikita, (70, 405))
        self.screen.blit(self.roma, (70, 510))
        self.screen.blit(self.maxim, (1030, 100))
        self.screen.blit(self.lesha, (1030, 205))
        self.screen.blit(self.yura, (1030, 310))
        self.screen.blit(self.anton, (1030, 415))
        self.screen.blit(self.fedor, (1030, 520))
        self.screen.blit(self.zahar, (500, 250))

            #прорисовка текста
        self.screen.blit(self.text_screen1, (170, 130))
        self.screen.blit(self.text_screen2, (177, 151))
        self.screen.blit(self.text_screen3, (170, 230))
        self.screen.blit(self.text_screen4, (177, 251))
        self.screen.blit(self.text_screen5, (170, 330))
        self.screen.blit(self.text_screen6, (177, 351))
        self.screen.blit(self.text_screen7, (170, 430))
        self.screen.blit(self.text_screen8, (177, 453))
        self.screen.blit(self.text_screen9, (170, 530))
        self.screen.blit(self.text_screen10, (177, 553))
        self.screen.blit(self.text_screen11, (810, 130))
        self.screen.blit(self.text_screen12, (870, 151))
        self.screen.blit(self.text_screen13, (835, 230))
        self.screen.blit(self.text_screen14, (750, 251))
        self.screen.blit(self.text_screen15, (880, 330))
        self.screen.blit(self.text_screen16, (900, 351))
        self.screen.blit(self.text_screen17, (860, 430))
        self.screen.blit(self.text_screen18, (840, 453))
        self.screen.blit(self.text_screen19, (845, 530))
        self.screen.blit(self.text_screen20, (840, 553))
        self.screen.blit(self.text_screen21, (530, 175))
        self.screen.blit(self.text_screen22, (535, 196))
        self.screen.blit(self.text_screen23, (510, 217))
        self.screen.blit(self.text_screen24, (477, 430))
        self.screen.blit(self.text_screen25, (525, 451))


        if self.number_lolar:
            """Выбор игрока"""
            if self.number_lolar == 11:
                self.text1 = 'Это лучший выбор!!! Захар Валерьевич готов противостоять инопланетным ордам!'
                self.text_screen_click = self.font.render(self.text1, True, (170, 0, 0))
                self.screen.blit(self.text_screen_click, (50, 700))
            else:
            
                self.text1 = 'Не лучший выбор, но ' + self.lst_name[self.number_lolar-1] + ' готов принять неравный бой'
                self.text_screen_click = self.font.render(self.text1, True, (0, 0, 255))
                self.screen.blit(self.text_screen_click, (200, 700))
            text_button = 'Чтоб начать - нажмите ENTER'    
            self.text_screen_button = self.font.render(text_button, True, (0, 0, 255))
            self.screen.blit(self.text_screen_button, (400, 731))
            tractor.click_face(self.number_lolar)

