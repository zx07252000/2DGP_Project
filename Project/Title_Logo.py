import game_framework
from pico2d import *
import Main_Screen


name = "TitleLogo"
image = None
logo_time=0.0

def enter():
    global image
    image = load_image('Resource_Screen\\Title_Logo.png')
    pass


def exit():
    global image
    del (image)
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

def draw():
    global image
    clear_canvas()
    image.draw(512, 382)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    pass


def pause():
    pass


def resume():
    pass






