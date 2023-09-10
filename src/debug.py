import pygame

from settings import *

def debug(text):
    screen = pygame.display.get_surface()
    font = pygame.font.Font("assets/ThaleahFat.ttf", 32)

    render_surf = font.render(text, False, TEXT_COLOR)
    render_rect = render_surf.get_rect(topright=(SCREEN_WIDTH - 20, 20))
    pygame.draw.rect(screen, BG_COLOR, render_rect.inflate(20, 20))
    screen.blit(render_surf, render_rect)
    pygame.draw.rect(screen, BORDER_COLOR, render_rect.inflate(20, 20), 3)