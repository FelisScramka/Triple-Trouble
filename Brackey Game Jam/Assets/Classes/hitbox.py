import pygame
from pygame.math import Vector2

class Hitbox():
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def collide(self, hitbox):
        if (self.x < hitbox.x + hitbox.w) & \
            (self.x + self.w > hitbox.x) & \
            (self.y < hitbox.y + hitbox.h) & \
            (self.y + self.h > hitbox.y):
            return True
        return False

    def add(self, x = 0, y = 0):
        self.x += x
        self.y += y
