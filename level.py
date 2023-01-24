import pygame
from setting import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        self.display_surf = pygame.display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        #sprite
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)


    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #main setup
        super().__init__()
        self.disply_surface = pygame.display.get_surface()
        self.half_width = (self.disply_surface.get_size())[0] // 2
        self.half_length = (self.disply_surface.get_size())[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        #get the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_length
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.disply_surface.blit(sprite.image, offset_pos)