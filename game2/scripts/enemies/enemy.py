from scripts.object import Object
import typing
from pygame.surface import Surface

class Enemy(Object):
    def __init__(self, cam, pos, targetpos, sprs: typing.Dict[str, Surface], hp, speed, rect=None) -> None:
        super().__init__(cam, pos, self.sprs["idle"], rect)
        self.hp = 100
        self.speed = 20
        self.vel = (0, 0)
        self.jumping = False
        self.sprs = sprs
        self.targetpos = targetpos
    
    def update(self, dt):
        pass