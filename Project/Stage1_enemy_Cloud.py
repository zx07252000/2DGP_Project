from pico2d import *
import game_framework
import game_world
import random

class Cloud:
    PIXEL_PER_METER = (10.0 / 2.0)

    RUN_SPEED_KMPH = 20.0

    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)

    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)

    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5

    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

    FRAMES_PER_ACTION = 8

    def __init__(self, i):
        self.x, self.y = 100+70*i , random.randint(100,700)
        self.image = load_image('Resource_Monster\\Stage1_enemy_Cloud.png')
        self.dir = 1
        self.velocity = -10
        self.frame = 0
        self.timer = 0
        self.length=0



    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def update(self):
        pass

    def do(Cloud):
        Cloud.frame = (Cloud.frame + 1) % 5

        Cloud.x = clamp(25, Cloud.x, 2000)

        Cloud.x += Cloud.velocity

        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.frame = (self.frame + 1) % 5

        self.x = clamp(25, self.x, 1020 - 25)

        self.x += self.velocity

        pass

    def draw(self):
        self.image.clip_draw(self.frame * 47, 50, 50, 40, self.x, self.y)
        pass
