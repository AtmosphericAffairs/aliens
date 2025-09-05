import pygame

class Snow():
    def __init__(self, screen, tractor):
        self.screen = screen

        self.x = tractor.rect.centerx
        self.y = 640

        self.speed_factor = 2

        self.count_snow = []
        self.faer = False
        self.time_count = 0

    def faer_snow(self, tractor, ai_setting, number_lolar):
        if self.faer:
            self.time_count += 1
            if (self.time_count % 12) == 0:
                self.add_snow(tractor, ai_setting, number_lolar)

    def add_snow(self, tractor, ai_setting, number_lolar):
        if number_lolar == 11:
            self.x = tractor.rect.centerx
            self.count_snow.append([self.x, self.y])
            ai_setting.sound1.play()
        else:
            if self.faer:
                self.x = tractor.rect.centerx
                self.count_snow.append([self.x, self.y])
                ai_setting.sound1.play()
            else:
                if len(self.count_snow) < 3:
                    self.x = tractor.rect.centerx
                    self.count_snow.append([self.x, self.y])
                    ai_setting.sound1.play()

    def update(self):
        for i in self.count_snow:
            i[1] -=4

    def delete_snow(self):
        for i in self.count_snow.copy():
            if i[1] <= 0:
                self.count_snow.remove(i)
