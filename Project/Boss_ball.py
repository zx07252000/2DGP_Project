from pico2d import *
import game_world
import game_framework
import math
import random

class Boss_Ball:
    MIN_Throw_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_Throw_SPEED = 200  # 200 pps = 6 meter per sec
    image = None

    def __init__(self,i):
        if Boss_Ball.image == None:
            Boss_Ball.image = load_image('Resource_Monster\\Boss_Bullet.png')
        self.x, self.y, self.velocity ,self.length,self.frame= 900, 100*i, 1,1,1
        self.Throw_Speed=300
        self.ball_change=0
        self.ball_count=0


    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
        #충돌처리

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 25, 30, self.x, self.y)
        draw_rectangle(*self.get_bb())
    def update(self):
        self.x -= self.Throw_Speed*game_framework.frame_time
        self.frame =(self.frame+1)%5
        if self.x < 25 and self.ball_change==0:
            self.x=900
            self.y+=50
            self.ball_change=1
            self.ball_count+=1
        if self.x < 25 and self.ball_change==1:
            self.x=900
            self.y-=50
            self.ball_change=1
            self.ball_count+=1

        if self.ball_count==3:
            pass
    def stop(self):
        self.Throw_Speed = 0

class Boss2_Ball:
    MIN_Throw_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_Throw_SPEED = 200  # 200 pps = 6 meter per sec
    image = None

    def __init__(self, i):
        if Boss2_Ball.image == None:
            Boss2_Ball.image = load_image('Resource_Monster\\Boss_Bullet.png')
        self.radian = 30
        self.x, self.y, self.velocity, self.length, self.frame = 20*(i+5)*math.cos(math.radians(self.radian))+500,random.randint(100, 700) , 1, 1, 1
        self.Throw_Speed = 200
        self.ball_change = 0
        self.ball_count = 0


    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
        # 충돌처리

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 25, 30, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= self.Throw_Speed*game_framework.frame_time

        #self.y +=self.Throw_Speed*game_framework.frame_time-20
        self.radian=self.radian+10



        self.frame = (self.frame + 1) % 3
        self.x = clamp(25, self.x, 5000 - 25)
        self.y = clamp(25, self.y, 767 - 75)


        if self.x < 30 and self.ball_change == 0:
            self.x = 800
            self.y =random.randint(100, 700)
            self.ball_change = 1
            self.ball_count += 1
        if self.x < 30 and self.ball_change == 1:
            self.x = 800
            self.y =random.randint(50, 700)
            self.ball_change = 1
            self.ball_count += 1

        if self.ball_count == 3:
            pass

    def stop(self):
        self.Throw_Speed = 0