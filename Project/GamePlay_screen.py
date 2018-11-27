import random
import json
import os
import math


from pico2d import *

import game_framework
import game_world
import Stage_Clear
import Game_Over

from CharacterMeiMei import *
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
ball=None

Stage1_Clear_Score=0
eraser=0

Stage1screen=None
Stage2screen=None
Stage3screen=None
Stage4screen=None



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
    global CharacterMeiMei,Stage1screen,Stage2screen,Stage3screen,Stage4screen,\
        Stage1_enemy_Cloud,Stage1_enemy_Chicken,Stage1_enemy_Sword,ball

    CharacterMeiMei = MeiMei()
    Stage1screen=Stage1()
    Stage2screen = Stage2()
    Stage3screen=Stage3()
    Stage4screen = Stage4()

    Stage1_enemy_Chicken = [Chicken(i) for i in range(10)]
    game_world.add_objects(Stage1_enemy_Chicken, 1)

    Stage1_enemy_Sword = [Sword(i) for i in range(10)]
    game_world.add_objects(Stage1_enemy_Sword, 1)

    Stage1_enemy_Cloud=[Cloud(i) for i in range(10)]
    game_world.add_objects( Stage1_enemy_Cloud, 1)

    game_world.add_object(Stage1screen, 0)
    game_world.add_object(CharacterMeiMei, 1)

    if Stage1_Clear_Score == 2:
        game_world.add_object(Stage2screen, 0)

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
    global Stage1_Clear_Score,eraser

    for game_object in game_world.all_objects():
        game_object.update()
    for enemy in Stage1_enemy_Chicken:
        for ball in ball_list:
            if collide(enemy,ball):
                Stage1_enemy_Chicken.remove(enemy)
                ball_list.remove(ball)
                game_world.remove_object(enemy)
                game_world.remove_object(ball)
                Stage1_Clear_Score = Stage1_Clear_Score + 1

    for enemy in Stage1_enemy_Cloud  :
            if collide(enemy, CharacterMeiMei):
                Stage1_enemy_Cloud.remove(enemy)
                game_world.remove_object(enemy)
                game_framework.change_state(Game_Over)

    for enemy in Stage1_enemy_Sword :
            if collide(enemy, CharacterMeiMei):
                Stage1_enemy_Sword.remove(enemy)
                game_world.remove_object(enemy)
                game_framework.change_state(Game_Over)

    for enemy in Stage1_enemy_Chicken :
            if collide(enemy, CharacterMeiMei):
                Stage1_enemy_Chicken.remove(enemy)
                game_world.remove_object(enemy)
                game_framework.change_state(Game_Over)

    for enemy in Stage1_enemy_Cloud:
        for ball in ball_list:
            if collide(enemy, ball):
                Stage1_enemy_Cloud. remove(enemy)
                ball_list.remove(ball)
                game_world.remove_object(enemy)
                game_world.remove_object(ball)
                Stage1_Clear_Score=Stage1_Clear_Score+1

    for enemy in Stage1_enemy_Sword:
        for ball in ball_list:
            if collide(enemy, ball):
                Stage1_enemy_Sword.remove(enemy)
                ball_list.remove(ball)
                game_world.remove_object(enemy)
                game_world.remove_object(ball)
                Stage1_Clear_Score = Stage1_Clear_Score + 1

    for enemy in Stage1_enemy_Sword:
        if Stage1_Clear_Score==20:
            game_world.remove_object(enemy)

    for enemy in Stage1_enemy_Cloud:
        if Stage1_Clear_Score == 20:
            game_world.remove_object(enemy)

    for enemy in Stage1_enemy_Chicken:
        if Stage1_Clear_Score == 20:
            game_world.remove_object(enemy)
            eraser=1

    if eraser==1:
        game_framework.change_state(Stage_Clear)





def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






