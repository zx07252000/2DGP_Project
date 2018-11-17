import random
import json
import os
import math


from pico2d import *

import game_framework
import game_world

from CharacterMeiMei import MeiMei
from Stage1screen import Stage1
from Stage2screen import Stage2
from Stage3screen import Stage3
from Stage4screen import Stage4
from ball import Ball
from Stage1_enemy_Cloud import Cloud
from Stage1_enemy_Chicken import Chicken
from Stage1_enemy_Sword import Sword



name = "GamePlay_screen"

CharacterMeiMei=None
Stage1_enemy_Cloud=[]
Stage1_enemy_Chicken=[]
Stage1_enemy_Sword=[]
Stage1screen=None
Stage2screen=None
Stage3screen=None
Stage4screen=None
balls = []


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global CharacterMeiMei,Stage1screen,Stage2screen,Stage3screen,Stage4screen

    CharacterMeiMei = MeiMei()
    Stage1screen=Stage1()
    Stage2screen = Stage2()
    Stage3screen=Stage3()
    Stage4screen = Stage4()
    global balls
    game_world.add_objects(balls, 1)

    global Stage1_enemy_Cloud
    Stage1_enemy_Cloud=Cloud()
    game_world.add_object(Stage1_enemy_Cloud, 1)

    Stage1_enemy_Chicken=Chicken()
    Stage1_enemy_Sword=Sword()


    game_world.add_object(Stage1screen, 0)
    game_world.add_object(CharacterMeiMei, 1)

    game_world.add_object(Stage1_enemy_Chicken, 1)
    game_world.add_object(Stage1_enemy_Sword, 1)




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
    for ball in balls:
        if collide(Stage1_enemy_Cloud, ball):
            ball.stop()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






