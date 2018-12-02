
from pico2d import *

import game_framework
import Main_Screen

import GamePlay_Stage1
import GamePlay_Stage2


name ="Character_select"
Character_Select_Screen = None
Choose_MeiMei=None
Not_Choose_MeiMei=None
Choose_Wukung=None
Not_Choose_Wukung=None

Character_Change=0
No_Choice=0
MeiMei=1
Wukung=2

def enter():
    global Character_Select_Screen,Choose_MeiMei,Not_Choose_MeiMei,Choose_Wukung,Not_Choose_Wukung,Character_select_bgm
    Character_Select_Screen = load_image('Resource_Screen\\character select.png')
    Choose_MeiMei= load_image('Resource_Screen\\MeiMei_R.png')
    Not_Choose_MeiMei= load_image('Resource_Screen\\MeiMei_L.png')
    Choose_Wukung= load_image('Resource_Screen\\Wukung_R.png')
    Not_Choose_Wukung= load_image('Resource_Screen\\Wukung_L.png')

    Character_select_bgm = load_music('Resource_Bgm\\Character_select.wav')
    Character_select_bgm.set_volume(64)

    pass


def exit():
    global Character_Select_Screen,Choose_MeiMei,Not_Choose_MeiMei,Choose_Wukung,Not_Choose_Wukung
    del (Character_Select_Screen)
    del (Choose_MeiMei)
    del (Not_Choose_MeiMei)
    del (Choose_Wukung)
    del (Not_Choose_Wukung)
    pass


def pause():
    pass


def handle_events():
    global Character_Change,MeiMei,Wukung

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(Main_Screen)
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                Character_select_bgm.play()

                Character_Change= MeiMei
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                Character_select_bgm.play()

                Character_Change = Wukung
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE)and Character_Change==MeiMei:
                game_framework.change_state(GamePlay_Stage2)
                Main_Screen.bgm.__del__()
                Character_select_bgm.stop()


            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE)and Character_Change==Wukung:
                game_framework.change_state(GamePlay_Stage2)
                Main_Screen.bgm.__del__()
                Character_select_bgm.stop()


    pass


def draw():
    global Character_Change
    clear_canvas()
    Character_Select_Screen.clip_draw(0,0,1100,812,512, 382)

    if Character_Change==MeiMei:
        Choose_MeiMei.clip_draw(0,0,230,300,100, 382)
        Not_Choose_Wukung.clip_draw(0, 0, 230, 300, 900, 382)
    if Character_Change==Wukung:
        Choose_Wukung.clip_draw(0,0,230,300,900, 382)
        Not_Choose_MeiMei.clip_draw(0, 0, 230, 300, 100, 382)
    if Character_Change==No_Choice:
        Not_Choose_Wukung.clip_draw(0, 0, 230, 300, 900, 382)
        Not_Choose_MeiMei.clip_draw(0, 0, 230, 300, 100, 382)
    update_canvas()
    pass


def update():
    pass


def resume():
    pass