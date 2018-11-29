
from pico2d import *
import game_framework
import Character_select

name="Main_Screen"
image=None
New_icon=None
Choose_option=None
Not_Choose_option=None
Choose_Exit=None
Not_Choose_Exit=None
Select_Menu=4
Select_New=4
Select_Option=3
Select_Exit=2

def enter():
    global image,New_icon,Choose_option,Not_Choose_option,Choose_Exit,Not_Choose_Exit,bgm,Menu_bgm

    image=load_image('Resource_Screen\\Main_Screen.png')
    New_icon=load_image('Resource_Screen\\newgame.png')
    Choose_option=load_image('Resource_Screen\\option.png')
    Not_Choose_option=load_image('Resource_Screen\\Option_L.png')
    Choose_Exit=load_image('Resource_Screen\\Exit.png')
    Not_Choose_Exit = load_image('Resource_Screen\\Exit_L.png')

    bgm = load_wav('Resource_Bgm\\Main_Theme.wav')
    bgm.set_volume(128)
    bgm.play()

    Menu_bgm=load_music('Resource_Bgm\\Menu_Bgm.wav')
    Menu_bgm.set_volume(32)
    Menu_bgm.play()
    pass

def exit():
    global image,New_icon,Choose_option,Not_Choose_option,Choose_Exit,Not_Choose_Exit
    del(New_icon)
    del(image)
    del(Choose_option)
    del(Not_Choose_option)
    del(Choose_Exit)
    del (Not_Choose_Exit)

    pass

def handle_events():
    global change,Select_Menu,Select_New,Select_Option,Select_Exit
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN) and Select_Menu>1:
                Select_Menu=Select_Menu-1
                Menu_bgm.play()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP) and Select_Menu <5:
                Select_Menu=Select_Menu+1
                Menu_bgm.play()
            elif Select_Menu==Select_New and(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Menu_bgm.__del__()
                game_framework.change_state(Character_select)



    pass

def draw():

    clear_canvas()
    image.clip_draw(0, 0, 1020, 767, 512, 382)
    if(Select_Menu==Select_New):
        New_icon.clip_draw(0, 30, 200, 45, 500, 400)
        Not_Choose_option.clip_draw(0, 0, 150, 30, 510, 350)
        Not_Choose_Exit.clip_draw(0, 0, 150, 40, 515, 280)
    if(Select_Menu==Select_Option):
        New_icon.clip_draw(0, 0, 200, 25, 500, 400)
        Choose_option.clip_draw(0, 0, 200, 30, 510, 350)
        Not_Choose_Exit.clip_draw(0, 0, 150, 40, 515, 280)
    if (Select_Menu == Select_Exit):
        New_icon.clip_draw(0, 0, 200, 25, 500, 400)
        Not_Choose_option.clip_draw(0, 0, 150, 30, 510, 350)
        Choose_Exit.clip_draw(0,0, 200, 50, 515, 280)
    elif(Select_Menu<Select_Exit or Select_Menu>Select_New):
        New_icon.clip_draw(0, 0, 200, 25, 500, 400)
        Not_Choose_option.clip_draw(0, 0, 150, 30, 510, 350)
        Not_Choose_Exit.clip_draw(0, 0, 150, 40, 515, 280)


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






