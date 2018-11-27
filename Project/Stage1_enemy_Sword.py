from pico2d import *
import game_framework
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

class Sword:
    image = None
    def __init__(self, i):
        self.x, self.y = 1000+200*i , random.randint(100,700)
        self.image = load_image('Resource_Monster\\Stage1_enemy_Sword.png')
        self.dir = 1
        self.velocity = random.randint(-10,-1)
        self.frame = 0
        self.timer = get_time()
        self.length=random.randint(-10,10)
        self.length_count=0




    def get_bb(self):
        return self.x - 10, self.y - 30, self.x + 10, self.y + 30

    def update(self):
        pass


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.frame = (self.frame + 1) % 4

        self.x = clamp(25, self.x, 5000 - 25)
        self.y=clamp(25,self.y,767-75)

        if self.x<50:
            self.x=1000
            self.y=random.randint(0,900)
        # 끝지점에 도달했을때 좌표 초기화

        self.x -= RUN_SPEED_PPS
        # 이동 값

        if self.timer%3>2:
            self.y -= self.length
        else:
            self.y += self.length
        # y축 랜덤 이동

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 40, 60, self.x, self.y)
        draw_rectangle(*self.get_bb())
        print (self.x)
        pass
