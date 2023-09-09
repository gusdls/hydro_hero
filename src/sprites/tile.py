import pygame

from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))

class StaticTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill(GRAY)

class WaterDrop(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill(BLUE)