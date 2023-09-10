import pygame
import os

from support import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, size):
        super().__init__()
        self.name = name
        self.animations = {'idle': [], 'move': []}
        for animation in self.animations.keys():
            self.import_assets(animation, size)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.frame_index = 0
        self.status = 'idle'
        self.facing_right = False
        self.update_time = pygame.time.get_ticks()

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.power = 1
        self.max_health = 3
        self.health = self.max_health

    def import_assets(self, animation, size):
        path = os.path.join("assets", self.name, animation)
        images = import_folder(path)
        for image in images:
            self.animations[animation].append(pygame.transform.scale(image, size))

    def animate(self):
        duration = 1000 / len(self.animations[self.status])
        if pygame.time.get_ticks() - self.update_time >= duration:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        
        self.image = self.animations[self.status][self.frame_index]
        self.image = pygame.transform.flip(self.image, self.facing_right, False)

    def get_status(self):
        if self.direction.x != 0:
            self.status = 'move'
        else:
            self.status = 'idle'

    def move(self, speed):
        self.rect.x += self.direction.x * speed

    def reverse(self):
        self.direction *= -1

    def update(self):
        self.get_status()
        self.animate()
        self.move(self.speed)

class Bear(Enemy):
    def __init__(self, x, y):
        super().__init__("bear", x, y, size=(TILESIZE * 4, TILESIZE * 4))

class Beetle(Enemy):
    def __init__(self, x, y):
        super().__init__("beetle", x, y, size=(TILESIZE * 3, TILESIZE * 3))

class Vulture(Enemy):
    def __init__(self, x, y):
        super().__init__("vulture", x, y, size=(TILESIZE * 3, TILESIZE * 3))