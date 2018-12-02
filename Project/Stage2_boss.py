from pico2d import *
import game_framework
from Boss_ball import Boss_Ball
import game_world
import random


PIXEL_PER_METER = (5.0 / 2.0)

RUN_SPEED_KMPH = 20.0

RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)

RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)

RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5

ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

FRAMES_PER_ACTION = 8

Boss_ball_list=[]

class Boss2:
    image = None

    def __init__(self):
        self.x, self.y = 900 , 500
        self.image = load_image('Resource_Monster\\Stage2_boss.png')
        self.dir = 1
        self.velocity = random.randint(-10,-1)
        self.frame = 0
        self.y_change=0
        self.timer = get_time()
        self.length=20
        self.length_count=0



    def get_bb(self):

        return self.x - 100, self.y - 100, self.x + 100, self.y + 100


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):

        self.frame = (self.frame + 1) % 4

        self.x = clamp(25, self.x, 5000 - 25)
        self.y=clamp(75,self.y,767-50)

        if self.x<50:
            self.x=1000
            self.y=random.randint(0,900)
        # 끝지점에 도달했을때 좌표 초기화


        if self.y_change==0:
            self.y -= self.length
        if self.y<76:
            self.y_change=1
        if self.y>767-51:
            self.y_change=0

        if self.y_change==1:
            self.y += self.length
            # y축 랜덤 이동

    def draw(self):
        self.image.clip_draw( self.frame * 240 , 780, 195, 170,  self.x,  self.y)
        draw_rectangle(*self.get_bb())

        pass
