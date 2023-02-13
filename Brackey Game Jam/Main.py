import pygame, sys, time

from pygame.math import Vector2

import Assets.Classes.player as player
import Assets.Classes.tilemap as tilemap
import Assets.Sprites.data as imgdata

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

last_t = time.time()

tm = tilemap.Tilemap(pygame.image.load("Assets/Maps/Map1.png"), 0, 0, imgdata.tile_sz[0], imgdata.tile_sz[1])

tm.addType("gr", (255, 255, 255), imgdata.gr15)

tm.addTile("gr", "DR", imgdata.gr0)
tm.addTile("gr", "LDR", imgdata.gr1)
tm.addTile("gr", "DL", imgdata.gr2)
tm.addTile("gr", "D", imgdata.gr3)
tm.addTile("gr", "TRD", imgdata.gr4)
tm.addTile("gr", "F", imgdata.gr5)
tm.addTile("gr", "DLT", imgdata.gr6)
tm.addTile("gr", "TD", imgdata.gr7)
tm.addTile("gr", "TR", imgdata.gr8)
tm.addTile("gr", "RTL", imgdata.gr9)
tm.addTile("gr", "TL", imgdata.gr10)
tm.addTile("gr", "T", imgdata.gr11)
tm.addTile("gr", "R", imgdata.gr12)
tm.addTile("gr", "LR", imgdata.gr13)
tm.addTile("gr", "L", imgdata.gr14)
tm.addTile("gr", "E", imgdata.gr15)
tm.addTile("gr", "ITL", imgdata.gr16)
tm.addTile("gr", "ITR", imgdata.gr17)
tm.addTile("gr", "IDL", imgdata.gr18)
tm.addTile("gr", "IDR", imgdata.gr19)

tm.addType("btn", (255, 0, 0), imgdata.btn0, 1)

tm.addTile("btn", "DLT", imgdata.btn0, [36, 12, 12, 24])
tm.addTile("btn", "TRD", imgdata.btn1, [0, 12, 12, 24])

tm.addType("spkt", (240, 240, 240), imgdata.spk3, 1, [1, 0, 46, 7])
tm.addType("spkd", (225, 225, 225), imgdata.spk2, 1, [1, 41, 46, 7])
tm.addType("spkl", (210, 210, 210), imgdata.spk1, 1, [0, 1, 7, 47])
tm.addType("spkr", (195, 195, 195), imgdata.spk0, 1, [46, 1, 7, 47])

tm.write()

p = player.Player()

p.add_ani("idle_sqr", imgdata.idle_sqr_frames)
p.add_ani("idle_tri", imgdata.idle_tri_frames)
p.add_ani("idle_cir", imgdata.idle_cir_frames)

p.add_ani("run_sqr", imgdata.run_sqr_frames)

p.set_act("idle")
p.type = "sqr"

j_bf = 0
_j_bf = 4

def lerp(v1, v2, t):
    return Vector2(v1.x + (v2.x - v1.x) * t, v1.y + (v2.y - v1.y) * t)

while True:
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
        p.vel = lerp(p.vel, Vector2(-4.8, p.vel.y), 0.4)
        p.set_act("run")
    if keys[pygame.K_d] and p.walled != 1:
        p.vel = lerp(p.vel, Vector2(4.8, p.vel.y), 0.4)
        p.set_act("run")
    if not keys[pygame.K_a] and not keys[pygame.K_d]:
        p.set_act("idle")

    p.update(dt, j_bf, tm.data.values())

    p.ani()
    
    #for hb in tm.hitboxs.values():
        #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(hb.x, hb.y, hb.w, hb.h))

    p.draw(screen)
    tm.draw(screen)

    clock.tick(60)
    pygame.display.update()
