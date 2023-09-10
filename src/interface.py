import pygame

from settings import *

class UI:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.water_bar = pygame.Rect(10, 10, 200, 20)
        self.health_bar = pygame.Rect(10, 34, 120, 20)

    def show_status_bar(self, current, maximum, rect, color):
        pygame.draw.rect(self.screen, BG_COLOR, rect)

        current_rect = rect.copy()
        ratio = current / maximum
        current_rect.width = rect.width * ratio
        pygame.draw.rect(self.screen, color, current_rect)

        pygame.draw.rect(self.screen, BORDER_COLOR, rect, 3)

    def display(self, player):
        self.show_status_bar(current=player.water_amount, maximum=player.water_capacity, rect=self.water_bar, color=WATER_COLOR)
        self.show_status_bar(current=player.health, maximum=player.max_health, rect=self.health_bar, color=HEALTH_COLOR)
