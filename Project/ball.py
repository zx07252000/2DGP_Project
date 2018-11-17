from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, move = 1,length=1,frame=1):
        if Ball.image == None:
            Ball.image = load_image('Resource_Character\\Ball_1.png')
        self.x, self.y, self.velocity ,self.length,self.frame= x, y, move,length,frame

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 15, self.x + 10, self.y + 15
        #충돌처리

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 16, 30, self.x, self.y)

    def update(self):
        self.x += self.length+100

        if self.x < 25 or self.x > 100000:
            game_world.remove_object(self)
