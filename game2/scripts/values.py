import random


class Values: # This class is used to store the probability values of the different types of factors in game
    def __init__(self) -> None:
        self.randomize()
    
    def __str__(self) -> str:
        return self.__dict__.__str__()

    def __repr__(self) -> str:
        return self.__dict__.__repr__()
    
    def randomize(self):
        self.enemy1 = random.randrange(10, 90)/100
        self.enemy2 = random.randrange(10, 90)/100
        self.enemy3 = random.randrange(10, 90)/100
        self.playermaxhp = random.randrange(10, 90)
        self.playermaxspeed = random.randrange(15, 55)
        self.playermaxjump = random.randrange(10, 90)
        self.playerdamage = random.randrange(10, 90)
