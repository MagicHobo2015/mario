# For parameter type hinting only
from __future__ import annotations
from pytmx.pytmx import TiledTileLayer

import pygame as pg


class Grass(pg.sprite.Sprite):
    def __init__(self, game: Game, layer: TiledTileLayer):
        super().__init__()
        self.game = game
        self.tile_size = game.settings.tile_size
        self.layer = layer
        print(self.layer)

        for x, y, sprite in self.layer.tiles():
            print(f"{x, y, sprite}")

    def update(self):
        self.draw()

    def draw(self):
        for x, y, sprite in self.layer.tiles():
            self.game.screen.blit(sprite, (x * self.tile_size, y * self.tile_size))