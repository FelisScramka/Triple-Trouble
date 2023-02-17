import pygame, sys, time

import copy

from pygame.math import Vector2

import Assets.Classes.player as player
import Assets.Classes.tilemap as tilemap
import Assets.Classes.level as level
from Assets.Classes.hitbox import Hitbox

import Assets.Sprites.data as imgdata

import Assets.Classes.lvl_dat as lvl_dat

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

last_t = time.time()

lvl_id = [1]

tm = copy.copy(eval(f"lvl_dat.lvl{lvl_id[0]}"))

p = player.Player()

p.add_ani("idle_sqr", imgdata.idle_sqr_frames)
p.add_ani("idle_tri", imgdata.idle_tri_frames)
p.add_ani("idle_cir", imgdata.idle_cir_frames)

p.add_ani("run_sqr", imgdata.run_sqr_frames)
p.add_ani("run_tri", imgdata.run_tri_frames)
p.add_ani("run_cir", imgdata.run_cir_frames)

p.set_act("idle")
p.type = "sqr"

j_bf = 0
_j_bf = 4

def lerp(v1, v2, t):
    return Vector2(v1.x + (v2.x - v1.x) * t, v1.y + (v2.y - v1.y) * t)

mode = 1

while True:
    if mode == 1:
        screen.fill((26, 22, 35))

        dt = (time.time() - last_t) * 60
        last_t = time.time()

        j_bf -= 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    j_bf = _j_bf

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and p.walled != -1:
            p.vel = lerp(p.vel, Vector2(-5.2, p.vel.y), 0.4)
            p.set_act("run")
        if keys[pygame.K_d] and p.walled != 1:
            p.vel = lerp(p.vel, Vector2(5.2, p.vel.y), 0.4)
            p.set_act("run")
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            p.set_act("idle")

        bds = list(p.body)
        bds.append([p.hitbox, 0])

        p.move_x(dt)
        tm.check_btn(bds)
        p.collide_x(tm.origin, tm, lvl_id, tm.data.values())

        bds = list(p.body)
        bds.append([p.hitbox, 0])

        p.move_y(dt)
        tm.check_btn(bds)
        p.collide_y(tm.origin, tm, lvl_id, tm.data.values())

        p.update(j_bf)

        for hb in tm.data.keys():
            if tm.data[hb]["type"] == "air":
                continue
            hit = tm.data[hb]["hitbox"]
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(hit.x, hit.y, hit.w, hit.h))

        tm.update(p, dt)

        p.draw(screen)
        p.draw_body(screen)
        tm.draw(screen)

        clock.tick(60)
        pygame.display.update()
