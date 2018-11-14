from pico2d import *
import game_world
import random

class IdleState:

    @staticmethod
    def enter(Wheel, event):

        Wheel.velocity-=1
        Wheel.x=1050
        Wheel.y =random.randint(100,700)

        pass


    @staticmethod
    def exit(Wheel, event):
        pass

    @staticmethod
    def do(Wheel):
        Wheel.frame = (Wheel.frame + 1) % 4
        Wheel.x = clamp(25, Wheel.x, 1020 - 25)
        Wheel.x+=Wheel.velocity

        pass



    @staticmethod
    def draw(Wheel):
        if Wheel.dir == 1:

            Wheel.image.clip_draw(Wheel.frame*50-2 , 50, 45, 40, Wheel.x, Wheel.y)

        else:

            Wheel.image.clip_draw(Wheel.frame*50-2, 50, 45, 40, Wheel.x, Wheel.y)
            pass


class RunState:

    @staticmethod
    def enter(Wheel, event):

        Wheel.dir = Wheel.velocity
        pass

    @staticmethod
    def exit(Wheel, event):

        pass

    @staticmethod
    def do(Wheel):
        Wheel.frame = (Wheel.frame + 1) % 4
        Wheel.timer -= 1
        Wheel.x +=Wheel.velocity
        Wheel.y += Wheel.length
        Wheel.x = clamp(25, Wheel.x, 1020 - 25)
        Wheel.y = clamp(25, Wheel.y, 767 - 25)
        pass

    @staticmethod
    def draw(Wheel):
        if Wheel.velocity == 1:

            Wheel.image.clip_draw(Wheel.frame*100, 0, 60, 60, Wheel.x, Wheel.y)

        else:

            Wheel.image.clip_draw(Wheel.frame*100, 0, 60, 60, Wheel.x, Wheel.y)
            pass



class Wheel:

    def __init__(self):
        self.x, self.y = 70 , 70
        self.image = load_image('Resource_Monster\\Stage1_enemy_Wheel.png')
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