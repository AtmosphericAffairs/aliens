
import pygame

from setting import Setting

from starttext import StartText

from tractor import Tractor

from snow import Snow

from aliens import Alien

from fon import Fon

from fon2 import Fon2

from fon3 import Fon3


from count_menu import Count_Menu

import game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Пришельцы')
    fon = Fon(screen)
    fon2 = Fon2(screen)
    fon3 = Fon3(screen)
    startext = StartText(screen)
    tractor = Tractor(screen)
    aliens = Alien(screen)
    snow = Snow(screen, tractor)
    count_menu = Count_Menu(screen)
    clock = pygame.time.Clock()
    gf.levelUp(1500)
    pygame.mixer.music.load('sound/kalambur.mp3')
    
    
    while True:
        if ai_setting.start_game == 0:
            time_passed = clock.tick(50)
            fon2.blitme()
            gf.check_events_start(ai_setting, fon3)
            gf.update_screen_start(screen, startext)

        elif ai_setting.start_game == 1:
            fon3.blitme(tractor)
            gf.check_events_start(ai_setting, fon3)
            gf.update_screen_menu(screen)
            count_menu.hit_points = 3

        elif ai_setting.start_game == 2:
            time_passed = clock.tick(200)
            gf.check_events(tractor, snow, aliens, ai_setting, fon3, count_menu)
            tractor.update()
            snow.update()
            snow.delete_snow()
            fon.blitme()
            aliens.delete_aliens(count_menu, ai_setting)
            aliens.update()
            snow.faer_snow(tractor, ai_setting, fon3.number_lolar)
            if aliens.moove_aliens == False:
                if count_menu.text_level:
                    count_menu.f_text_level()
                else:
                    count_menu.beer_moove(aliens, snow)
            gf.kill_alien(snow, aliens, ai_setting, count_menu)
            count_menu.blitme(aliens)
            gf.update_screen(screen, tractor, snow, aliens)
            gf.vodka_bonus(count_menu, snow)
            

run_game()