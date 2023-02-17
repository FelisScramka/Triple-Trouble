from scripts.enemies.enemy import Enemy
from pygame import math
import typing
from pygame.surface import Surface

class Enemy1Manager:
    def __init__(self) -> None:
        self.enemies: typing.List[Enemy1] = []
    
    def update(self, dt):
        for enemy in self.enemies:
            enemy.update(dt)

# From past experience IK that returning stuff when they should be killed is bad,
# which is why I'm going to use Managers to handle enemy deletion and other stuff

class Enemy1(Enemy):
    def __init__(self, cam, pos, targetpos, sprs: typing.Dict[str, Surface], hp, speed, rect=None) -> None:
        super().__init__(cam, pos, targetpos, sprs, hp, speed, rect)
    
    def _move(self, dt):
        vec = math.Vector2([self.targetpos[0]-self.x, self.targetpos[1]-self.y])
        mov = [0, 0]
        if vec.length() != 0:
            dir = vec.normalize()
            mov = [dir[0]*self.speed*dt, dir[1]*self.speed*dt]
        else:
            pass
        self.update_pos((self.x + mov[0], self.y + mov[1]))

    def update(self, dt):
        self._move(dt)