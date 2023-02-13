import pygame

sqr_idle_1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Square1.png"), (64, 64))
sqr_idle_2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Square2.png"), (64, 64))
sqr_idle_3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Square3.png"), (64, 64))
sqr_idle_4 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Square4.png"), (64, 64))

tri_idle_1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Triangle1.png"), (64, 64))
tri_idle_2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Triangle2.png"), (64, 64))
tri_idle_3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Triangle3.png"), (64, 64))
tri_idle_4 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Triangle4.png"), (64, 64))

cir_idle_1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Sphere1.png"), (64, 64))
cir_idle_2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Sphere2.png"), (64, 64))
cir_idle_3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Sphere3.png"), (64, 64))
cir_idle_4 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Sphere4.png"), (64, 64))

idle_sqr_frames = []

for i in range(8):
    idle_sqr_frames.append(sqr_idle_1)
for i in range(8):
    idle_sqr_frames.append(sqr_idle_2)
for i in range(8):
    idle_sqr_frames.append(sqr_idle_3)
for i in range(8):
    idle_sqr_frames.append(sqr_idle_4)

idle_tri_frames = []

for i in range(8):
    idle_tri_frames.append(tri_idle_1)
for i in range(8):
    idle_tri_frames.append(tri_idle_2)
for i in range(8):
    idle_tri_frames.append(tri_idle_3)
for i in range(8):
    idle_tri_frames.append(tri_idle_4)

idle_cir_frames = []

for i in range(8):
    idle_cir_frames.append(cir_idle_1)
for i in range(8):
    idle_cir_frames.append(cir_idle_2)
for i in range(8):
    idle_cir_frames.append(cir_idle_3)
for i in range(8):
    idle_cir_frames.append(cir_idle_4)

gr0 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/0.png"), (64, 64))
gr1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/1.png"), (64, 64))
gr2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/2.png"), (64, 64))
gr3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/3.png"), (64, 64))
gr4 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/4.png"), (64, 64))
gr5 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/5.png"), (64, 64))
gr6 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/6.png"), (64, 64))
gr7 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/7.png"), (64, 64))
gr8 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/8.png"), (64, 64))
