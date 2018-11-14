from pico2d import *
import game_world
import random

class IdleState:

    @staticmethod
    def enter(Mask, event):

        Mask.velocity-=1
        Mask.x=1050
        Mask.y =random.randint(100,700)

        pass


    @staticmethod
    def exit(Mask, event):
        pass

    @staticmethod
    def do(Mask):
        Mask.frame = (Mask.frame + 1) % 4
        Mask.x = clamp(25, Mask.x, 1020 - 25)
        Mask.x+=Mask.velocity

        pass



    @staticmethod
    def draw(Mask):
        if Mask.dir == 1:

            Mask.image.clip_draw(Mask.frame*50-2 , 50, 45, 40, Mask.x, Mask.y)

        else:

            Mask.image.clip_draw(Mask.frame*50-2, 50, 45, 40, Mask.x, Mask.y)
            pass


class RunState:

    @staticmethod
    def enter(Mask, event):

        Mask.dir = Mask.velocity
        pass

    @staticmethod
    def exit(Mask, event):

        pass

    @staticmethod
    def do(Mask):
        Mask.frame = (Mask.frame + 1) % 4
        Mask.timer -= 1
        Mask.x +=Mask.velocity
        Mask.y += Mask.length
        Mask.x = clamp(25, Mask.x, 1020 - 25)
        Mask.y = clamp(25, Mask.y, 767 - 25)
        pass

    @staticmethod
    def draw(Mask):
        if Mask.velocity == 1:

            Mask.image.clip_draw(Mask.frame*100, 0, 60, 60, Mask.x, Mask.y)

        else:

            Mask.image.clip_draw(Mask.frame*100, 0, 60, 60, Mask.x, Mask.y)
            pass



class Mask:

    def __init__(self):
        self.x, self.y = 70 , 70
        self.image = load_image('Resource_Monster\\Stage1_enemy_Mask.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.length=0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass
    def draw(self):
        self.cur_state.draw(self)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass