import pygame
import os

from settings import *
from support import *
from interface import UI
from sprites import *

class GameWorld:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.visible_group = CenterCameraGroup()

        terrain_layout = import_csv_layout("layouts/terrain.csv")
        self.create_tile_group(terrain_layout, "terrain")

        ground_layout = import_csv_layout("layouts/ground.csv")
        self.ground_group = self.create_tile_group(ground_layout, "ground")

        self.player = Player(0, 968)
        self.visible_group.add(self.player)

        self.interface = UI()

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        ground_tiles = import_cut_graphics("assets/tilemap/ground.png")
        terrain_tiles = import_folder(os.path.join("assets", "terrain"), lambda file: int(os.path.splitext(file)[0]))

        for row_idx, row in enumerate(layout):
            for col_idx, val in enumerate(row):
                if val == -1:
                    continue

                x = col_idx * TILESIZE
                y = row_idx * TILESIZE
                    
                if type == "ground":
                    sprite = StaticTile(ground_tiles[val], x, y)
                    self.visible_group.add(sprite)
                    sprite_group.add(sprite)
                elif type == "terrain":
                    sprite = TerrainTile(terrain_tiles[val], x, y + TILESIZE)
                    self.visible_group.add(sprite)
                    sprite_group.add(sprite)

        return sprite_group

    def horizontal_collision(self):
        self.player.move()
        for sprite in self.ground_group.sprites():
            if sprite.rect.colliderect(self.player.hitbox):
                if self.player.direction.x < 0:
                    self.player.hitbox.left = sprite.rect.right
                elif self.player.direction.x > 0:
                    self.player.hitbox.right = sprite.rect.left
    
    def vertical_collision(self):
        self.player.apply_gravity()
        for sprite in self.ground_group.sprites():
            if sprite.rect.colliderect(self.player.hitbox):
                if self.player.direction.y < 0:
                    self.player.hitbox.top = sprite.rect.bottom
                    self.player.direction.y = 0
                elif self.player.direction.y > 0:
                    self.player.hitbox.bottom = sprite.rect.top
                    self.player.direction.y = 0
                    self.player.on_ground = True

    def run(self):
        self.horizontal_collision()
        self.vertical_collision()
        self.visible_group.update()
        self.visible_group.draw(self.player)
        self.interface.display(self.player)