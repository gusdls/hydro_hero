from csv import reader
import pygame
import os

from settings import *

def import_csv_layout(path):
    with open(path) as file:
        return [row for row in reader(file, delimiter=',')]
    
def import_folder(path, prefix=""):
    images = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith(prefix):
                location = os.path.join(root, file)
                images.append(pygame.image.load(location).convert_alpha())
    
    return images
    
def import_cut_graphics(path):
    target = pygame.image.load(path).convert_alpha()
    width, height = target.get_size()

    graphics = []
    for y in range(0, height, TILE_SIZE):
        for x in range(0, width, TILE_SIZE):
            new_graphic = pygame.Surface((TILE_SIZE, TILE_SIZE), flags=pygame.SRCALPHA)
            new_graphic.blit(target, (0, 0), pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            graphics.append(new_graphic)

    return graphics