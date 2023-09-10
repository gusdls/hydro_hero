from csv import reader
import pygame
import os

from settings import *

def import_csv_layout(path):
    with open(path) as file:
        return [map(int, row) for row in reader(file, delimiter=',')]
    
def import_folder(path, priority=lambda file: file):
    images = []
    for root, dirs, files in os.walk(path):
        for file in sorted(files, key=priority):
            location = os.path.join(root, file)
            images.append(pygame.image.load(location).convert_alpha())
    
    return images

def import_cut_graphics(path):
    target = pygame.image.load(path).convert_alpha()
    width, height = target.get_size()

    graphics = []
    for y in range(0, height, TILESIZE):
        for x in range(0, width, TILESIZE):
            new_graphic = pygame.Surface((TILESIZE, TILESIZE), flags=pygame.SRCALPHA)
            new_graphic.blit(target, (0, 0), pygame.Rect(x, y, TILESIZE, TILESIZE))
            graphics.append(new_graphic)

    return graphics