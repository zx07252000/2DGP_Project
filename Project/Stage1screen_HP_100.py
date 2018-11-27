import random
import json
import os

from pico2d import *
from GamePlay_screen import *

from Stage2screen import Stage2
from Character_State import State


class Stage1_HP_100:
    def __init__(self):
        self.image=load_image('Resource_Stage\\stage1.png')
        self.image2 = load_image('Resource_Screen\\Character_State_100.png')


        self.event_que = []
        self.x, self.y = 0, 382
        self.x2,self.y2=350, 750
        self.change=0
        self.dir = 1
        self.velocity = 0
        self.bgm = load_wav('Resource_Bgm\\Stage1_Bgm.wav')
        self.bgm.set_volume(64)
        self.bgm.play()

    def enter_IDLE(self):
        self.timer = 1000
        self.frame = 0

    def exit_IDLE(self):
        pass

    def update(self):
        pass
    def do_IDLE(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
    def draw(self):

        if (self.x == 1000):
            self.change = 1
        if (self.x == 0):
            self.change = 0
        self.image.clip_draw(self.x, -200, 1040, 767,500,self.y)


        self.image2.clip_draw(0, 0, 700, 50, self.x2, self.y2)


        if (self.change==0 and self.x  < 1000):
            self.x+=2
        if (self.change==1):
            self.x -= 2
        delay(0.1)



