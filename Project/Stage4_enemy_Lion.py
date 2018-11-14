from pico2d import *
import game_world
import random

class IdleState:

    @staticmethod
    def enter(Lion, event):

        Lion.velocity-=1
        Lion.x=1050
        Lion.y =random.randint(100,700)

        pass


    @staticmethod
    def exit(Lion, event):
        pass

    @staticmethod
    def do(Lion):
        Lion.frame = (Lion.frame + 1) % 4
        Lion.x = clamp(25, Lion.x, 1020 - 25)
        Lion.x+=Lion.velocity

        pass



    @staticmethod
    def draw(Lion):
        if Lion.dir == 1:

            Lion.image.clip_draw(Lion.frame*50-2 , 50, 45, 40, Lion.x, Lion.y)

        else:

            Lion.image.clip_draw(Lion.frame*50-2, 50, 45, 40, Lion.x, Lion.y)
            pass


class RunState:

    @staticmethod
    def enter(Lion, event):

        Lion.dir = Lion.velocity
        pass

    @staticmethod
    def exit(Lion, event):

        pass

    @staticmethod
    def do(Lion):
        Lion.frame = (Lion.frame + 1) % 4
        Lion.timer -= 1
        Lion.x +=Lion.velocity
        Lion.y += Lion.length
        Lion.x = clamp(25, Lion.x, 1020 - 25)
        Lion.y = clamp(25, Lion.y, 767 - 25)
        pass

    @staticmethod
    def draw(Lion):
        if Lion.velocity == 1:

            Lion.image.clip_draw(Lion.frame*100, 0, 60, 60, Lion.x, Lion.y)

        else:

            Lion.image.clip_draw(Lion.frame*100, 0, 60, 60, Lion.x, Lion.y)
            pass



class Lion:

    def __init__(self):
        self.x, self.y = 70 , 70
        self.image = load_image('Resource_Monster\\Stage1_enemy_Lion.png')
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