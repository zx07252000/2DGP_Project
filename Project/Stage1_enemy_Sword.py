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


class RunState:

    @staticmethod
    def enter(Sword, event):

        Sword.dir = Sword.velocity
        pass

    @staticmethod
    def exit(Sword, event):

        pass

    @staticmethod
    def do(Sword):
        Sword.frame = (Sword.frame + 1) % 8
        Sword.timer -= 1
        Sword.x +=Sword.velocity
        Sword.y += Sword.length
        Sword.x = clamp(25, Sword.x, 1020 - 25)
        Sword.y = clamp(25, Sword.y, 767 - 25)
        pass

    @staticmethod
    def draw(Sword):
        if Sword.velocity == 1:

            Sword.image.clip_draw(260, 0, 60, 60, Sword.x, Sword.y)

        else:

            Sword.image.clip_draw(260, 0, 60, 60, Sword.x, Sword.y)
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