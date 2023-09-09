import pygame
from random import random

from settings import *
from support import *

from camera import BoxCameraGroup
from interface import UI

from sprites.player import Player
from sprites.tile import StaticTile, WaterDrop

class GameManager:
    def __init__(self):
        self.visible_group = BoxCameraGroup()
        self.interface = UI()

        terrain_layout = import_csv_layout("layouts/ground.csv")
        terrain_group = self.create_tile_group(terrain_layout, StaticTile)
        self.water_group = self.create_tile_group(terrain_layout, WaterDrop, lambda: random() < 0.01)

        self.player = Player(size=(150, 150), position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.visible_group.add(self.player)
    
    def create_tile_group(self, layout, Tile, check=lambda: True):
        sprite_group = pygame.sprite.Group()

        for row_idx, row in enumerate(layout):
            for col_idx, value in enumerate(row):
                if value != '-1' and check():
                    sprite = Tile(col_idx * TILE_SIZE, row_idx * TILE_SIZE)
                    self.visible_group.add(sprite)
                    sprite_group.add(sprite)
        
        return sprite_group
    
    def collision_items(self):
        for sprite in self.water_group.sprites():
            if sprite.rect.colliderect(self.player.rect):
                self.player.collect_water()
                sprite.kill()
    
    def run(self):
        self.collision_items()
        self.visible_group.update()
        self.visible_group.draw(self.player)
        self.interface.display(self.player)