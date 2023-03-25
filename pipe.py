# For parameter type hinting only
from __future__ import annotations
from pytmx.pytmx import TiledTileLayer

import pygame as pg
from vector import Vector

class Pipes(pg.sprite.Sprite):
    def __init__(self, game: Game, layer: TiledTileLayer):
        super().__init__()
        self.game = game
        self.tile_size = game.settings.tile_size
        self.layer = layer
        self.layer_vel = Vector()
        print(self.layer)

        for x, y, sprite in self.layer.tiles():
            print(f"{x, y, sprite}")

    def update(self):
        self.layer.offsetx += self.layer_vel.x
        # The y offset should not change (map is only moving left or right)
        self.layer.offsety = 0
        self.draw()

    def draw(self):
        # Draws all the tiles in the layer object based on the x and y coordinates
        # Also adds the offset to the x and y coordinates (from moving left or right)
        for x, y, sprite in self.layer.tiles():
            self.game.screen.blit(sprite, 
                                  (x * self.tile_size + self.layer.offsetx, 
                                   y * self.tile_size + self.layer.offsety)
                                )