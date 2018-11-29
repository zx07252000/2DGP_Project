
import json
import os

from pico2d import *
import GamePlay_screen

from Stage2screen import Stage2
from Character_State import State


class Stage1_HP_30:
    def __init__(self):
        self.image = load_image('Resource_Stage\\stage1.png')
        self.image2 = load_image('Resource_Screen\\Character_State_30.png')
        self.score_image = load_image('Resource_Screen\\Record_Time.png')
        self.font = load_font('Resource_Temporary\\ENCR10B.TTF', 64)

        self.score_image.x = 700
        self.event_que = []
        self.x, self.y = 0, 382
        self.x2, self.y2 = 250, 750
        self.change = 0
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

        self.image2.clip_draw(0, 0, 500, 50, self.x2, self.y2)
        self.score_image.clip_draw(0, 0, 200, 50, self.score_image.x, self.y2 - 10)
        self.font.draw(self.score_image.x + 100, self.y2 - 10, '%d' % GamePlay_screen.score, (255, 255, 255))

        if (self.change==0 and self.x  < 1000):
            self.x+=2
        if (self.change==1):
            self.x -= 2
        delay(0.1)



