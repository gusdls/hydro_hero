import pygame
import sys

from settings import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("The Flumen")
        self.clock = pygame.time.Clock()

    def draw_window(self):
        self.screen.fill(BLACK)
        pygame.display.update()

    def run(self):
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