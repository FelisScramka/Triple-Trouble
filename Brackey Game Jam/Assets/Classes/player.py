import pygame, math
from pygame.math import Vector2

from Assets.Classes.hitbox import Hitbox

class Player():
    def __init__(self, hitbox = Hitbox(0, 0, 64, 64), vel = Vector2()):
        self.sprite = pygame.image.load("Assets/Sprites/Player/Square1.png")
        self.hitbox = hitbox

        self.grounded = False
        self.walled = False
        
        self.gr_bf = 0
        self._gr_bf = 2
        
        self.vel = vel

        self.type = "sqr"

        self.act = "idle"
        self.anis = {"idle": [self.sprite]}
        self.ani_i = 0

    def draw(self, screen):
        try:
            image = self.anis[self.act + "_" + self.type][self.ani_i]
        except:
            image = self.sprite
        screen.blit(image, (self.hitbox.x, self.hitbox.y))

    def add_ani(self, act, sprites):
        self.anis[act] = sprites

    def ani(self):
        self.ani_i = (self.ani_i + 1) % len(self.anis[self.act + "_" + self.type])

    def set_act(self, act):
        if act in self.anis:
            self.act = act
        else:
            self.act = "idle"
        self.ani_i = 0
    
    def move_x(self, dt, hitboxs = []):
        self.hitbox.x += self.vel.x * dt

        if self.grounded:
            self.vel.x *= 0.83
        else:
            self.vel.x *= 0.94

        self.walled = 0
        for hb in hitboxs:
            collide = hb.collide(self.hitbox)
            if collide:
                if self.vel.x < 0:
                    self.hitbox.x = hb.x + hb.w
                    self.walled = -1
                elif self.vel.x >= 0:
                    self.hitbox.x = hb.x - self.hitbox.w
                    self.walled = 1

    def move_y(self, dt, hitboxs = []):
        self.hitbox.y += self.vel.y * dt
        self.vel.y = min(self.vel.y + 0.61, 14.1)
        
        self.gr_bf -= 1
        self.grounded = False
        for hb in hitboxs:
            collide = hb.collide(self.hitbox)
            if collide:
                if self.vel[1] < 0:
                    self.vel[1] = -0.006
                    self.hitbox.y = hb.y + hb.h
                elif self.vel[1] >= 0:
                    self.vel[1] = 0.006
                    self.hitbox.y = hb.y - self.hitbox.h
                    self.grounded = True
                    self.gr_bf = self._gr_bf
    
    def jump(self, j_bf):
        if self.gr_bf > 0 and j_bf > 0:
            self.vel[1] = -10.1
