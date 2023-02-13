import pygame, sys, time

from pygame.math import Vector2

import Assets.Classes.player as player
import Assets.Classes.tilemap as tilemap
import Assets.Sprites.data as imgdata

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

last_t = time.time()

tm = tilemap.Tilemap(pygame.image.load("Assets/Maps/Map1.png"), 0, 0, 64, 64)

tm.addType("gr", (255, 255, 255), imgdata.gr4)

tm.addTile("gr", "DR", imgdata.gr0)
tm.addTile("gr", "LDR", imgdata.gr1)
tm.addTile("gr", "DL", imgdata.gr2)
tm.addTile("gr", "TRD", imgdata.gr3)
tm.addTile("gr", "F", imgdata.gr4)
tm.addTile("gr", "DLT", imgdata.gr5)
tm.addTile("gr", "TR", imgdata.gr6)
tm.addTile("gr", "RTL", imgdata.gr7)
tm.addTile("gr", "TL", imgdata.gr8)

tm.write()

p = player.Player()

p.add_ani("idle_sqr", imgdata.idle_sqr_frames)
p.add_ani("idle_tri", imgdata.idle_tri_frames)
p.add_ani("idle_cir", imgdata.idle_cir_frames)

p.set_act("idle")
p.type = "sqr"

j_bf = 0
_j_bf = 4

def lerp(v1, v2, t):
    return Vector2(v1.x + (v2.x - v1.x) * t, v1.y + (v2.y - v1.y) * t)

while True:
    screen.fill((0, 0, 0))

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
                
    p.jump(j_bf)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and p.walled != -1:
        p.vel = lerp(p.vel, Vector2(-4.4, p.vel.y), 0.4)
    if keys[pygame.K_d] and p.walled != 1:
        p.vel = lerp(p.vel, Vector2(4.4, p.vel.y), 0.4)

    p.move_x(dt, tm.hitboxs.values())
    p.move_y(dt, tm.hitboxs.values())

    p.ani()

    p.draw(screen)
    tm.draw(screen)

    clock.tick(60)
    pygame.display.update()
