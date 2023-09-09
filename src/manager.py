import pygame

from settings import *
from support import *
from camera import BoxCameraGroup
from sprites.player import Player
from sprites.tile import Tile

class GameManager:
    def __init__(self):
        self.visible_group = BoxCameraGroup()

        terrain_layout = import_csv_layout("layouts/ground.csv")
        terrain_group = self.create_tile_group(terrain_layout)

        self.player = Player(size=(150, 150), position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.visible_group.add(self.player)
    
    def create_tile_group(self, layout):
        sprite_group = pygame.sprite.Group()

        for row_idx, row in enumerate(layout):
            for col_idx, value in enumerate(row):
                if value != '-1':
                    sprite = Tile(col_idx * TILE_SIZE, row_idx * TILE_SIZE)
                    self.visible_group.add(sprite)
                    sprite_group.add(sprite)
        
        return sprite_group
    
    def run(self):
        self.visible_group.update()
        self.visible_group.draw(self.player)