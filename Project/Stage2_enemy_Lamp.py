from pico2d import *
import game_world
import random

class IdleState:

    @staticmethod
    def enter(Lamp, event):

        Lamp.velocity-=1
        Lamp.x=1050
        Lamp.y =random.randint(100,700)

        pass


    @staticmethod
    def exit(Lamp, event):
        pass

    @staticmethod
    def do(Lamp):
        Lamp.frame = (Lamp.frame + 1) % 4
        Lamp.x = clamp(25, Lamp.x, 1020 - 25)
        Lamp.x+=Lamp.velocity

        pass



    @staticmethod
    def draw(Lamp):
        if Lamp.dir == 1:

            Lamp.image.clip_draw(Lamp.frame*50-2 , 50, 45, 40, Lamp.x, Lamp.y)

        else:

            Lamp.image.clip_draw(Lamp.frame*50-2, 50, 45, 40, Lamp.x, Lamp.y)
            pass


class RunState:

    @staticmethod
    def enter(Lamp, event):

        Lamp.dir = Lamp.velocity
        pass

    @staticmethod
    def exit(Lamp, event):

        pass

    @staticmethod
    def do(Lamp):
        Lamp.frame = (Lamp.frame + 1) % 4
        Lamp.timer -= 1
        Lamp.x +=Lamp.velocity
        Lamp.y += Lamp.length
        Lamp.x = clamp(25, Lamp.x, 1020 - 25)
        Lamp.y = clamp(25, Lamp.y, 767 - 25)
        pass

    @staticmethod
    def draw(Lamp):
        if Lamp.velocity == 1:

            Lamp.image.clip_draw(Lamp.frame*100, 0, 60, 60, Lamp.x, Lamp.y)

        else:

            Lamp.image.clip_draw(Lamp.frame*100, 0, 60, 60, Lamp.x, Lamp.y)
            pass



class Lamp:

    def __init__(self):
        self.x, self.y = 70 , 70
        self.image = load_image('Resource_Monster\\Stage2_enemy_Lamp.png')
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