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
                   "still_right": [6], "still_left": [7], "scale": 3}
    
    large_mario = {"offsetx": 30, "offsety" : 52, "sizex": 17, "sizey": 35,
                   "left": [3, 4, 5], "right": [10, 9, 8],
                   "still_right": [7], "still_left": [6], "squatting_right": [13],
                   "squatting_left": [0], "jump_right": [12], "jump_left": [1], "scale": 5}
    
    
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.lives = self.settings.mario_lives
        self.dying = False
        self.running = False
        self.marios_direction = "right"
        self.marios_action = "still_right" # begining state
        
        # this is where marios first postition is set
        self.v = Vector()
        self.posn = self.v
        
        #self.mario_images = self.setup_small_mario()
        self.mario_images = self.setup_large_mario()
        self.images = self.mario_images[self.marios_action]
        self.rect = self.images[0].get_rect()
        self.rect.y = self.screen.get_height() - self.rect.height * 2
        self.posn.y = self.rect.y
        self.x = float(self.rect.x)
        self.posn.x = self.x
        self.timer = Timer(self.images, 0, delay=50, is_loop=True)
        
        # leave this for now
    def setup_small_mario(self):
            offsetx = self.small_mario["offsetx"]
            offsety = self.small_mario["offsety"]
            sizex = self.small_mario["sizex"]
            sizey = self.small_mario["sizey"]
            
            # this is how much to stretch the image from the sheet
            scale = self.small_mario["scale"]
            
            image_sheet = SpriteSheet('assets/characters/mario/mario.png')
            
            left_images = [image_sheet.get_image(offsetx * slot,
                                                           offsety, sizex, sizey, scale)
                                for slot in self.small_mario["left"]]
            
            right_images = [image_sheet.get_image(offsetx * slot, offsety,
                                                            sizex, sizey, scale)
                                 for slot in self.small_mario["right"]]
            
            still_left = [image_sheet.get_image(offsetx * slot,
                                                          offsety, sizex, sizey, scale)
                               for slot in self.small_mario["still_left"]]
            
            still_right = [image_sheet.get_image(offsetx * slot, offsety, sizex, sizey, scale)
                                for slot in self.small_mario["still_right"]]
            
            return {"left": left_images, "right": right_images,
                                "still_left": still_left, "still_right": still_right}
            
    def setup_large_mario(self):
            offsetx = self.large_mario["offsetx"]
            offsety = self.large_mario["offsety"]
            sizex = self.large_mario["sizex"]
            sizey = self.large_mario["sizey"]
            
            # this is how much to stretch the image from the sheet
            scale = self.large_mario["scale"]
            
            image_sheet = SpriteSheet('assets/characters/mario/mario.png')
            
            left_images = [image_sheet.get_image(offsetx * slot,
                                                           offsety, sizex, sizey, scale)
                                for slot in self.large_mario["left"]]
            
            right_images = [image_sheet.get_image(offsetx * slot, offsety,
                                                            sizex, sizey, scale)
                                 for slot in self.large_mario["right"]]
            
            still_left = [image_sheet.get_image(offsetx * slot,
                                                          offsety, sizex, sizey, scale)
                               for slot in self.large_mario["still_left"]]
            
            still_right = [image_sheet.get_image(offsetx  * slot, offsety, sizex, sizey, scale)
                                for slot in self.large_mario["still_right"]]
            
            jump_right = [image_sheet.get_image(offsetx * slot, offsety, sizex, sizey, scale)
                                for slot in self.large_mario["jump_right"]]
            
            jump_left = [image_sheet.get_image(offsetx * slot, offsety, sizex, sizey, scale)
                                for slot in self.large_mario["jump_left"]]
            
            squatting_right =[image_sheet.get_image(offsetx * slot, offsety - 6, sizex, sizey, scale)
                                for slot in self.large_mario["squatting_right"]]
            
            squatting_left =[image_sheet.get_image(offsetx * slot, offsety - 6, sizex, sizey, scale)
                                for slot in self.large_mario["squatting_left"]]
            
            return {"left": left_images, "right": right_images, "still_left": still_left,
                    "still_right": still_right, "jump_right": jump_right,
                    "jump_left": jump_left, "squatting_right": squatting_right, "squatting_left": squatting_left}

    def move_mario(self, key, event_type):
        if key == pg.K_LEFT:
            self.marios_direction = "left"
        elif key == pg.K_RIGHT:
            self.marios_direction = "right"
        
    
        keys_dir = {pg.K_w: ["jump_", "still_"], pg.K_UP: ["jump_", "still_"],
            pg.K_s: ["squatting_", "still_"], pg.K_DOWN: ["squatting_", "still_"],
            pg.K_a: ["left", "still_"], pg.K_LEFT: ["left", "still_"],
            pg.K_d: ["right", "still_"],
            pg.K_RIGHT: ["right", "still_", "jump_"]}
        
        if event_type == "KEYDOWN":
            self.set_action(keys_dir[key][0])
        elif event_type == "KEYUP":
            self.set_action(keys_dir[key][1])
        
        
    def set_action(self, action):
        new_action = action
        print(action)
        if action == "squatting_":
            join_me = ["squatting_", self.marios_direction]
            new_action = ''.join(join_me)
        elif action == "still_":
           join_me = ["still_", self.marios_direction]
           new_action = ''.join(join_me)
        elif action == "jump_":
            join_me = ["jump_", self.marios_direction]
            new_action = ''.join(join_me)
            print(new_action)
           
        self.timer = Timer(self.mario_images[new_action], 0, delay=100, is_loop=True)
     
     
     
    def update(self):
        # this is where we check if he is still alive and update x and y pos.
        self.posn += self.v
        self.posn, self.rect = self.clamp( self.posn, self.rect, self.settings)
        self.draw()
    
    # this binds the vector to the image rect. if other objs need it ill put it in a class
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
        
        
