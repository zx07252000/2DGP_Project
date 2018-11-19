from pico2d import *
import game_world
import random

class IdleState:

    @staticmethod
    def enter(Sword, event):
        Sword.velocity-=1
        Sword.x=1050
        Sword.y = random.randint(100,700)
        pass


    @staticmethod
    def exit(Sword, event):
        pass

    @staticmethod
    def do(Sword):
        Sword.frame = (Sword.frame + 1) % 4
        Sword.x = clamp(25, Sword.x, 1020 - 25)
        Sword.x += Sword.velocity
        pass



    @staticmethod
    def draw(Sword):
        if Sword.dir == 1:

            Sword.image.clip_draw(Sword.frame*50, 0, 40, 60, Sword.x, Sword.y)

        else:

            Sword.image.clip_draw(Sword.frame*50, 0, 40, 60, Sword.x, Sword.y)
            pass

class Sword:

    def __init__(self):
        self.x, self.y = 70 , 70
        self.image = load_image('Resource_Monster\\Stage1_enemy_Sword.png')
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
        return self.x - 20, self.y - 30, self.x + 20, self.y + 30

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
