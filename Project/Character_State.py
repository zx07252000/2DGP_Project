import random
import json
import os

from pico2d import *

class State:
    def __init__(self):
        self.image=load_image('Resource_Screen\\Character_State_100.png')
        self.event_que = []
        self.x, self.y = 350, 750
        self.change=0
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

        self.image.clip_draw(0,0 , 700, 50,self.x,self.y)

        delay(0.1)



