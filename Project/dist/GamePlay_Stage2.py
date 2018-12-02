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
from Stage2screen_HP_100 import Stage2_HP_100
from Stage2screen_HP_70 import Stage2_HP_70
from Stage2screen_HP_30 import Stage2_HP_30

from ball import Ball
from Boss_ball import Boss2_Ball

from Stage2_enemy_Lamp import Lamp
from Stage2_enemy_mask import Mask


from Stage2_boss import Boss2



name = "GamePlay_Stage2"

CharacterMeiMei=None
Stage2_enemys_Lamp=[]
Stage2_enemys_mask=[]

Boss_ball=[]

Stage2_boss=None
score=0

Ball=None


Stage1_Clear_Score=0
Game_Over_State=0
eraser=0
Boss_Hp=50


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global CharacterMeiMei,Stage2screen_HP_100,Stage2screen_HP_70,Stage2screen_HP_30,\
        Stage2_enemys_Lamp,Stage2_enemys_mask,Character_State,Stage2_boss,Boss_ball

    CharacterMeiMei = MeiMei()
    Stage2screen_HP_100=Stage2_HP_100()
    Stage2screen_HP_70=Stage2_HP_70()
    Stage2screen_HP_30=Stage2_HP_30()

    Stage2_boss = Boss2()


    Stage2_enemys_Lamp = [Lamp(i) for i in range(10)]
    game_world.add_objects(Stage2_enemys_Lamp, 1)

    Stage2_enemys_mask = [Mask(i) for i in range(10)]
    game_world.add_objects(Stage2_enemys_mask,1)


    Boss_ball=[Boss2_Ball(i) for i in range(20)]

    game_world.add_object(Stage2screen_HP_100, 0)

    game_world.add_object(CharacterMeiMei, 1)


def exit():
    game_world.clear()

def pause():
    pass

def get_CharacterMeiMei():
    return CharacterMeiMei

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
    global Stage1_Clear_Score,eraser,Game_Over_State,Boss_Hp,score

    for game_object in game_world.all_objects():
        game_object.update()

    remove_enemys = []
    remove_ball = []

    for enemys in Stage2_enemys_Lamp:
        for ball in ball_list:
            if collide(enemys, ball):
                remove_enemys.append(enemys)
                remove_ball.append(ball)

    for enemys in remove_enemys:
        while True:
            try:
                Stage2_enemys_Lamp.remove(enemys)
                game_world.remove_object(enemys)
                Stage1_Clear_Score += 1
                score = score + 100
            except:
                break

    for ball in remove_ball:
        while True:
            try:
                ball_list.remove(ball)
                game_world.remove_object(ball)
            except:
                break

    for enemys in Stage2_enemys_mask:
        for ball in ball_list:
            if collide(enemys, ball):
                remove_enemys.append(enemys)
                remove_ball.append(ball)
                

    for enemys in remove_enemys:
        while True:
            try:
                Stage2_enemys_mask.remove(enemys)
                game_world.remove_object(enemys)
                Stage1_Clear_Score += 1
                score = score + 100
            except:
                break
    for ball in remove_ball:
        while True:
            try:
                ball_list.remove(ball)
                game_world.remove_object(ball)
            except:
                break




    if Stage1_Clear_Score==10:
        game_world.add_object(Stage2_boss, 1)
        game_world.add_objects(Boss_ball, 1)
        Stage1_Clear_Score=Stage1_Clear_Score+1

    if Stage1_Clear_Score > 10:
        for ball in ball_list:
            if collide(ball,Stage2_boss):
                game_world.remove_object(ball)
                ball_list.remove(ball)
                Boss_Hp -= 1


    if Boss_Hp==0:
        game_world.remove_object(Stage2_boss)
        Stage2screen_HP_100.bgm.__del__()
        Stage2screen_HP_70.bgm.__del__()
        Stage2screen_HP_30.bgm.__del__()

        game_framework.change_state(Stage_Clear)


    for enemys in Stage2_enemys_mask:
        if collide(enemys, CharacterMeiMei):
            Stage2_enemys_mask.remove(enemys)
            game_world.remove_object(enemys)
            Game_Over_State=Game_Over_State+1

    for enemys in Stage2_enemys_Lamp:
        if collide(enemys, CharacterMeiMei):
            Stage2_enemys_Lamp.remove(enemys)
            game_world.remove_object(enemys)
            Game_Over_State=Game_Over_State+1


    if Game_Over_State == 1:
        game_world.remove_object(Stage2screen_HP_100)
        game_world.add_object(Stage2screen_HP_70,0)
        Game_Over_State=Game_Over_State+1

    if Game_Over_State == 3:
        game_world.remove_object(Stage2screen_HP_70)
        game_world.add_object(Stage2screen_HP_30,0)
        Game_Over_State=Game_Over_State+1

    if Game_Over_State==5:

        Stage2screen_HP_100.bgm.__del__()
        Stage2screen_HP_70.bgm.__del__()
        Stage2screen_HP_30.bgm.__del__()
        game_framework.change_state(Game_Over)

    for enemys in Stage2_enemys_Lamp:
        if Stage1_Clear_Score==10:
            game_world.remove_object(enemys)

    for enemys in Stage2_enemys_mask:
        if Stage1_Clear_Score == 10:
            game_world.remove_object(enemys)




    for Boss_Attack in Boss_ball:
        if collide(Boss_Attack, CharacterMeiMei):

            Game_Over_State = Game_Over_State + 1



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()



    update_canvas()






