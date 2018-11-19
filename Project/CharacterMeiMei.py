from pico2d import *
from ball import Ball

import game_world
import random

PIXEL_PER_METER = (10.0 / 2.0)

RUN_SPEED_KMPH = 20.0

RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)

RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)

RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5

ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

FRAMES_PER_ACTION = 8


# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,SPACE_E,UP_DOWN,DOWN_DOWN,UP_UP,DOWN_UP = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_E,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN
}


# Boy States

class IdleState:

    @staticmethod
    def enter(MeiMei, event):
        MeiMei.time = get_time()
        if event == RIGHT_DOWN:
            MeiMei.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            MeiMei.velocity -= RUN_SPEED_PPS

        elif event == RIGHT_UP:
            MeiMei.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            MeiMei.velocity += RUN_SPEED_PPS

        elif event == DOWN_DOWN:
            MeiMei.length -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            MeiMei.length += RUN_SPEED_PPS

        elif event == DOWN_UP:
            MeiMei.length += RUN_SPEED_PPS
        elif event == UP_UP:
            MeiMei.length -= RUN_SPEED_PPS


        MeiMei.time = get_time()


    @staticmethod
    def exit(MeiMei, event):
        if event == SPACE_E:
            MeiMei.fire_ball()
        pass

    @staticmethod
    def do(MeiMei):
        MeiMei.frame = (MeiMei.frame + 1) % 8
        MeiMei.x = clamp(25, MeiMei.x, 1020 - 25)
        MeiMei.time = get_time()


    @staticmethod
    def draw(MeiMei):
        if MeiMei.dir == 1:

            MeiMei.image.clip_draw(70, 0, 60, 60, MeiMei.x, MeiMei.y)

        else:

            MeiMei.image.clip_draw(70, 0, 60, 60, MeiMei.x, MeiMei.y)


class RunState:

    @staticmethod
    def enter(MeiMei, event):
        if event == RIGHT_DOWN:
            MeiMei.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            MeiMei.velocity -=RUN_SPEED_PPS

        elif event == RIGHT_UP:
            MeiMei.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            MeiMei.velocity += RUN_SPEED_PPS

        elif event == DOWN_DOWN:
            MeiMei.length -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            MeiMei.length += RUN_SPEED_PPS

        elif event == DOWN_UP:
            MeiMei.length += RUN_SPEED_PPS
        elif event == UP_UP:
            MeiMei.length -= RUN_SPEED_PPS

        MeiMei.time = get_time()
        MeiMei.dir = MeiMei.velocity

    @staticmethod
    def exit(MeiMei, event):
        if event == SPACE_E:
            MeiMei.fire_ball()
        pass

    @staticmethod
    def do(MeiMei):
        MeiMei.frame = (MeiMei.frame + 1) % 8
        MeiMei.timer -= 1
        MeiMei.x += MeiMei.velocity
        MeiMei.y += MeiMei.length
        MeiMei.x = clamp(25, MeiMei.x, 1020 - 25)
        MeiMei.y = clamp(25, MeiMei.y, 767 - 25)
        MeiMei.time = get_time()


    @staticmethod
    def draw(MeiMei):
        if MeiMei.velocity == 1:

            MeiMei.image.clip_draw(260, 0, 60, 60, MeiMei.x, MeiMei.y)

        else:

            MeiMei.image.clip_draw(260, 0, 60, 60, MeiMei.x, MeiMei.y)





next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                DOWN_UP:RunState,DOWN_DOWN:RunState,UP_DOWN:RunState,UP_UP:RunState,
                SPACE_E: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
               DOWN_UP:IdleState,DOWN_DOWN:RunState,UP_DOWN:RunState,UP_UP:IdleState,
               SPACE_E: RunState}
}

class MeiMei:

    def __init__(self):
        self.x, self.y = 70 , 70
        self.image = load_image('Resource_Character\\CharacterMeiMei.png')
        self.font = load_font('Resource_Temporary\\ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0

        self.length=0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir * 3)
        game_world.add_object(ball, 1)

    def get_bb(self):
        # fill here
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)

        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time:%3.2f)' % self.time, (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

