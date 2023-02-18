import pygame, math
from pygame.math import Vector2

from Assets.Classes.hitbox import Hitbox
import Assets.Classes.lvl_dat as lvl_dat
import Assets.Sprites.data as imgdata

import copy

class Player():
    def __init__(self, app, hitbox = Hitbox(0, 0, 0, 0), vel = Vector2()):
        self.sprite = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Square1.png"), (48, 48))
        self.hitbox = hitbox
        self.app = app
        
        self.hitbox.w = imgdata.tile_sz[0]
        self.hitbox.h = imgdata.tile_sz[1]

        self.grounded = False
        self.walled = False
        
        self.gr_bf = 0
        self._gr_bf = 2
        
        self.vel = vel

        self.shapes = ["sqr", "tri", "cir"]
        self.s_i = 0

        self.type = "sqr"

        self.act = "idle"
        self.anis = {"idle": [self.sprite]}
        self.ani_i = 0

        self.body = []
        self.dths = 0

    def draw(self, screen):
        try:
            image = self.anis[self.act + "_" + self.type][self.ani_i]
        except:
            image = self.sprite
        screen.blit(image, (self.hitbox.x, self.hitbox.y))

    def draw_body(self, screen):
        for b in self.body:
            screen.blit(self.sprite, (b[0].x, b[0].y))

    def add_ani(self, act, sprites):
        self.anis[act] = sprites

    def ani(self):
        self.ani_i = (self.ani_i + 1) % len(self.anis[self.act + "_" + self.type])

    def set_act(self, act):
        if self.act == act or not (act + "_" + self.type) in self.anis:
            return
        self.act = act
        self.ani_i = 0
    
    def move_x(self, dt):
        if self.grounded:
            self.vel.x *= 0.83
        else:
            self.vel.x *= 0.94
        
        self.hitbox.x += self.vel.x * dt

    def collide_x(self, origin, lvl, lvl_i, hitboxs = []):
        self.walled = 0
        d = False
        for hb in hitboxs:
            if hb["type"] == "air":
                continue
            hit = hb["hitbox"]
            collide = hit.collide(self.hitbox)
            if collide:
                if hb["type"] == "kill":
                    d = True
                elif hb["type"] == "pt":
                    lvl_i[0] += 1
                    self.reset(origin, lvl, lvl_i)
                if self.vel.x < 0:
                    self.hitbox.x = hit.x + hit.w
                    self.walled = -1
                elif self.vel.x >= 0:
                    self.hitbox.x = hit.x - self.hitbox.w
                    self.walled = 1
                    
        for b in self.body:
            if self.hitbox.collide(b[0]):
                if self.vel[0] < 0:
                    self.vel[0] = -0.006
                    self.hitbox.x = b[0].x + b[0].w
                    self.walled = -1
                elif self.vel[0] >= 0:
                    self.vel[0] = 0.006
                    self.hitbox.x = b[0].x - self.hitbox.w
                    self.walled = 1
        if d:
            self.die(origin, lvl, lvl_i)

    def move_y(self, dt):
        self.vel.y = min(self.vel.y + 0.61 * dt, 14.1)
        self.hitbox.y += self.vel.y * dt

        for b in self.body:
            b[0].add(0, b[1].y)
            b[1].y = min(b[1].y + 0.61 * dt, 14.1)

    def collide_y(self, origin, lvl, lvl_i, hitboxs = []):
        self.gr_bf -= 1
        self.grounded = False
        d = False
        for hb in hitboxs:
            if hb["type"] == "air":
                continue
            hit = hb["hitbox"]
            collide = hit.collide(self.hitbox)
            if collide:
                if hb["type"] == "kill":
                    d = True
                elif hb["type"] == "pt":
                    lvl_i[0] += 1
                    self.reset(origin, lvl, lvl_i)
                if self.vel[1] < 0:
                    self.vel[1] = -0.006
                    self.hitbox.y = hit.y + hit.h
                elif self.vel[1] >= 0:
                    self.vel[1] = 0.006
                    self.hitbox.y = hit.y - self.hitbox.h
                    self.grounded = True
                    self.gr_bf = self._gr_bf
            for b in self.body:
                collide = hit.collide(b[0])
                if collide:
                    if b[1].y < 0:
                        b[1].y = 0
                        b[0].y = hit.y + hit.h
                    elif b[1].y >= 0:
                        b[1].y = 0
                        b[0].y = hit.y - b[0].h
                        
        for b in self.body:
            if self.hitbox.collide(b[0]):
                if self.vel[1] < 0:
                    self.vel[1] = -0.006
                    self.hitbox.y = b[0].y + b[0].h
                elif self.vel[1] >= 0:
                    self.vel[1] = 0.006
                    self.hitbox.y = b[0].y - self.hitbox.h
                    self.grounded = True
                    self.gr_bf = self._gr_bf
        if d:
            self.die(origin, lvl, lvl_i)

    def update(self, j_bf):
        if self.walled:
            if self.vel.y > 0:
                self.vel.y *= 0.86

        self.jump(j_bf)

        self.ani()
    
    def jump(self, j_bf):
        if self.gr_bf > 0 and j_bf > 0:
            self.vel[1] = -10.6

    def reset(self, org_pos, lvl, lvl_id):
        self.hitbox = Hitbox(org_pos.x, org_pos.y)
        
        self.hitbox.w = imgdata.tile_sz[0]
        self.hitbox.h = imgdata.tile_sz[1]

        self.grounded = False
        self.walled = False
        
        self.gr_bf = 0
        self._gr_bf = 2
        
        self.vel = Vector2()

        self.s_i = 0

        self.type = "sqr"

        self.body = []
        self.dths = 0

        print(lvl_id)
        newlvl = copy.copy(eval(f"lvl_dat.lvl{lvl_id[0]}"))
        self.app.set_lvl(newlvl)

    def die(self, org_pos, lvl, lvl_i):
        self.body.append([Hitbox(self.hitbox.x, self.hitbox.y, self.hitbox.w, self.hitbox.h), Vector2(0, 0)])
        
        self.hitbox.x = org_pos.x
        self.hitbox.y = org_pos.y
        
        self.vel.x = 0
        self.vel.y = 0

        self.s_i = (self.s_i + 1) % 3
        self.type = self.shapes[self.s_i]

        self.dths += 1

        if self.dths == 3:
            self.reset(org_pos, lvl, lvl_i)

