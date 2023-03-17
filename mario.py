#-----------------------------------------------------------------------------#
#Description: controls all things mario, from animation to lives			  #
#																			  #
#																			  #
#-----------------------------------------------------------------------------#
import pygame as pg
from pygame.sprite import Sprite
from timer import Timer
from vector import Vector
from spriteSheet import SpriteSheet


class Mario(Sprite):

    small_mario = {"offsetx": 30, "offsety" : 0, "sizex": 17, "sizey": 17,
                   "left": [1, 3, 4, 5], "right": [ 8, 9, 10, 12],
                   "still_right": [6], "still_left": [7]}

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.lives = self.settings.mario_lives
        self.dying = False
        self.marios_action = "still_right" # begining state

        self.offsetx = self.small_mario["offsetx"]
        self.offsety = self.small_mario["offsety"]
        self.sizex = self.small_mario["sizex"]
        self.sizey = self.small_mario["sizey"]
        
        self.v = Vector()
        self.posn = self.v
        
        self.image_sheet = SpriteSheet('assets/characters/mario/mario.png')
        
        self.left_images = [self.image_sheet.get_image(self.offsetx * slot,
                            self.offsety, self.sizex, self.sizey)
                            for slot in self.small_mario["left"]]
        
        self.right_images = [self.image_sheet.get_image(self.offsetx * slot,
                            self.offsety, self.sizex, self.sizey)
                            for slot in self.small_mario["right"]]
        
        self.still_left = [self.image_sheet.get_image(self.offsetx * slot,
                            self.offsety, self.sizex, self.sizey)
                            for slot in self.small_mario["still_left"]]
        
        self.still_right = [self.image_sheet.get_image(self.offsetx * slot,
                            self.offsety, self.sizex, self.sizey)
                            for slot in self.small_mario["still_right"]]
        
        self.small_mario_images = {"left": self.left_images, "right": self.right_images,
                                "still_left": self.still_left, "still_right": self.still_right}
        
        # END Mario images ========================================================
        self.images = self.small_mario_images[self.marios_action]
        self.rect = self.images[0].get_rect()
        self.rect.y = self.screen.get_height() - self.rect.height * 2
        self.x = float(self.rect.x)
        self.timer = Timer(self.images, 0, delay=50, is_loop=True)

    def set_action(self, action):
        self.timer = Timer(self.small_mario_images[action], 0, delay=100, is_loop=True)
     
 
    def update(self):
        # this is where we check if he is still alive and update x and y pos.
        self.posn += self.v
        self.posn, self.rect = self.clamp( self.posn, self.rect, self.settings)
        self.draw()
    
    # this binds the vector to the image rect
    def clamp(self, posn, rect, settings):
        left, top = posn.x, posn.y
        width, height = rect.width, rect.height
        left = max(0, min(left, settings.window_size[0] - width))
        top = max(0, min(top, settings.window_size[1] - height))
        return Vector(x=left, y=top), pg.Rect(left, top, width, height)
    
    
    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.centerx, rect.centery = self.rect.centerx, self.rect.centery
        self.screen.blit(image, rect)
        
        
