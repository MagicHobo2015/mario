# For parameter type hinting only
from __future__ import annotations
from pytmx.pytmx import TiledTileLayer

import pygame as pg
from vector import Vector

class Layer():
    """Base Class for all pytmx layers to inherit from"""
    def __init__(self, game: Game, layer: TiledTileLayer):
        super().__init__()
        self.game = game
        self.tile_size = game.settings.tile_size
        self.layer = layer
        self.layer_vel = Vector()

        print(f"{self.layer} loaded")

    def check_collisions(self, sprite: pg.sprite.Sprite):
        # Check for collisions with all tiles in the layer
        for x, y, tile in self.layer.tiles():
            # get_clip() returns a pg.Rect object
            tile_rect = tile.get_clip()
            tile_rect.x = x * self.tile_size + self.layer.offsetx
            tile_rect.y = y * self.tile_size + self.layer.offsety
            if sprite.rect.colliderect(tile_rect):
                print(f"Collision at {x=} {y=} in layer {self.layer.name}")
                return [x, y, self.layer.name]

                


    def update(self):
        self.layer.offsetx += self.layer_vel.x
        # The y offset should not change (map is only moving left or right)
        self.layer.offsety = 0
        self.draw()

    def draw(self):
        # Draws all the tiles in the layer object based on the x and y coordinates
        # Also adds the offset to the x and y coordinates (from moving left or right)
        for x, y, sprite in self.layer.tiles():
            self.game.screen.blit(sprite, (x * self.tile_size + self.layer.offsetx, y * self.tile_size + self.layer.offsety))