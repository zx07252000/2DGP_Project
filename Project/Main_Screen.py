
from pico2d import *
import game_framework
import Character_select

name="Main_Screen"
image=None
new=None
option=None
option_L=None
Exit=None
Exit_L=None
change=4


def enter():
    global image,new,option,option_L,Exit,Exit_L

    image=load_image('Resource\\Main_Screen.png')
    new=load_image('Resource\\newgame.png')
    option=load_image('Resource\\option.png')
    option_L=load_image('Resource\\Option_L.png')
    Exit=load_image('Resource\\Exit.png')
    Exit_L = load_image('Resource\\Exit_L.png')

    pass

def exit():
    global image,new,option,option_L,Exit,Exit_L
    del(new)
    del(image)
    del(option)
    del(option_L)
    del(Exit)
    del (Exit_L)

    pass

def handle_events():
    global change
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN) and change>1:
                change=change-1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP) and change <5:
                change=change+1
            elif change==4and(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(Character_select)


    pass

def draw():

    clear_canvas()
    image.clip_draw(0, 0, 1020, 767, 512, 382)
    if(change==4):
        new.clip_draw(0, 30, 200, 45, 500, 400)
        option_L.clip_draw(0, 0, 150, 30, 510, 350)
        Exit_L.clip_draw(0, 0, 150, 40, 515, 280)
    if(change==3):
        new.clip_draw(0, 0, 200, 25, 500, 400)
        option.clip_draw(0, 0, 200, 30, 510, 350)
        Exit_L.clip_draw(0, 0, 150, 40, 515, 280)
    if (change == 2):
        new.clip_draw(0, 0, 200, 25, 500, 400)
        option_L.clip_draw(0, 0, 150, 30, 510, 350)
        Exit.clip_draw(0,0, 200, 50, 515, 280)
    elif(change<2or change>4):
        new.clip_draw(0, 0, 200, 25, 500, 400)
        option_L.clip_draw(0, 0, 150, 30, 510, 350)
        Exit_L.clip_draw(0, 0, 150, 40, 515, 280)


    update_canvas()
    pass

def update():
    pass


def pause():
    pass


def resume():
    pass

def Main_Screen_to_Character_Screen():
    global x,y
    events=get_events()
    pass


def Character_Screen_to_GamePlay_Screen():
    pass


def Main_Screen_to_Ranking():
    pass


def Main_Screen_to_Shop():
    pass


def Main_Screen_to_Exit():
    pass




