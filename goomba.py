from __future__ import annotations
import pygame as pg
from vector import Vector

# This is supposed to be the code for Mario eventually with working collisions and not Goomba
# But it doesn't work so I'm just going to leave it as Goomba for now
class Goomba(pg.sprite.Sprite):
    def __init__(self, game: Game) -> None:
        super().__init__()
        self.game = game
        # For now, draw a rectangle to represent the goomba
        self.image = pg.Surface((32, 32))
        self.image.fill(pg.Color("red"))

        # Dimensions of the block (should be 32x32 for now)
        self.rect = self.image.get_rect()

        # Initial position
        self.rect.x = 800
        self.rect.y = 50

        # Player movement
        self.direction = Vector()
        self.speed = 4
        self.gravity = 0.5
        self.jump_speed = 30
        
    def get_key_input(self, keys: pg.key.get_pressed) -> None:
        # Get the direction of the player
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction.x = -1
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction.x = 1
        elif keys[pg.K_SPACE]:
            self.direction.y = -self.jump_speed
            self.game.sound.play_sound("mario_jump_small")
        else:
            self.direction = Vector()

    def apply_gravity(self) -> None:
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def handle_collisions(self):
        ground_collisions = self.game.ground.check_collisions(self)
        if ground_collisions:
            for tile in ground_collisions:
                # if goomba is to the left/right of a block
                if self.direction.x > 0:
                    self.rect.right = tile.left
                if self.direction.x < 0:
                    self.rect.left = tile.right
                

        if ground_collisions:
            for tile in ground_collisions:
                # if goomba is above/below a block
                if self.direction.y > 0:
                    self.rect.bottom = tile.top
                    self.direction.y = 0
                if self.direction.y < 0:
                    self.rect.top = tile.bottom
                    self.direction.y = 0

    def update(self) -> None:
        self.rect.x += self.direction.x * self.speed
        self.apply_gravity()
        # self.handle_collisions()
        self.draw()

    def draw(self) -> None:
        self.game.screen.blit(self.image, self.rect)