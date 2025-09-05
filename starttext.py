import pygame

class StartText():

    def __init__(self, screen):
        self.text_count1 = ['Антарктида, ст. Восток 2024 год...', 'После пятничного пива, магнитолог, геофизик и метеоролог,' +
            'сравнив результаты наблюдений, пришли к неоднозначному выводу...', 'На станцию "Восток" готовится ИНОПЛАНЕТНОЕ ВТОРЖЕНИЕ!',
            'На камбузе прошло совещание станции, на котором было принято единственное верное решение:', 'Попросить механиков ДЭС сделать из последнего '+
            'пылесоса космический снежкомёт, для противостояния внеземным захватчикам!', 'Чтобы начать противостоять, нажмите ENTER!']
        self.screen = screen
        self.font = pygame.font.SysFont('Comic Sans MS', 40)
        self.font2 = pygame.font.SysFont('Comic Sans MS', 18)
        self.image_beer = pygame.image.load('images/beer.bmp')
        self.image_plate = pygame.image.load('images/plate_text.gif')
        self.image_pilesos = pygame.image.load('images/pilesos.bmp')
        self.count1 = [0, 0, 0, 0, 0, 0]
        self.text1 = [' ', ' ', ' ', ' ', ' ', ' ']
        self.number_str = 0
        self.beer = False
        self.plate = False
        self.pilesos = False
        
    def blitme(self):
        self.text_screen1 = self.font.render(self.text1[0], True, (0, 0, 255))
        self.text_screen2 = self.font2.render(self.text1[1], True, (255, 0, 50))
        self.text_screen3 = self.font2.render(self.text1[2], True, (255, 0, 50))
        self.text_screen4 = self.font2.render(self.text1[3], True, (255, 0, 100))
        self.text_screen5 = self.font2.render(self.text1[4], True, (255, 0, 100))
        self.text_screen6 = self.font.render(self.text1[5], True, (255, 0, 0))
        if self.number_str == 0:
            if self.count1[0] < len(self.text_count1[0]):
                self.text1[0] += self.text_count1[0][self.count1[0]]
                self.count1[0] += 1
            elif self.count1[0] == len(self.text_count1[0]):
                self.number_str = 1
                self.count1[0] = [False]
        if self.number_str == 1:
            if self.count1[1] < len(self.text_count1[1]):
                self.text1[1] += self.text_count1[1][self.count1[1]]
                self.count1[1] += 1
            elif self.count1[1] == len(self.text_count1[1]):
                self.beer = True
                self.number_str = 2
                self.count1[1] = [False]
        if self.number_str == 2:
            if self.count1[2] < len(self.text_count1[2]):
                self.text1[2] += self.text_count1[2][self.count1[2]]
                self.count1[2] += 1
            elif self.count1[2] == len(self.text_count1[2]):
                self.plate = True
                self.number_str = 3
                self.count1[2] = [False]
        if self.number_str == 3:
            if self.count1[3] < len(self.text_count1[3]):
                self.text1[3] += self.text_count1[3][self.count1[3]]
                self.count1[3] += 1
            elif self.count1[3] == len(self.text_count1[3]):
                self.number_str = 4
                self.count1[3] = [False]
        if self.number_str == 4:
            if self.count1[4] < len(self.text_count1[4]):
                self.text1[4] += self.text_count1[4][self.count1[4]]
                self.count1[4] += 1
            elif self.count1[4] == len(self.text_count1[4]):
                self.pilesos = True
                self.number_str = 5
                self.count1[4] = [False]
        if self.number_str == 5:
            if self.count1[5] < len(self.text_count1[5]):
                self.text1[5] += self.text_count1[5][self.count1[5]]
                self.count1[5] += 1
            elif self.count1[5] == len(self.text_count1[5]):
                self.number_str = 6
                self.count1[5] = [False]
        self.screen.blit(self.text_screen1, (15, 50))
        self.screen.blit(self.text_screen2, (20, 100))
        self.screen.blit(self.text_screen3, (20, 125))
        if self.beer:
            self.screen.blit(self.image_beer, (300, 175))
        if self.plate:
            self.screen.blit(self.image_plate, (700, 190))
        if self.pilesos:
            self.screen.blit(self.image_pilesos, (500, 450))
        self.screen.blit(self.text_screen4, (20, 325))
        self.screen.blit(self.text_screen5, (20, 350))
        self.screen.blit(self.text_screen6, (180, 600))
