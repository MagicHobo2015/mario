from __future__ import annotations
import pygame as pg
from vector import Vector

class Goomba(pg.sprite.Sprite):
    def __init__(self, game: Game) -> None:
        super().__init__()
        self.game = game
        # For now, draw a rectangle to represent the mario
        self.image = pg.Surface((32, 32))
        self.image.fill(pg.Color("red"))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 100

        # Player movement
        self.direction = Vector()
        self.speed = 4
        self.gravity = 3
        
    def get_key_input(self, keys: pg.key.get_pressed) -> None:
        # Get the direction of the player
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction.x = -1
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction.x = 1
        elif keys[pg.K_SPACE]:
            self.direction.y = -1
        else:
            self.direction = Vector()

    def apply_gravity(self) -> None:
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self) -> None:
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed + self.gravity
        ground_collisions = self.game.ground.check_collisions(self)
        if ground_collisions:
            for tile in ground_collisions:
                # if tile is to the left/right of a pipe
                if self.direction.x > 0:
                    self.rect.right = tile.left
                elif self.direction.x < 0:
                    self.rect.left = tile.right
                
                # if tile is above/below a pipe
                if self.direction.y > 0:
                    self.rect.bottom = tile.top
                    self.direction.y = 0
                elif self.direction.y < 0:
                    self.rect.top = tile.bottom
                    self.direction.y = 0
        # self.apply_gravity()

        self.draw()

    def draw(self) -> None:
        self.game.screen.blit(self.image, self.rect)