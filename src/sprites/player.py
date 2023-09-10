import pygame
import os

from settings import *
from support import *
from debug import debug

class Player(pygame.sprite.Sprite):
    def __init__(self, size, position):
        super().__init__()
        self.animations = {'idle': [], 'run': [], 'attack': []}
        self.animation_times = {'idle': 2000, 'run': 1000, 'attack': 1000}
        for animation in self.animations.keys():
            self.import_assets(animation, size)

        self.frame_index = 0
        self.status = 'idle'
        self.update_time = pygame.time.get_ticks()
        self.facing_right = True
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=position)

        self.direction = pygame.math.Vector2()
        self.speed = 10
        self.jump_speed = -15
        self.gravity = 0.8
        self.on_ground = False

        self.attacking = False
        self.attack_time = None
        
    def import_assets(self, animation, size):
        path = os.path.join('assets', 'bandit', animation)
        images = import_folder(path)
        for image in images:
            self.animations[animation].append(pygame.transform.scale(image, size))
        
    def animate(self):
        frame_time = self.animation_times[self.status] / len(self.animations[self.status])
        if pygame.time.get_ticks() - self.update_time >= frame_time:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.image = pygame.transform.flip(self.image, self.facing_right, False)
        
    def get_status(self):
        if self.attacking:
            self.status = 'attack'
        elif self.direction.x != 0:
            self.status = 'run'
        else:
            self.status = 'idle'

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.attacking:
            if keys[pygame.K_a]:
                self.direction.x = -1
                self.facing_right = False
            elif keys[pygame.K_d]:
                self.direction.x = 1
                self.facing_right = True
            else:
                self.direction.x = 0

            if keys[pygame.K_SPACE] and self.on_ground:
                self.jump()

            if keys[pygame.K_LSHIFT]:
                self.attack()

    def move(self):
        self.rect.x += self.direction.x * self.speed

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        self.on_ground = False

    def attack(self):
        self.attacking = True
        self.attack_time = pygame.time.get_ticks()
        self.frame_index = 0
        self.direction = pygame.math.Vector2()

    def cooldowns(self):
        if self.attacking and pygame.time.get_ticks() - self.attack_time >= self.animation_times[self.status]:
            self.attacking = False

    def collect_water(self):
        if self.water < self.capacity:
            self.water += 1

    def update(self):
        debug(str(self.rect.center))

        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()