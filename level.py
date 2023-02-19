import pygame
import csv
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
        layout = {
            'bound': import_csv_layout('map_FloorBlocks.csv')

        }
        for style, layout in layout.items():

            for row_index, row in enumerate(WORLD_MAP):
                for col_index, col in enumerate(row):
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE


    #            if col == 'x':
    #                Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
    #        if col == 'p':
    #             self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)

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

        #creating floor
        self.floor_surface = pygame.image.load('basic.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))

    def custom_draw(self, player):
        #get the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_length

        #draw
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.disply_surface.blit(self.floor_surface, floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.disply_surface.blit(sprite.image, offset_pos)