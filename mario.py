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
                   "left": [3, 4, 5], "right": [ 8, 9, 10, 12],
                   "still_right": [7], "still_left": [6],"squatting_right": [7],
                   "squatting_left": [6], "jump_right": [12], "jump_left": [1],"scale": 3}


    large_mario = {"offsetx": 30, "offsety" : 52, "sizex": 19, "sizey": 35,
                   "left": [3, 4, 5], "right": [10, 9, 8],
                   "still_right": [6.9], "still_left": [6], "squatting_right": [13],
                   "squatting_left": [0], "jump_right": [11.9], "jump_left": [1], "scale": 2}
    
    fire_mario = {"offsetx": 25, "offsety" : 120, "sizex": 23, "sizey": 35,
                   "left": [4, 5, 6], "right": [11.4, 10.36, 9.44],
                   "still_right": [8.28], "still_left": [7], "squatting_right": [15.4],
                   "squatting_left": [0], "jump_right": [14.4], "jump_left": [1], "scale": 3}


    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.lives = self.settings.mario_lives
        self.acceleration = .001
        self.velocity = 0.0
        # delay for the animation 100 good for walking
        self.delay = 100

        # ********************************  ******  section of mario statuses
        self.running = False
        self.walking = False
        self.jumping = False
        self.dying = False

        self.marios_direction = "right"
        # begining state
        self.marios_action = "still_right" 

        # other statuses: large_mario, small_mario, fire_mario
        self.mario_status = "fire_mario"
        
        self.which_image = {"small_mario": self.setup_small_mario(), "large_mario": self.setup_large_mario(), "fire_mario": self.setup_fire_mario()}
        self.mario_images = self.which_image[self.mario_status]
        # self.mario_images = self.setup_small_mario()
        
        # self.mario_images = self.setup_large_mario()
        self.images = self.mario_images[self.marios_action]
        self.rect = self.images[0].get_rect()
        
        self.v = Vector()
        self.posn = self.v
        self.rect.y =  446
        self.posn.y = self.rect.y
        self.x = float(self.rect.x)
        self.posn.x = self.x
        self.timer = Timer(self.images, 0, delay=500, is_loop=True)

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
            
            jump_right = [image_sheet.get_image(offsetx * slot, offsety, sizex, sizey, scale)
                                for slot in self.small_mario["jump_right"]]
            
            jump_left = [image_sheet.get_image(offsetx * slot, offsety, sizex, sizey, scale)
                                for slot in self.small_mario["jump_left"]]
            
            squatting_right = [image_sheet.get_image(offsetx * slot, offsety, sizex, sizey, scale)
                                for slot in self.small_mario["still_right"]]
            
            squatting_left = [image_sheet.get_image(offsetx * slot, offsety, sizex, sizey, scale)
                                for slot in self.small_mario["squatting_left"]]
            
            
            return {"left": left_images, "right": right_images,
                                "still_left": still_left, "still_right": still_right,
                                "jump_right": jump_right, "jump_left": jump_left,
                                "squatting_right": squatting_right, "squatting_left": squatting_left}

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


    def setup_fire_mario(self):
            offsetx = self.fire_mario["offsetx"]
            offsety = self.fire_mario["offsety"]
            sizex = self.fire_mario["sizex"]
            sizey = self.fire_mario["sizey"]
            
            # this is how much to stretch the image from the sheet
            scale = self.fire_mario["scale"]
            
            image_sheet = SpriteSheet('assets/characters/mario/mario.png')
            
            left_images = [image_sheet.get_image(offsetx * slot,
                                                           offsety, sizex, sizey, scale)
                                for slot in self.fire_mario["left"]]
            
            right_images = [image_sheet.get_image(offsetx * slot, offsety,
                                                            sizex, sizey, scale)
                                 for slot in self.fire_mario["right"]]
            
            still_left = [image_sheet.get_image(offsetx * slot,
                                                          offsety, sizex, sizey, scale)
                               for slot in self.fire_mario["still_left"]]
            
            still_right = [image_sheet.get_image(offsetx  * slot, offsety, sizex, sizey, scale)
                                for slot in self.fire_mario["still_right"]]
            
            jump_right = [image_sheet.get_image(offsetx * slot, offsety, sizex, sizey, scale)
                                for slot in self.fire_mario["jump_right"]]
            
            jump_left = [image_sheet.get_image(offsetx * slot, offsety, sizex, sizey, scale)
                                for slot in self.fire_mario["jump_left"]]
            
            squatting_right =[image_sheet.get_image(offsetx * slot, offsety, sizex, sizey - 5, scale)
                                for slot in self.fire_mario["squatting_right"]]
            
            squatting_left =[image_sheet.get_image(offsetx * slot, offsety, sizex, sizey - 5, scale)
                                for slot in self.fire_mario["squatting_left"]]

            
            return {"left": left_images, "right": right_images, "still_left": still_left,
                    "still_right": still_right, "jump_right": jump_right,
                    "jump_left": jump_left, "squatting_right": squatting_right, "squatting_left": squatting_left}


    # In this function you set the action based on the key pressed
    # Once the action is set the actual moving happens inside of update()
    def move_mario(self, key, event_type):

        keys_dir = {pg.K_KP0: ["jump_", "still_"], pg.K_UP: ["jump_", "still_"],
            pg.K_s: ["squatting_", "still_"], pg.K_DOWN: ["squatting_", "still_"],
            pg.K_a: ["left", "still_"], pg.K_LEFT: ["left", "still_"],
            pg.K_d: ["right", "still_"],
            pg.K_RIGHT: ["right", "still_", "jump_"]}

        # If you are pressing or holding a key this is where the action is set
        if event_type == "KEYDOWN":
            # if you press d or the right arrow
            if key == pg.K_d or key == pg.K_RIGHT:
                # then mario should be facing right, and all his animations face right
                self.marios_direction = "right"
                if not self.running:
                    # sets the flag that we are walking
                    self.walking = True
            # if you press a or the left arrow then do this stuff
            elif key == pg.K_a or key == pg.K_LEFT:
                # animations should face left
                self.marios_direction = "left"
                if not self.running:
                    self.walking = True
            # no matter what his action (state) is set here
            self.set_action(keys_dir[key][0])
        # if you let the key go this is where that action is set
        elif event_type == "KEYUP":
            if key == pg.K_a or key == pg.K_LEFT or key == pg.K_RIGHT or key == pg.K_d:
                self.walking = False
            self.set_action(keys_dir[key][1])


    def set_action(self, action):
        new_action = action
        if action == "squatting_":
            join_me = ["squatting_", self.marios_direction]
            new_action = ''.join(join_me)
        elif action == "still_":
           join_me = ["still_", self.marios_direction]
           new_action = ''.join(join_me)
        elif action == "jump_":
            join_me = ["jump_", self.marios_direction]
            new_action = ''.join(join_me)

        self.timer = Timer(self.mario_images[new_action], 0, delay=self.delay, is_loop=True)


    def update(self):
        # this is where we check if he is still alive and update x and y pos
        if self.walking and self.velocity < self.settings.mario_walk_speed:
            # sets the direction if its left its negative if its right its positive
            self.velocity += self.acceleration
            self.v.x += self.velocity if self.marios_direction == "right" else -self.velocity
        elif not self.walking and self.velocity != 0:
            # this is where deceleration would happen or maybe sliding
            self.velocity = 0

        # Check collisions with all tiles from all layers
        self.game.ground.check_collisions(self)
        self.game.blocks.check_collisions(self)
        self.game.pipes.check_collisions(self)
        self.game.grass.check_collisions(self)
        self.game.clouds.check_collisions(self)

        self.posn += self.v
        self.v
        self.posn, self.rect = self.clamp( self.posn, self.rect, self.settings)
        self.draw()

    # this binds the vector to the image rect. if other objs need it ill put it in a class
    def clamp(self, posn, rect, settings):
        left, top = posn.x, posn.y
        width, height = rect.width, rect.height
        left = max(0, min(left, settings.window_size[0] - width))
        # set lowest point here
        if self.mario_status == "fire_mario":
            if self.marios_action == "squatting_right" or self.marios_action == "squatting_left":
                top = max(0, min(top, settings.window_size[1] / 2 + 20))
            top = max(0, min(top, settings.window_size[1] / 2 + 8))
        else: 
            top = max(0, min(top, settings.window_size[1] / 2 + height - 25))

        return Vector(x=left, y=top), pg.Rect(left, top, width, height)

    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.centerx, rect.centery = self.rect.centerx, self.rect.centery
        self.screen.blit(image, rect)

