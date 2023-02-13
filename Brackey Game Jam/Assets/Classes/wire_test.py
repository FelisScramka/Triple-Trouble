import pygame
import math

class Wire:
    def __init__(self, startpoint, endpoint, segments = 24):
        if startpoint[0] > endpoint[0]:
            self.startpoint = [startpoint[0], startpoint[1]]
            self.endpoint = [endpoint[0], endpoint[1]]
        else:
            print("startpoint is not greater than endpoint")
            self.startpoint, self.endpoint = [startpoint[0], startpoint[1]], [endpoint[0], endpoint[1]]
        self.num_segments = segments
        self.points = [self.startpoint]
        self.width = endpoint[0] - startpoint[0]
        self.height = startpoint[1]
        print(self.width)
        for index in range(self.num_segments):
            width_per_segment = self.width / self.num_segments
            x = self.startpoint[0] + width_per_segment * index
            y = self.height
            self.points.append([x, y])
        print(width_per_segment)
        self.points.append(self.endpoint)
        print(self.points)
    
    def draw(self, screen):
        pygame.draw.lines(screen, "black", False, self.points, 1)

    def update(self):
        mid_index = len(self.points) // 2
        index = 0
        for point_x, point_y in self.points:
            startpoint_distance = abs(self.startpoint[0] - point_x)
            endpoint_distance = abs(self.endpoint[0] - point_x)
            distance = min(startpoint_distance, endpoint_distance)

            dist_to_mid = abs(self.points[mid_index][0] - point_x)
            val2 = dist_to_mid**1

            if index == mid_index:
                val2 = abs(self.points[mid_index][0] - self.points[mid_index-1][0] )

            val = 100 * (1 +(distance /(self.width / 2)))
            self.points[index][1] = val - val2
            # try messing aroung with the **(102/100) to get a different curve

            index += 1


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.fps = 60
        self.wire = Wire((100, 100), (700, 100))
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        self.wire.update()
    
    def draw(self):
        self.screen.fill("white")
        self.wire.draw(self.screen)

    def run(self):
        while self.running:
            self.dt = self.clock.tick(self.fps)
            self.events()
            self.update()
            self.draw()
            pygame.display.update()


if __name__ == "__main__":
    app = App()
    app.run()
