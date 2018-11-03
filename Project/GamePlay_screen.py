import random
import json
import os
import sys

sys.path.insert(0,'C:\사용자\qaz04\Documents\GitHub\2DGP\1차 발표\Resource')
from pico2d import *

import game_framework
import game_world

from CharacterMeiMei import MeiMei
from Stage1screen import Stage1
from Stage2screen import Stage2
from Stage3screen import Stage3
from Stage4screen import Stage4
from Stage1_enemy_Cloud import Cloud
from Stage1_enemy_Chicken import Chicken
from Stage1_enemy_Sword import Sword


name = "GamePlay_screen"

CharacterMeiMei=None
Stage1_enemy_Cloud=None
Stage1_enemy_Chicken=None
Stage1_enemy_Sword=None
Stage1screen=None
Stage2screen=None
Stage3screen=None
Stage4screen=None
logo_time=0

def enter():
    global CharacterMeiMei,Stage1screen,Stage2screen,Stage3screen,Stage4screen,\
        Cloud,Chicken,Sword
    CharacterMeiMei = MeiMei()
    Stage1screen=Stage1()
    Stage2screen = Stage2()
    Stage3screen=Stage3()
    Stage4screen = Stage4()
    Stage1_enemy_Cloud = Cloud()
    Stage1_enemy_Chicken=Chicken()
    Stage1_enemy_Sword=Sword()

    game_world.add_object(Stage1screen, 0)
    game_world.add_object(CharacterMeiMei, 1)
    game_world.add_object(Stage1_enemy_Cloud, 2)
    game_world.add_object(Stage1_enemy_Chicken, 3)
    game_world.add_object(Stage1_enemy_Sword, 4)




def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            CharacterMeiMei.handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()


    update_canvas()






