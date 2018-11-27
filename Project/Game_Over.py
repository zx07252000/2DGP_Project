
from pico2d import *
import game_framework
import Main_Screen
import GamePlay_screen2

name = "Stage_Clear"
image = None
logo_time=0.0

def enter():
    global image

    image=load_image('Resource_Screen\\Game_Over.png')

    pass

def exit():
    global image
    del (image)
    pass

def handle_events():
    events = get_events()


    pass

def draw():
    global image
    clear_canvas()
    image.clip_draw(30, 100, 1020, 1020, 512, 450)
    update_canvas()
    pass

def update():
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(Main_Screen)
    delay(0.01)
    logo_time += 0.01
    pass


def pause():
    pass


def resume():
    pass







