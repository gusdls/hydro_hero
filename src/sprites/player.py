import pygame
import os

from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = {'idle': [], 'run': [], 'attack': []}
        self.animation_duration = {'idle': 2000, 'run': 1000, 'attack': 1000}
        for animation in self.animations.keys():
            self.import_assets(animation, size=(120, 120))

        self.frame_index = 0
        self.status = 'idle'
        self.update_time = pygame.time.get_ticks()
        self.facing_right = True
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hitbox = self.rect.inflate(-70, -20)

        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.jump_speed = -15
        self.gravity = 0.8
        self.on_ground = False

        self.attacking = False
        self.attack_time = None

        self.capacity = 30
        self.water = 0
        
    def import_assets(self, animation, size):
        path = os.path.join("assets", "bandit", animation)
        images = import_folder(path)
        for image in images:
            self.animations[animation].append(pygame.transform.scale(image, size))
        
    def animate(self):
        duration = self.animation_duration[self.status] / len(self.animations[self.status])
        if pygame.time.get_ticks() - self.update_time >= duration:
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
        self.hitbox.x += self.direction.x * self.speed
        self.rect.midbottom = self.hitbox.midbottom

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.hitbox.y += self.direction.y
        self.rect.midbottom = self.hitbox.midbottom

    def jump(self):
        self.direction.y = self.jump_speed
        self.on_ground = False

    def attack(self):
        self.attacking = True
        self.attack_time = pygame.time.get_ticks()
        self.frame_index = 0
        self.direction = pygame.math.Vector2()

    def cooldowns(self):
        if self.attacking:
            if pygame.time.get_ticks() - self.attack_time >= self.animation_duration[self.status]:
                self.attacking = False

    def collect_water(self):
        if self.water < self.capacity:
            self.water += 1

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()