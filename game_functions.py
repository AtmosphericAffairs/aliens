import sys
import pygame

def func_position(tractor):
    if tractor.position == 1:
        tractor.position = 0
    elif tractor.position == 0:
        tractor.position = 1

def play_music():
    pygame.mixer.music.play(-1)

def levelUp(a):
    pygame.time.set_timer(pygame.USEREVENT, a)


def check_events(tractor, snow, aliens, ai_setting, fon3, count_menu):
    """обработка событий нажатия клавиш"""
    
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            if aliens.moove_aliens:
                aliens.add_aliens()
        if event.type == pygame.QUIT:
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                tractor.mooving_right = True
                func_position(tractor)
            elif event.key == pygame.K_LEFT:
                tractor.mooving_left = True
                func_position(tractor)
            elif event.key == pygame.K_UP:
                if count_menu.bonus_count and count_menu.bonus == False:
                    count_menu.click_bonus()
                    count_menu.bonus = True
            if count_menu.bonus == False:
                if event.key == pygame.K_SPACE:
                    snow.add_snow(tractor, ai_setting, fon3.number_lolar)
            if count_menu.bonus:
                if event.key == pygame.K_SPACE:
                    snow.faer = True
                    snow.add_snow(tractor, ai_setting, fon3.number_lolar)
            
                

        elif event.type == pygame.KEYUP:
            tractor.count_move = 1
            if event.key == pygame.K_RIGHT:
                tractor.mooving_right = False
            elif event.key == pygame.K_LEFT:
                tractor.mooving_left = False
            if event.key == pygame.K_SPACE:
                snow.faer = False           
            
                
def check_events_start(ai_setting, fon3):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
        if ai_setting.start_game == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    ai_setting.start_game +=1
                    if ai_setting.start_game >= 2:
                        ai_setting.start_game = 2
        elif ai_setting.start_game == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()
                print(x)
                if fon3.rect_mu.collidepoint(x):
                    fon3.number_lolar = 1
                    
                elif fon3.rect_mi.collidepoint(x):
                    fon3.number_lolar = 2
                   
                elif fon3.rect_va.collidepoint(x):
                    fon3.number_lolar = 3
                    
                elif fon3.rect_ni.collidepoint(x):
                    fon3.number_lolar = 4
                    
                elif fon3.rect_ro.collidepoint(x):
                    fon3.number_lolar = 5
                    
                elif fon3.rect_ma.collidepoint(x):
                    fon3.number_lolar = 6
                    
                elif fon3.rect_le.collidepoint(x):
                    fon3.number_lolar = 7
                    
                elif fon3.rect_yu.collidepoint(x):
                    fon3.number_lolar = 8
                    
                elif fon3.rect_an.collidepoint(x):
                    fon3.number_lolar = 9
                    
                elif fon3.rect_fe.collidepoint(x):
                    fon3.number_lolar = 10
                    
                elif fon3.rect_za.collidepoint(x):
                    fon3.number_lolar = 11
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if ai_setting.start_game == 1 and fon3.number_lolar == False:
                        pass
                    else:
                        play_music()
                        ai_setting.start_game +=1
                        if ai_setting.start_game >= 2:
                            ai_setting.start_game = 2


def kill_alien(snow, aliens, ai_setting, count_menu):
    for i in snow.count_snow:
        for j in aliens.count_aliens:
            if i[0] < (j[0] + 100) and i[0] > (j[0]-10) and i[1] < (j[1]+69) and i[1] > j[1]:
                snow.count_snow.remove(i)
                aliens.count_aliens.remove(j)
                aliens.count_faer_aliens.append(j)
                ai_setting.sound2.play()
                count_menu.count_alien += 1
                count_menu.level += 1
                if aliens.moove_aliens:
                    if count_menu.level == 10:

                        aliens.moove_aliens = False
                        if (count_menu.game_level % 2) == 0:
                            aliens.speed_x += 1
                            count_menu.game_level +=1
                            print(count_menu.game_level)
                        else:
                            count_menu.event_alien -= 300
                            levelUp(count_menu.event_alien)
                            count_menu.game_level +=1
                            print(count_menu.game_level)
                        count_menu.level = 0
                        count_menu.text_level = True
                        count_menu.f_text_level()



def vodka_bonus(count_menu, snow):
    if count_menu.bonus:
        count_menu.timer_vodka +=1
        if (count_menu.timer_vodka % 200) == 0:
            count_menu.count_timer -= 1
        if count_menu.count_timer == 0:
            count_menu.count_timer = 3
            count_menu.bonus = False
            snow.faer = False
        print(count_menu.count_timer)


def update_screen(screen, tractor, snow, aliens):
    for i in snow.count_snow:
        pygame.draw.circle(screen, (255, 255, 255), (i[0], i[1]), 7 )
    for i in aliens.count_aliens:
        if len(aliens.count_aliens) > 0:
            aliens.blitme(i)
    for i in aliens.count_faer_aliens:
        if len(aliens.count_aliens) > 0:
            aliens.blitme_faer(i)
    tractor.blitme()
    pygame.display.flip()

def update_screen_start(screen, startext):
    startext.blitme()
    pygame.display.flip()

def update_screen_menu(screen):
    pygame.display.flip()
