# For parameter type hinting only
from __future__ import annotations
from pytmx.pytmx import TiledTileLayer

from layer import Layer

class Blocks(Layer):
    def __init__(self, game: Game, layer: TiledTileLayer):
        super().__init__(game=game, layer=layer)
