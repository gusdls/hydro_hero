import pygame
from random import random

from settings import *
from support import *

from camera import CenterCameraGroup
from interface import UI

from sprites.player import Player
from sprites.tile import StaticTile, WaterDrop
from sprites.enemy import Enemy

class GameManager:
    def __init__(self):
        self.visible_group = CenterCameraGroup()
        self.interface = UI()

        terrain_layout = import_csv_layout("layouts/ground.csv")
        self.create_tile_group(terrain_layout, 'terrain')
        self.water_group = self.create_tile_group(terrain_layout, 'water')

        objects_layout = import_csv_layout("layouts/objects.csv")
        self.create_tile_group(objects_layout, 'objects')
    
    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_idx, row in enumerate(layout):
            for col_idx, value in enumerate(row):
                if value == '-1':
                    continue

                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE

                if type == 'terrain':
                    sprite = StaticTile(x, y)
                    self.visible_group.add(sprite)
                    sprite_group.add(sprite)
                elif type == 'water':
                    if random() < 0.01:
                        sprite = WaterDrop(x, y)
                        self.visible_group.add(sprite)
                        sprite_group.add(sprite)
                elif type == 'objects':
                    if value == '0':
                        self.player = Player(size=(120, 120), position=(x, y))
                        self.visible_group.add(self.player)
                    else:
                        sprite = Enemy(
                            position=(x, y),
                            name=enemies_data[value]['name'],
                            size=enemies_data[value]['size'],
                            speed=enemies_data[value]['speed'],
                            notice_radius=enemies_data[value]['notice_radius']
                        )
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
        self.visible_group.enemy_update(self.player)
        self.visible_group.draw(self.player)
        self.interface.display(self.player)