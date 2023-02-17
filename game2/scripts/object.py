from pygame import surface, transform, draw

class Object:
    def __init__(self, camera, pos, surf, rect=None, debugmode=False) -> None:
        self.cam = camera
        self.x, self.y = pos
        self.rect = rect if rect is not None else surf.get_rect()
        self.surf = surf
        self.jump_height = 0
        self.debugmode = debugmode

    def draw(self, screen) -> None:
        screen.blit(self.surf, (self.x - self.cam.x, self.y - self.cam.y))
        if self.debugmode:
            draw.rect(screen, "red", (self.rect.x - self.cam.x, self.rect.y - self.cam.y - 10, self.rect.w, self.rect.h), 3)

    def update_pos(self, newpos, jump_height=None) -> None:
        self.x, self.y = newpos
        if jump_height is not None:
            self.jump_height = jump_height
        self.rect.topleft = (self.x, self.y)