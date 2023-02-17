from pygame import surface, transform, image, font

class Res:
    def __init__(self) -> None:
        self.playersprs = {}
        self.enemysprs = {}
        self.tilesprs = {}
        self.itemsprs = {}
        self.fonts = {}
        self.sounds = {}
        self.music = {}
        self.load()
    
    def load(self):
        self.playersprs["idle"] = image.load("assets/player/idle.png").convert_alpha()
        self.playersprs["walk"] = {}
        self.playersprs["jump"] = {}
        self.playersprs["fall"] = {}
        self.playersprs["attack"] = {}
        self.playersprs["hurt"] = {}
        self.playersprs["dead"] = {}
        # self.fonts["debug"] = font.Font("assets/fonts/debug.ttf", 20)