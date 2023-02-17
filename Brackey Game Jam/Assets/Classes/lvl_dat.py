import pygame

import Assets.Classes.level as level
import Assets.Sprites.data as imgdata

from pygame.math import Vector2

def create_lvl(img):
    lvl = level.Level(img, 0, 0, imgdata.tile_sz[0], imgdata.tile_sz[1], Vector2())

    lvl.addType("gr", (255, 255, 255), imgdata.gr15)

    lvl.addTile("gr", "DR", imgdata.gr0)
    lvl.addTile("gr", "LDR", imgdata.gr1)
    lvl.addTile("gr", "DL", imgdata.gr2)
    lvl.addTile("gr", "D", imgdata.gr3)
    lvl.addTile("gr", "TRD", imgdata.gr4)
    lvl.addTile("gr", "F", imgdata.gr5)
    lvl.addTile("gr", "DLT", imgdata.gr6)
    lvl.addTile("gr", "TD", imgdata.gr7)
    lvl.addTile("gr", "TR", imgdata.gr8)
    lvl.addTile("gr", "RTL", imgdata.gr9)
    lvl.addTile("gr", "TL", imgdata.gr10)
    lvl.addTile("gr", "T", imgdata.gr11)
    lvl.addTile("gr", "R", imgdata.gr12)
    lvl.addTile("gr", "LR", imgdata.gr13)
    lvl.addTile("gr", "L", imgdata.gr14)
    lvl.addTile("gr", "E", imgdata.gr15)
    lvl.addTile("gr", "ITL", imgdata.gr16)
    lvl.addTile("gr", "ITR", imgdata.gr17)
    lvl.addTile("gr", "IDL", imgdata.gr18)
    lvl.addTile("gr", "IDR", imgdata.gr19)

    lvl.addType("btn", (255, 0, 0), imgdata.btn0, 1)

    lvl.addTile("btn", "DLT", imgdata.btn0, [36, 12, 12, 24])
    lvl.addTile("btn", "TL", imgdata.btn0, [36, 12, 12, 24])
    lvl.addTile("btn", "DL", imgdata.btn0, [36, 12, 12, 24])
    lvl.addTile("btn", "L", imgdata.btn0, [36, 12, 12, 24])
    
    lvl.addTile("btn", "TRD", imgdata.btn1, [0, 12, 12, 24])
    lvl.addTile("btn", "TR", imgdata.btn1, [0, 12, 12, 24])
    lvl.addTile("btn", "DR", imgdata.btn1, [0, 12, 12, 24])
    lvl.addTile("btn", "R", imgdata.btn1, [0, 12, 12, 24])

    lvl.addType("spkt", (240, 240, 240), imgdata.spk3, 1, [1, 0, 46, 1], "kill")
    lvl.addType("spkd", (225, 225, 225), imgdata.spk2, 1, [1, 47, 46, 1], "kill")
    lvl.addType("spkl", (210, 210, 210), imgdata.spk1, 1, [0, 1, 1, 47], "kill")
    lvl.addType("spkr", (195, 195, 195), imgdata.spk0, 1, [52, 1, 1, 47], "kill")

    lvl.addType("dr", (255, 255, 0), imgdata.dr, 1, tag = "dr")
    
    lvl.addType("drtri", (255, 0, 255), imgdata.drtri, 1, tag = "drtri")
    lvl.addType("drsqr", (0, 255, 0), imgdata.drsqr, 1, tag = "drsqr")
    lvl.addType("drcir", (0, 0, 255), imgdata.drcir, 1, tag = "drcir")

    lvl.addType("pt", (0, 255, 255), imgdata.pt, 1, tag = "pt")

    lvl.write()

    return lvl

lvl1 = create_lvl(pygame.image.load("Assets/Maps/Lvl1.png"))

lvl1.add_btn((9, 2), [[5, 0, "normal"], [6, 0, "normal"], [7, 0, "normal"],   [0, 9, "dr"], [0, 10, "dr"], [0, 11, "dr"], [0, 12, "dr"]])

lvl2 = create_lvl(pygame.image.load("Assets/Maps/Lvl2.png"))

lvl2.add_btn((6, 8), [[14, 3, "dr"], [14, 4, "dr"], [14, 5, "dr"], [14, 6, "dr"]])
lvl2.add_btn((9, 5), [[15, 3, "dr"], [15, 4, "dr"], [15, 5, "dr"], [15, 6, "dr"], [6, 1, "dr"]])

