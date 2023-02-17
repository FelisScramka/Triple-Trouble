import pygame

tile_sz = (48, 48)

sqr_idle_1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Square1.png"), tile_sz)
sqr_idle_2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Square2.png"), tile_sz)
sqr_idle_3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Square3.png"), tile_sz)
sqr_idle_4 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Square4.png"), tile_sz)

sqr_run_1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/SquareRun1.png"), tile_sz)
sqr_run_2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/SquareRun2.png"), tile_sz)

tri_idle_1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Triangle1.png"), tile_sz)
tri_idle_2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Triangle2.png"), tile_sz)
tri_idle_3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Triangle3.png"), tile_sz)
tri_idle_4 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Triangle4.png"), tile_sz)

tri_run_1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/TriangleRun1.png"), tile_sz)
tri_run_2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/TriangleRun2.png"), tile_sz)

cir_idle_1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Sphere1.png"), tile_sz)
cir_idle_2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Sphere2.png"), tile_sz)
cir_idle_3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Sphere3.png"), tile_sz)
cir_idle_4 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/Sphere4.png"), tile_sz)

cir_run_1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/SphereRun1.png"), tile_sz)
cir_run_2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Player/SphereRun2.png"), tile_sz)

idle_sqr_frames = []

for i in range(10):
    idle_sqr_frames.append(sqr_idle_1)
for i in range(10):
    idle_sqr_frames.append(sqr_idle_2)
for i in range(10):
    idle_sqr_frames.append(sqr_idle_3)
for i in range(10):
    idle_sqr_frames.append(sqr_idle_4)

run_sqr_frames = []

for i in range(8):
    run_sqr_frames.append(sqr_run_1)
for i in range(8):
    run_sqr_frames.append(sqr_run_2)

idle_tri_frames = []

for i in range(10):
    idle_tri_frames.append(tri_idle_1)
for i in range(10):
    idle_tri_frames.append(tri_idle_2)
for i in range(10):
    idle_tri_frames.append(tri_idle_3)
for i in range(10):
    idle_tri_frames.append(tri_idle_4)

run_tri_frames = []

for i in range(8):
    run_tri_frames.append(tri_run_1)
for i in range(8):
    run_tri_frames.append(tri_run_2)

idle_cir_frames = []

for i in range(10):
    idle_cir_frames.append(cir_idle_1)
for i in range(10):
    idle_cir_frames.append(cir_idle_2)
for i in range(10):
    idle_cir_frames.append(cir_idle_3)
for i in range(10):
    idle_cir_frames.append(cir_idle_4)

run_cir_frames = []

for i in range(8):
    run_cir_frames.append(cir_run_1)
for i in range(8):
    run_cir_frames.append(cir_run_2)

gr0 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/0.png"), tile_sz)
gr1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/1.png"), tile_sz)
gr2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/2.png"), tile_sz)
gr3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/3.png"), tile_sz)
gr4 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/4.png"), tile_sz)
gr5 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/5.png"), tile_sz)
gr6 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/6.png"), tile_sz)
gr7 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/7.png"), tile_sz)
gr8 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/8.png"), tile_sz)
gr9 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/9.png"), tile_sz)
gr10 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/10.png"), tile_sz)
gr11 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/11.png"), tile_sz)
gr12 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/12.png"), tile_sz)
gr13 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/13.png"), tile_sz)
gr14 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/14.png"), tile_sz)
gr15 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/15.png"), tile_sz)
gr16 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/16.png"), tile_sz)
gr17 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/17.png"), tile_sz)
gr18 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/18.png"), tile_sz)
gr19 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Gr/19.png"), tile_sz)

btn0 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Btn/0.png"), tile_sz)
btn1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Btn/1.png"), tile_sz)

spk0 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Spk/0.png"), tile_sz)
spk1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Spk/1.png"), tile_sz)
spk2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Spk/2.png"), tile_sz)
spk3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Spk/3.png"), tile_sz)

dr = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Dr/0.png"), tile_sz)
drsqr = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Dr/1.png"), tile_sz)
drcir = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Dr/2.png"), tile_sz)
drtri = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Dr/3.png"), tile_sz)

pt = pygame.transform.scale(pygame.image.load("Assets/Sprites/Tiles/Pt/0.png"), tile_sz)
