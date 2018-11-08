
from pico2d import *

import game_framework
import Main_Screen

import GamePlay_screen
import GamePlay_screen2

name ="Character_select"
image = None
MeiMei_R=None
MeiMei_L=None
Wukung_R=None
Wukung_L=None
change=0

def enter():
    global image,MeiMei_R,MeiMei_L,Wukung_R,Wukung_L
    image = load_image('Resource_Screen\\character select.png')
    MeiMei_R= load_image('Resource_Screen\\MeiMei_R.png')
    MeiMei_L= load_image('Resource_Screen\\MeiMei_L.png')
    Wukung_R= load_image('Resource_Screen\\Wukung_R.png')
    Wukung_L= load_image('Resource_Screen\\Wukung_L.png')
    pass


def exit():
    global image,MeiMei_R,MeiMei_L,Wukung_R,Wukung_L
    del (image)
    del (MeiMei_R)
    del (MeiMei_L)
    del (Wukung_R)
    del (Wukung_L)
    pass


def pause():
    pass


def handle_events():
    global change
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(Main_Screen)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                change=1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                change = 2
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE)and change==1:
                game_framework.change_state(GamePlay_screen)

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE)and change==2:
                game_framework.change_state(GamePlay_screen2)

    pass


def draw():
    global change
    clear_canvas()
    image.clip_draw(0,0,1100,812,512, 382)

    if change==1:
        MeiMei_R.clip_draw(0,0,230,300,100, 382)
        Wukung_L.clip_draw(0, 0, 230, 300, 900, 382)
    if change==2:
        Wukung_R.clip_draw(0,0,230,300,900, 382)
        MeiMei_L.clip_draw(0, 0, 230, 300, 100, 382)
    if change==0:
        Wukung_L.clip_draw(0, 0, 230, 300, 900, 382)
        MeiMei_L.clip_draw(0, 0, 230, 300, 100, 382)
    update_canvas()
    pass


def update():
    pass


def resume():
    pass