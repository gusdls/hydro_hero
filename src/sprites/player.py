import pygame
import glob

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, size, position):
        super().__init__()
        ANIMATIONS = ['idle', 'run']
        ANIMATION_TIMES = [2000, 1000]
        
        self.animations = {}
        self.animation_times = {}
        for i, status in enumerate(ANIMATIONS):
            self.import_assets(status, size)
            self.animation_times[status] = ANIMATION_TIMES[i]

        self.frame_index = 0
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=position)

        self.update_time = pygame.time.get_ticks()
        self.facing_right = True

        self.direction = pygame.math.Vector2()
        self.speed = 10
        self.jump_speed = -12
        self.gravity = 0.8
        self.on_ground = False
        
    def import_assets(self, status, size):
        files = glob.glob(f"assets/bandit/{status}*.png")
        images = [pygame.image.load(file).convert_alpha() for file in files]
        self.animations[status] = [pygame.transform.scale(image, size) for image in images]
        
    def animate(self):
        animation_cooldown = self.animation_times[self.status] / len(self.animations[self.status])
        if pygame.time.get_ticks() - self.update_time >= animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.image = pygame.transform.flip(self.image, self.facing_right, False)
        
    def get_status(self):
        if self.direction.x != 0:
            self.status = 'run'
        else:
            self.status = 'idle'

    def input(self):
        keys = pygame.key.get_pressed()

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

    def move(self):
        self.rect.x += self.direction.x * self.speed

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.on_ground = True

    def jump(self):
        self.direction.y = self.jump_speed
        self.on_ground = False

    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.apply_gravity()
        self.move()