# For parameter type hinting only
from __future__ import annotations
from pytmx.pytmx import TiledTileLayer

import pygame as pg
from vector import Vector

class Blocks(pg.sprite.Sprite):
    def __init__(self, game: Game, layer: TiledTileLayer):
        super().__init__()
