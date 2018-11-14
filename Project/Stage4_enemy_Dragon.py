from pico2d import *
import game_world
import random

class IdleState:

    @staticmethod
    def enter(Dragon, event):

        Dragon.velocity-=1
        Dragon.x=1050
        Dragon.y =random.randint(100,700)

        pass


    @staticmethod
    def exit(Dragon, event):
        pass

    @staticmethod
    def do(Dragon):
        Dragon.frame = (Dragon.frame + 1) % 4
        Dragon.x = clamp(25, Dragon.x, 1020 - 25)
        Dragon.x+=Dragon.velocity

        pass



    @staticmethod
    def draw(Dragon):
        if Dragon.dir == 1:

            Dragon.image.clip_draw(Dragon.frame*50-2 , 50, 45, 40, Dragon.x, Dragon.y)

        else:

            Dragon.image.clip_draw(Dragon.frame*50-2, 50, 45, 40, Dragon.x, Dragon.y)
            pass


class RunState:

    @staticmethod
    def enter(Dragon, event):

        Dragon.dir = Dragon.velocity
        pass

    @staticmethod
    def exit(Dragon, event):

        pass

    @staticmethod
    def do(Dragon):
        Dragon.frame = (Dragon.frame + 1) % 4
        Dragon.timer -= 1
        Dragon.x +=Dragon.velocity
        Dragon.y += Dragon.length
        Dragon.x = clamp(25, Dragon.x, 1020 - 25)
        Dragon.y = clamp(25, Dragon.y, 767 - 25)
        pass

    @staticmethod
    def draw(Dragon):
        if Dragon.velocity == 1:

            Dragon.image.clip_draw(Dragon.frame*100, 0, 60, 60, Dragon.x, Dragon.y)

        else:

            Dragon.image.clip_draw(Dragon.frame*100, 0, 60, 60, Dragon.x, Dragon.y)
            pass



class Dragon:

    def __init__(self):
        self.x, self.y = 70 , 70
        self.image = load_image('Resource_Monster\\Stage1_enemy_Dragon.png')
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