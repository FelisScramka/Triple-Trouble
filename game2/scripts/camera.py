class Camera:
    def __init__(self, pos) -> None:
        self.x, self.y = pos
    
    def update(self, newpos):
        self.x, self.y = newpos