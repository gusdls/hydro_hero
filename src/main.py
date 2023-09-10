import pygame
import sys

from settings import *
from world import GameWorld

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("The Flumen")
        self.clock = pygame.time.Clock()
        self.world = GameWorld()
        
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

            self.screen.fill(SKY)
            self.world.run()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()