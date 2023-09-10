import pygame

class CenterCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_w = self.screen.get_width() // 2
        self.half_h = self.screen.get_height() // 2

    def view(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def draw(self, player):
        self.view(player)
        for sprite in self.sprites():
            self.screen.blit(sprite.image, sprite.rect.topleft - self.offset)