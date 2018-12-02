from pico2d import *
import game_framework
import game_world
import math
import random
import GamePlay_Stage2
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

PIXEL_PER_METER = (10.0 / 0.3)

RUN_SPEED_KMPH = 30.0

RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)

RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)

RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5

ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

FRAMES_PER_ACTION = 8

class Mask:
    image = None

    def __init__(self, i):
        self.x, self.y = 1000+200*i , random.randint(100,700)
        self.image = load_image('Resource_Monster\\Stage2_enemy_mask.png')
        self.dir = random.random()*2*math.pi
        self.velocity = random.randint(10,20)
        self.frame = 0
        self.timer = 1.0
        self.speed = 0
        self.length=random.randint(10,20)
        self.length_count=0
        self.x_change=0
        self.build_behavior_tree()

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random() * 2 * math.pi

        return BehaviorTree.SUCCESS
        pass

    def find_player(self):
        CharacterMeiMei = GamePlay_Stage2.get_CharacterMeiMei()

        distance = (CharacterMeiMei.x - self.x) ** 2 + (CharacterMeiMei.y - self.y) ** 2
        if distance < (PIXEL_PER_METER * 10) ** 2:
            self.dir = math.atan2(CharacterMeiMei.y - self.y, CharacterMeiMei.x - self.x)
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass

    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        return BehaviorTree.SUCCESS
        pass

    def build_behavior_tree(self):
        wander_node = LeafNode("Wander", self.wander)
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node)
        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_children(chase_node, wander_node)
        self.bt = BehaviorTree(wander_chase_node)
        pass

    def update(self):
        self.bt.run()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        if self.x<30:
            self.x=1500



        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time-10
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(25, self.x, 5000 - 25)
        self.y = clamp(25, self.y, 767 - 75)
        pass


    def draw(self):
        self.image.clip_draw( 50 , 50, 45, 40,  self.x,  self.y)
        draw_rectangle(*self.get_bb())

        pass
