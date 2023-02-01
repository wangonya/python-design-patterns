import pygame


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        raise NotImplementedError()

    def move(self, direction):
        if direction == "up":
            self.y -= 4
        elif direction == "down":
            self.y += 4
        elif direction == "left":
            self.x -= 4
        elif direction == "right":
            self.x += 4

    @staticmethod
    def factory(type):
        if type == "Circle":
            return Circle(100, 100)
        if type == "Square":
            return Square(100, 100)

        assert 0, f"Bad shape requested: {type}"


class Square(Shape):
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(self.x, self.y, 20, 20))


class Circle(Shape):
    def draw(self):
        pygame.draw.rect(screen, (0, 255, 255), (self.x, self.y), 10)


if __name__ == "__main__":
    window_dimensions = 800, 600
    screen = pygame.display.set_mode(window_dimensions)

    obj = Shape.factory("Square")
    player_quits = False

    while not player_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                obj.move("up")
            if pressed[pygame.K_DOWN]:
                obj.move("down")
            if pressed[pygame.K_LEFT]:
                obj.move("left")
            if pressed[pygame.K_RIGHT]:
                obj.move("right")

            screen.fill((0, 0, 0))
            obj.draw()
        pygame.display.flip()
