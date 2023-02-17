import pygame as pg
from scripts.object import Object

class Player(Object):
    def __init__(self, app, camera, pos, surf) -> None:
        super().__init__(camera, pos, surf)
        self.app = app
        self.hp = 100
        self.speed = 20
        self.vel = (0, 0)
        self.jumping = False # maybe jump mechanics later?

    def _move(self, keys, dt):
        mov = [0, 0]
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            mov[0] -= 1
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            mov[0] += 1
        if keys[pg.K_w] or keys[pg.K_UP]:
            mov[1] -= 1
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            mov[1] += 1
        mov = [mov[0]*self.speed*dt, mov[1]*self.speed*dt]
        self.update_pos((self.x + mov[0], self.y + mov[1]))

    def update(self, keys, mclicks, mpos, dt):
        self._move(keys, dt)

    def draw(self, screen):
        screen.blit(self.surf, (self.x - self.cam.x, self.y - self.cam.y))

        pg.draw.rect(screen, (255, 0, 0), (self.x - self.cam.x, self.y - self.cam.y - 10, 50, 5))
        pg.draw.rect(screen, (0, 255, 0), (self.x - self.cam.x, self.y - self.cam.y - 10, self.hp, 5))
        if self.debugmode:
            pg.draw.rect(screen, "red", (self.rect.x - self.cam.x, self.rect.y - self.cam.y - 10, self.rect.w, self.rect.h), 3)
