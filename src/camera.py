import pygame

from sprites.enemy import Enemy

class CenterCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_w = self.screen.get_width() // 2
        self.half_h = self.screen.get_height() // 2

    def get_view(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def draw(self, player):
        self.get_view(player)
        for sprite in self.sprites():
            self.screen.blit(sprite.image, sprite.rect.topleft - self.offset)

    def enemy_update(self, player):
        for sprite in self.sprites():
            if isinstance(sprite, Enemy):
                sprite.custom_update(player)

class BoxCameraGroup(pygame.sprite.Group):
    def __init__(self, camera_border={'left': 200, 'right': 200, 'top': 100, 'bottom': 100}):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.camera_border = camera_border
        self.update_box_rect()

    def update_box_rect(self):
        left_margin = self.camera_border['left']
        top_margin = self.camera_border['top']
        width = self.screen.get_width() - left_margin - self.camera_border['right']
        height = self.screen.get_height() - top_margin - self.camera_border['bottom']
        self.box_rect = pygame.Rect(left_margin, top_margin, width, height)

    def get_view(self, target):
        if target.rect.left < self.box_rect.left:
            self.box_rect.left = target.rect.left
        elif target.rect.right > self.box_rect.right:
            self.box_rect.right = target.rect.right
        
        if target.rect.top < self.box_rect.top:
            self.box_rect.top = target.rect.top
        elif target.rect.bottom > self.box_rect.bottom:
            self.box_rect.bottom = target.rect.bottom

        self.offset.x = self.box_rect.left - self.camera_border['left']
        self.offset.y = self.box_rect.top - self.camera_border['top']

    def draw(self, player):
        self.get_view(player)
        for sprite in self.sprites():
            self.screen.blit(sprite.image, sprite.rect.topleft - self.offset)