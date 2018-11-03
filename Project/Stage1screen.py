import random
import json
import os

from pico2d import *
from Stage2screen import Stage2

class Stage1:
    def __init__(self):
        self.image=load_image('Resource\\stage1.png')
        self.event_que = []

        self.x, self.y = 0, 382
        self.logo_time = 0
        self.dir = 1

        self.velocity = 0
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


        self.image.clip_draw(self.x, -200, 1040, 767,500,self.y)

        self.x+=10
        if (self.x == 1010):
            self.x = 0
        delay(0.1)



