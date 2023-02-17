import pygame as pg
import sys
import time
import math
import random
import os
import json
import asyncio
from scripts.camera import Camera
from scripts.res import Res
from scripts.player import Player

pg.font.init()

class App:
    def __init__(self):
        self.screen = pg.display.set_mode((240, 240), pg.RESIZABLE | pg.SCALED)
        self.clock = pg.time.Clock()
        self.running = True
    
    def update(self):
        self.dt = self.clock.tick(60) / 100
        self.player.update(self.keys, self.mouse, self.mpos, self.dt)
        self.camera.update((0, 0)) # player pos
    
    def draw(self):
        self.screen.fill("black")
        self.player.draw(self.screen)

    def input(self):
        self.keys = pg.key.get_pressed()
        self.mouse = pg.mouse.get_pressed()
        self.mpos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

    def start(self):
        self.res = Res()
        self.res.load()
        self.camera = Camera((0, 0))
        self.player = Player(self, self.camera, (0, 0), self.res.playersprs["idle"])

    async def run(self):
        self.start()
        while self.running:
            self.input()
            self.update()
            self.draw()
            self.clock.tick(60)
            pg.display.update()
            await asyncio.sleep(0)


if __name__ == "__main__":
    app = App()
    asyncio.run(app.run())