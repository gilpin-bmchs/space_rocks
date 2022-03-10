from arcade import Vector
from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_sprite

DIRECTION_UP = Vector2(0, -1)

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, position)

    def move(self):
        self.position = self.position + self.velocity

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius

class Spaceship(GameObject):
    ROTATION_SPEED = 3

    def __init__(self, position):
        super().__init__(position, load_sprite("spaceship"), Vector2(0))

    def rotate(self, clockwise = True):
        if clockwise:
            sign = 1
        else:
            sign = -1

        angle = self.ROTATION_SPEED * sign

        self.direction.rotate_ip(angle)
