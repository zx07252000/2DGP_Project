from pico2d import *
import game_world
import random

class IdleState:

    @staticmethod
    def enter(Fairy, event):

        Fairy.velocity-=1
        Fairy.x=1050
        Fairy.y =random.randint(100,700)

        pass


    @staticmethod
    def exit(Fairy, event):
        pass

    @staticmethod
    def do(Fairy):
        Fairy.frame = (Fairy.frame + 1) % 4
        Fairy.x = clamp(25, Fairy.x, 1020 - 25)
        Fairy.x+=Fairy.velocity

        pass



    @staticmethod
    def draw(Fairy):
        if Fairy.dir == 1:

            Fairy.image.clip_draw(Fairy.frame*50-2 , 50, 45, 40, Fairy.x, Fairy.y)

        else:

            Fairy.image.clip_draw(Fairy.frame*50-2, 50, 45, 40, Fairy.x, Fairy.y)
            pass


class RunState:

    @staticmethod
    def enter(Fairy, event):

        Fairy.dir = Fairy.velocity
        pass

    @staticmethod
    def exit(Fairy, event):

        pass

    @staticmethod
    def do(Fairy):
        Fairy.frame = (Fairy.frame + 1) % 4
        Fairy.timer -= 1
        Fairy.x +=Fairy.velocity
        Fairy.y += Fairy.length
        Fairy.x = clamp(25, Fairy.x, 1020 - 25)
        Fairy.y = clamp(25, Fairy.y, 767 - 25)
        pass

    @staticmethod
    def draw(Fairy):
        if Fairy.velocity == 1:

            Fairy.image.clip_draw(Fairy.frame*100, 0, 60, 60, Fairy.x, Fairy.y)

        else:

            Fairy.image.clip_draw(Fairy.frame*100, 0, 60, 60, Fairy.x, Fairy.y)
            pass



class Fairy:

    def __init__(self):
        self.x, self.y = 70 , 70
        self.image = load_image('Resource_Monster\\Stage1_enemy_Fairy.png')
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