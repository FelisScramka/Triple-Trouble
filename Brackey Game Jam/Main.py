import pygame as pg
import sys, time
import asyncio
import copy

from pygame.math import Vector2

import Assets.Classes.player as player
import Assets.Classes.tilemap as tilemap
import Assets.Classes.level as level
from Assets.Classes.hitbox import Hitbox

import Assets.Sprites.data as imgdata

import Assets.Classes.lvl_dat as lvl_dat

pg.init()

def lerp(v1, v2, t):
    return Vector2(v1.x + (v2.x - v1.x) * t, v1.y + (v2.y - v1.y) * t)

class App:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode((800, 800))
        self.clock = pg.time.Clock()
        self.last_t = time.time()
        self.lvl_id = [1]
        self.tm = copy.copy(eval(f"lvl_dat.lvl{self.lvl_id[0]}"))
        self.mode = 1
        self.player = player.Player(self)

        self.player.add_ani("idle_sqr", imgdata.idle_sqr_frames)
        self.player.add_ani("idle_tri", imgdata.idle_tri_frames)
        self.player.add_ani("idle_cir", imgdata.idle_cir_frames)

        self.player.add_ani("run_sqr", imgdata.run_sqr_frames)
        self.player.add_ani("run_tri", imgdata.run_tri_frames)
        self.player.add_ani("run_cir", imgdata.run_cir_frames)

        self.player.set_act("idle")
        self.player.type = "sqr"
        self.j_bf = 0
        self._j_bf = 4
    
    def draw(self):
        self.screen.fill((26, 22, 35))
        self.player.draw(self.screen)
        self.player.draw_body(self.screen)
        self.tm.draw(self.screen)
    
    def update(self):
        self.tm.update(self.player, self.dt)
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and self.player.walled != -1:
            self.player.vel = lerp(self.player.vel, Vector2(-5.2, self.player.vel.y), 0.4)
            self.player.set_act("run")
        if keys[pg.K_d] and self.player.walled != 1:
            self.player.vel = lerp(self.player.vel, Vector2(5.2, self.player.vel.y), 0.4)
            self.player.set_act("run")
        if not keys[pg.K_a] and not keys[pg.K_d]:
            self.player.set_act("idle")
        
        bds = list(self.player.body)
        bds.append([self.player.hitbox, 0])

        self.player.move_x(self.dt)
        self.tm.check_btn(bds)
        self.player.collide_x(self.tm.origin, self.tm, self.lvl_id, self.tm.data.values())

        bds = list(self.player.body)
        bds.append([self.player.hitbox, 0])

        self.player.move_y(self.dt)
        self.tm.check_btn(bds)
        self.player.collide_y(self.tm.origin, self.tm, self.lvl_id, self.tm.data.values())

        self.player.update(self.j_bf)

        for hb in self.tm.data.keys():
            if self.tm.data[hb]["type"] == "air":
                continue
            hit = self.tm.data[hb]["hitbox"]
            pg.draw.rect(self.screen, (255, 0, 0), pg.Rect(hit.x, hit.y, hit.w, hit.h))

    def input(self):
        self.j_bf -= 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.j_bf = self._j_bf

    def start(self):
        pass

    async def run(self):
        self.start()
        while True:
            if self.mode == 1:
                # self.dt = self.clock.tick(60)
                self.dt = self.clock.tick(60)/20
                self.input()
                self.update()
                self.draw()
                pg.display.update()
                await asyncio.sleep(0)

    def set_lvl(self, new_lvl):
        self.tm = new_lvl

if __name__ == "__main__":
    app = App()
    asyncio.run(app.run())
