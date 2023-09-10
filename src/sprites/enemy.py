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