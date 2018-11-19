from pico2d import *
import game_world
import random

class IdleState:

    @staticmethod
    def enter(Cloud, event):

        Cloud.velocity-=1
        Cloud.x=1050
        Cloud.y =random.randint(100,700)

        pass


    @staticmethod
    def exit(Cloud, event):
        pass

    @staticmethod
    def do(Cloud):
        Cloud.frame = (Cloud.frame + 1) % 5
        Cloud.x = clamp(25, Cloud.x, 1020 - 25)
        Cloud.x+=Cloud.velocity

        pass



    @staticmethod
    def draw(Cloud):
        if Cloud.dir == 1:

            Cloud.image.clip_draw(Cloud.frame*47, 50, 50, 40, Cloud.x, Cloud.y)

        else:

            Cloud.image.clip_draw(Cloud.frame*47, 50, 50, 40, Cloud.x, Cloud.y)
            pass

class Cloud:

    def __init__(self):
        self.x, self.y = 70 , 70
        self.image = load_image('Resource_Monster\\Stage1_enemy_Cloud.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.length=0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        # fill here
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state.enter(self, event)
        pass
    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        pass
