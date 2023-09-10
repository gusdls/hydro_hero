import pygame
import os

from support import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, size, position, speed, notice_radius):
        super().__init__()
        self.name = name
        self.speed = speed
        self.notice_radius = notice_radius

        self.animations = {'idle': [], 'move': []}
        for animation in self.animations.keys():
            self.import_assets(animation, size)

        self.frame_index = 0
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=position)
        self.update_time = pygame.time.get_ticks()
        self.facing_right = False

        self.direction = pygame.math.Vector2()

    def import_assets(self, animation, size):
        path = os.path.join('assets', self.name, animation)
        images = import_folder(path)
        for image in images:
            self.animations[animation].append(pygame.transform.scale(image, size))

    def animate(self):
        one_second = 1000
        if pygame.time.get_ticks() - self.update_time >= one_second / len(self.animations[self.status]):
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()

        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.image = pygame.transform.flip(self.image, self.facing_right, False)

    def get_geometric(self, player):
        player_pos = pygame.math.Vector2(player.rect.center)
        enemy_pos = pygame.math.Vector2(self.rect.center)
        distance = (player_pos - enemy_pos).magnitude()
        
        if distance > 0:
            direction = (player_pos - enemy_pos).normalize()
        else:
            direction = pygame.math.Vector2()

        return distance, direction

    def get_status(self, distance):
        if distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self, direction):
        if self.status == 'move':
            self.direction = direction
        else:
            self.direction = pygame.math.Vector2()

        if self.direction.x < 0:
            self.facing_right = False
        elif self.direction.x > 0:
            self.facing_right = True

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * self.speed

    def update(self):
        self.animate()
        self.move()

    def custom_update(self, player):
        distance, direction = self.get_geometric(player)
        self.get_status(distance)
        self.actions(direction)