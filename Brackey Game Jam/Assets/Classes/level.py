import pygame

import Assets.Classes.tilemap
from Assets.Classes.hitbox import Hitbox

blank = pygame.Surface((0, 0))

class Level(tilemap.Tilemap):
    def __init__(self, map_sprite, x, y, size_x, size_y, origin):
        #Format: [hitbox, targetx, targety]
        self.buttons = {}

        self.origin = Vector2()

        self.falling = {}
        
        self.sqr_doors = []
        self.tri_doors = []
        self.cir_doors = []
        
        self.doors = []

        super(Level).__init__(map_sprite, x, y, size_x, size_y)
        
    def update(self, p):
        for t in falling.keys():
            self.data[t]["render_pos"][1] += falling[t]
            self.data[t]["hitbox"].y += falling[t]
            
            falling[t] = min(falling[t] + 0.61 * dt, 14.1)
            
            if self.data[(t[0], t[1] + falling[t])]["type"] == "air":
                hit = self.data[(t[0], t[1] + falling[t])]["hitbox"]
                
                falling[t] = None
                self.data[(t[0], t[1] + falling[t])]["hitbox"].y = hit.y - self.data[(t[0], t[1] + falling[t])]["hitbox"].h

            if p.hitbox.collide(self.data[(t[0], t[1] + falling[t])]["hitbox"]):
                p.die(self.origin)
                
                
    def check_btn(self, hb):
        for btn in self.buttons:
            if hb.collide(btn[0]):
                tile = self.data[(btn[1], btn[2])]
                if tile == None:
                    continue
                
                if tile["type"] == "normal":
                    self.falling[(btn[1], btn[2])] = 0
                if tile["type"] == "ndoor":
                    self.data[(btn[1], btn[2])] = {"render_pos": [btn[1] * self.size[0] + self.hitbox.x, btn[2] * self.size[1] + self.hitbox.y], "sprite": blank, "hitbox": Hitbox(), "type": "air"}

