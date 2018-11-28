from pico2d import *
import game_world
import game_framework


class Boss_Ball:
    MIN_Throw_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_Throw_SPEED = 200  # 200 pps = 6 meter per sec
    image = None

    def __init__(self,i):
        if Boss_Ball.image == None:
            Boss_Ball.image = load_image('Resource_Monster\\Boss_Bullet.png')
        self.x, self.y, self.velocity ,self.length,self.frame= 200*i, 300, 1,1,1
        self.Throw_Speed=300

    def get_bb(self):
        return self.x - 10, self.y - 15, self.x + 10, self.y + 15
        #충돌처리

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 16, 30, self.x, self.y)

    def update(self):
        self.x -= self.Throw_Speed*game_framework.frame_time

        if self.x > 1060:
            game_world.remove_object(self)

    def stop(self):
        self.Throw_Speed = 0