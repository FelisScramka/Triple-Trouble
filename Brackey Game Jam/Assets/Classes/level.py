import pygame

from pygame.math import Vector2

import Assets.Classes.tilemap as tilemap
from Assets.Classes.hitbox import Hitbox

import Assets.Sprites.data as imgdata

blank = pygame.Surface((0, 0))

class Level(tilemap.Tilemap):
    def __init__(self, map_sprite, x, y, size_x, size_y, origin):
        #Format: [hitbox, targetx, targety]
        self.buttons = []

        self.origin = origin

        self.falling = {}
        
        self.sqr_doors = []
        self.tri_doors = []
        self.cir_doors = []
        
        self.doors = []

        super(Level, self).__init__(map_sprite, x, y, size_x, size_y)

    def add_btn(self, cords, target):
        self.buttons.append([self.data[cords]["hitbox"], target, False])
    
    def __str__(self) -> str:
        return self.__dict__.__str__()
    
    def __repr__(self) -> str:
        return self.__dict__.__repr__()

    def update(self, p, dt):
        rem_l = []
        for t in self.falling.keys():
            self.falling[t] = min(self.falling[t] + 0.61 * dt, 14.1)
            
            self.data[t]["render_pos"][1] += self.falling[t] * dt
            self.data[t]["hitbox"].y += self.falling[t] * dt

            pre_pos = (int((self.data[t]["hitbox"].x + self.size[0]) / self.size[0]), int((self.data[t]["hitbox"].y + self.size[1]) / self.size[1]))
            
            if self.data[pre_pos]["type"] != "air" and pre_pos != t:
                hit = self.data[pre_pos]["hitbox"]

                self.data[t]["render_pos"][1] = hit.y - self.data[t]["hitbox"].h
                self.data[t]["hitbox"].y = hit.y - self.data[t]["hitbox"].h
                rem_l.append(t)
                
            if p.hitbox.collide(self.data[(t[0], t[1])]["hitbox"]):
                p.die(self.origin)
        for t in rem_l:
            self.falling.pop(t)
        for btn in self.buttons:
            hb = Hitbox(btn[0].x, btn[0].y, btn[0].w, btn[0].h)
            ind = Hitbox(btn[0].x // imgdata.tile_sz[0], btn[0].y // imgdata.tile_sz[1], btn[0].w, btn[0].h)
            btile = self.data[(ind.x, ind.y)]
            if btn[2]:
                if btile["place"] in ["DLT", "TL", "DL", "L"]:
                    self.data[(ind.x, ind.y)]["hitbox"] = Hitbox(hb.x + 47, hb.y + 12, 1, 24)
                elif btile["place"] in ["TRD", "TR", "DR", "R"]:
                    self.data[(ind.x, ind.y)]["hitbox"] = Hitbox(hb.x + 0, hb.y + 12, 1, 24)
                for b in btn[1]:
                    if b[2] == "normal" and not (b[0], b[1]) in self.falling:
                        self.falling[(b[0], b[1])] = 0
                    elif b[2] == "dr":
                        self.data[(b[0], b[1])] = {"render_pos": [b[0] * self.size[0] + self.hitbox.x, b[1] * self.size[1] + self.hitbox.y], "sprite": blank, "hitbox": Hitbox(), "type": "air"}
            else:
                if btile["place"] in ["DLT", "TL", "DL", "L"]:
                    self.data[(ind.x, ind.y)]["hitbox"] = Hitbox(hb.x + 36, hb.y + 12, 12, 24)
                elif btile["place"] in ["TRD", "TR", "DR", "R"]:
                    self.data[(ind.x, ind.y)]["hitbox"] = Hitbox(hb.x + 0, hb.y + 12, 12, 24)
                for b in btn[1]:
                    tile = self.data[(b[0], b[1])]
                    if b[2] == "dr":
                        self.data[(b[0], b[1])] = {"render_pos": [b[0] * self.size[0] + self.hitbox.x, b[1] * self.size[1] + self.hitbox.y], "sprite": imgdata.dr, "hitbox": Hitbox(b[0] * self.size[0] + self.hitbox.x + 1, b[1] * self.size[1] + self.hitbox.y + 1, 46, 46), "type": "dr"}
                
    def check_btn(self, hbs):
        for btn in self.buttons:
            st = False
            for hb in hbs:
                if hb[0].collide(btn[0]):
                    st = True
            btn[2] = st
                    

