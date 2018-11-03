import random
import json
import os

from pico2d import *

import game_framework


from CharacterWukung import Wukung
from Stage1screen import Stage1
from Stage2screen import Stage2
from Stage3screen import Stage3
from Stage4screen import Stage4

name = "GamePlay_screen"

CharacterWukung=None

Stage1screen=None
Stage2screen=None
Stage3screen=None
Stage4screen=None
logo_time=0

def enter():
    global CharacterWukung,Stage1screen,Stage2screen,Stage3screen,Stage4screen
    CharacterWukung = Wukung()
    Stage1screen=Stage1()
    Stage2screen = Stage2()
    Stage3screen=Stage3()
    Stage4screen = Stage4()


def exit():
    global CharacterWukung,Stage1screen,Stage2screen,Stage3screen,Stage4screen
    del CharacterWukung
    del Stage1screen
    del Stage2screen
    del Stage3screen
    del Stage4screen

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
            CharacterWukung.handle_event(event)

def update():

    CharacterWukung.update()

def draw():
    clear_canvas()
    Stage1screen.draw()
    global logo_time

    if (logo_time > 1.0):
        Stage2screen.draw()
    if(logo_time>2.0):
        Stage3screen.draw()
    if (logo_time > 3.0):
        Stage4screen.draw()
    delay(0.01)
    logo_time += 0.01
    CharacterWukung.draw()
    update_canvas()






