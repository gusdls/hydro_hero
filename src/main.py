import pygame
import sys

from settings import *
from sprites.camera import CenterCameraGroup
from sprites.player import Player

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("The Flumen")
        self.clock = pygame.time.Clock()
        self.visible_group = CenterCameraGroup()

    def init_sprites(self):
        self.player = Player(size=(150, 150), position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.visible_group.add(self.player)

    def draw_window(self):
        self.screen.fill(BLACK)
        self.visible_group.update()
        self.visible_group.draw(self.player)
        pygame.display.update()

    def run(self):
        self.init_sprites()
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.draw_window()

if __name__ == "__main__":
    game = Game()
    game.run()