import pygame

from pygame.math import Vector2

import Assets.Classes.tilemap as tilemap
from Assets.Classes.hitbox import Hitbox

blank = pygame.Surface((0, 0))

class Level(tilemap.Tilemap):
    def __init__(self, map_sprite, x, y, size_x, size_y, origin):
        #Format: [hitbox, targetx, targety]
        self.buttons = []

        self.origin = Vector2()

        self.falling = {}
        
        self.sqr_doors = []
        self.tri_doors = []
        self.cir_doors = []
        
        self.doors = []

        super(Level, self).__init__(map_sprite, x, y, size_x, size_y)
        
    def update(self, p, dt):
        rem_l = []
        for t in self.falling.keys():
            self.falling[t] = min(self.falling[t] + 0.61 * dt, 14.1)
            
            self.data[t]["render_pos"][1] += self.falling[t] * dt
            self.data[t]["hitbox"].y += self.falling[t] * dt
            
            if self.data[(t[0], int(t[1] + self.falling[t]))]["type"] != "air" and (t[0], int(t[1] + self.falling[t])) != t:
                hit = self.data[(t[0], int(t[1] + self.falling[t]))]["hitbox"]

                self.data[t]["render_pos"][1] = hit.y - self.data[t]["hitbox"].h
                self.data[t]["hitbox"].y = hit.y - self.data[t]["hitbox"].h
                rem_l.append(t)
                
            if p.hitbox.collide(self.data[(t[0], t[1])]["hitbox"]):
                p.die(self.origin)
        for t in rem_l:
            self.falling.pop(t)
                
    def check_btn(self, hb):
        for btn in self.buttons:
            if hb.collide(btn[0]):
                tile = self.data[(btn[1], btn[2])]
                if tile == None:
                    continue
                
                if tile["type"] == "normal" and not (btn[1], btn[2]) in self.falling:
                    self.falling[(btn[1], btn[2])] = 0
                if tile["type"] == "ndoor":
                    self.data[(btn[1], btn[2])] = {"render_pos": [btn[1] * self.size[0] + self.hitbox.x, btn[2] * self.size[1] + self.hitbox.y], "sprite": blank, "hitbox": Hitbox(), "type": "air"}

