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

FRAMES_PER_ACTION = 4

class Cloud:

    image=None
    def __init__(self, i):
        self.image = load_image('Resource_Monster\\Stage1_enemy_Cloud.png')
        self.x, self.y = 1000 + 200 * i, random.randint(100, 700)
        self.dir = 1
        self.velocity = random.randint(-10,-1)
        self.frame = 0
        self.timer = get_time()
        self.length=random.randint(10,20)
        self.length_count=0
        self.y_change = 0



    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def update(self):
        pass



    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.frame = (self.frame + 1) % 5

        self.x = clamp(25, self.x, 5000 - 25)
        self.y=clamp(25,self.y,767-75)

        if self.x<50:
            self.x=1000
            self.y=random.randint(0,900)
        # 끝지점에 도달했을때 좌표 초기화

        self.x -= RUN_SPEED_PPS
        # 이동 값

        if self.y_change==0:
            self.y -= self.length
        if self.y_change == 1:
            self.y += self.length

        if self.y > 767 - 70:
            self.y_change = 0
        if self.y < 30:
            self.y_change = 1
        # y축 랜덤 이동
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 47, 50, 50, 40, self.x, self.y)


        pass
