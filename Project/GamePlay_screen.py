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
from Stage1screen_HP_100 import Stage1_HP_100
from Stage1screen_HP_70 import Stage1_HP_70
from Stage1screen_HP_30 import Stage1_HP_30

from ball import Ball
from Boss_ball import Boss_Ball

from Stage2screen import Stage2
from Stage3screen import Stage3
from Stage4screen import Stage4

from Stage1_enemy_Cloud import Cloud
from Stage1_enemy_Chicken import Chicken
from Stage1_enemy_Sword import Sword

from Stage1_boss import Boss1



name = "GamePlay_screen"

CharacterMeiMei=None
Stage1_enemy_Cloud=[]
Stage1_enemy_Chicken=[]
Stage1_enemy_Sword=[]
Boss_ball=[]

Stage1_boss=None

Ball=None


Stage1_Clear_Score=0
Game_Over_State=0
eraser=0
Boss_Hp=50

Stage1screen=None
Stage2screen=None
Stage3screen=None
Stage4screen=None



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global CharacterMeiMei,Stage1screen_HP_100,Stage1screen_HP_70,Stage1screen_HP_30,Stage2screen,Stage3screen,Stage4screen,\
        Stage1_enemy_Cloud,Stage1_enemy_Chicken,Stage1_enemy_Sword,Character_State,Ball,Stage1_boss,Boss_ball

    CharacterMeiMei = MeiMei()
    Stage1screen_HP_100=Stage1_HP_100()
    Stage1screen_HP_70=Stage1_HP_70()
    Stage1screen_HP_30=Stage1_HP_30()

    Ball=ball_list


    Stage1_boss=Boss1()

    Stage2screen = Stage2()
    Stage3screen=Stage3()
    Stage4screen = Stage4()

    Stage1_enemy_Chicken = [Chicken(i) for i in range(10)]
    game_world.add_objects(Stage1_enemy_Chicken, 1)

    Stage1_enemy_Sword = [Sword(i) for i in range(10)]
    game_world.add_objects(Stage1_enemy_Sword, 1)

    Stage1_enemy_Cloud=[Cloud(i) for i in range(10)]
    game_world.add_objects( Stage1_enemy_Cloud, 1)

    Boss_ball=[Boss_Ball(i) for i in range(10)]
    game_world.add_objects(Boss_ball, 1)

    game_world.add_object(Stage1screen_HP_100, 0)

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
    global Stage1_Clear_Score,eraser,Game_Over_State,Boss_Hp

    for game_object in game_world.all_objects():
        game_object.update()

    for enemy in Stage1_enemy_Chicken:
        for ball in ball_list:
            if collide(enemy,ball):
                Stage1_enemy_Chicken.remove(enemy)
                ball_list.remove(ball)
                game_world.remove_object(enemy)
                game_world.remove_object(ball)
                Stage1_Clear_Score += 1
    for enemy in Stage1_enemy_Cloud:
        for ball in ball_list:
            if collide(enemy, ball):
                Stage1_enemy_Cloud.remove(enemy)
                ball_list.remove(ball)
                game_world.remove_object(enemy)
                game_world.remove_object(ball)
                Stage1_Clear_Score += 1

    for enemy in Stage1_enemy_Sword:
        for ball in ball_list:
            if collide(enemy, ball):
                Stage1_enemy_Sword.remove(enemy)
                ball_list.remove(ball)
                game_world.remove_object(enemy)
                game_world.remove_object(ball)
                Stage1_Clear_Score+=1


        for ball in ball_list:
            if collide(Stage1_boss, ball):
                game_world.remove_object(ball)
                ball_list.remove(ball)
                Boss_Hp -= 1
            if Boss_Hp==0:
                Stage1_boss.remove(Stage1_boss)
                game_world.remove_object(Stage1_boss)
                game_framework.change_state(Stage_Clear)

    for Boss_Attack in Boss_ball:
        if collide(Boss_Attack, CharacterMeiMei):
            Boss_ball.remove(Boss_Attack)
            game_world.remove_object(Boss_Attack)
            Game_Over_State = Game_Over_State + 1



    for enemy in Stage1_enemy_Cloud:
        if collide(enemy, CharacterMeiMei):
            Stage1_enemy_Cloud.remove(enemy)
            game_world.remove_object(enemy)
            Game_Over_State=Game_Over_State+1


    for enemy in Stage1_enemy_Sword:
        if collide(enemy, CharacterMeiMei):
            Stage1_enemy_Sword.remove(enemy)
            game_world.remove_object(enemy)
            Game_Over_State=Game_Over_State+1

    for enemy in Stage1_enemy_Chicken:
        if collide(enemy, CharacterMeiMei):
            Stage1_enemy_Chicken.remove(enemy)
            game_world.remove_object(enemy)
            Game_Over_State=Game_Over_State+1


    if Game_Over_State == 1:
        game_world.remove_object(Stage1screen_HP_100)
        game_world.add_object(Stage1screen_HP_70,0)
        Game_Over_State=Game_Over_State+1

    if Game_Over_State == 3:
        game_world.remove_object(Stage1screen_HP_70)
        game_world.add_object(Stage1screen_HP_30,0)
        Game_Over_State=Game_Over_State+1

    if Game_Over_State==5:
        game_framework.change_state(Game_Over)

    for enemy in Stage1_enemy_Sword:
        if Stage1_Clear_Score==29:
            game_world.remove_object(enemy)

    for enemy in Stage1_enemy_Cloud:
        if Stage1_Clear_Score == 29:
            game_world.remove_object(enemy)

    for enemy in Stage1_enemy_Chicken:
        if Stage1_Clear_Score == 29:
            game_world.remove_object(enemy)

    if Stage1_Clear_Score==0:
        game_world.add_object(Stage1_boss, 1)
        Stage1_Clear_Score=Stage1_Clear_Score+1






def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()






