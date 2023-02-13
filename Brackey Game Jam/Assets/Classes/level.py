class Level():
    def __init__(self, tilemap):
        #Format: [indexx, indexy, targetx, targety]
        self.buttons = {}
        
        self.tm = tilemap

        self.falling = []
        
        self.sqr_doors = []
        self.tri_doors = []
        self.cir_doors = []
        
        self.doors = []
        
    def update(self):
        """
        add vel into 'falling' blocks
        """
