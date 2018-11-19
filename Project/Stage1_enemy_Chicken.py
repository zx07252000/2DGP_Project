from pico2d import *
import game_world
import random

class IdleState:

    @staticmethod
    def enter(Chicken, event):

        Chicken.velocity-=1
        Chicken.x=1050
        Chicken.y =random.randint(100,700)
        pass


    @staticmethod
    def exit(Chicken, event):
        pass

    @staticmethod
    def do(Chicken):
        Chicken.frame = (Chicken.frame + 1) % 4
        Chicken.x = clamp(25, Chicken.x, 1020 - 25)
        Chicken.x+=Chicken.velocity
        pass



    @staticmethod
    def draw(Chicken):
        if Chicken.dir == 1:
            Chicken.image.clip_draw(Chicken.frame*50-2 , 50, 45, 40, Chicken.x, Chicken.y)

        else:
            Chicken.image.clip_draw(Chicken.frame*50-2, 50, 45, 40, Chicken.x, Chicken.y)
            pass



class Chicken:

    def __init__(self):
        self.x, self.y = 70 , 70
        self.image = load_image('Resource_Monster\\Stage1_enemy_Chicken.png')
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

