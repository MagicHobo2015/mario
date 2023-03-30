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
        self.walking_acceleration = .001
        self. running_acceleration = .008
        self.friction = .05
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

    def move_mario(self, keys):
        
        # this list translates keys into animation actions
        keys_dir = {pg.K_KP0: ["jump_", "still_"], pg.K_UP: ["jump_", "still_"],
        pg.K_s: ["squatting_", "still_"], pg.K_DOWN: ["squatting_", "still_"],
        pg.K_a: ["left", "still_"], pg.K_LEFT: ["left", "still_"],
        pg.K_d: ["right", "still_"],pg.K_RIGHT: ["right", "still_", "jump_"]}
        
        # ***************************************** PRESSING NOTHING *****************************
        # if keys == []:
        #     self.walking = False
        #     self.running = False
        #     self.set_action("still_")
        #     keys = pg.key.get_pressed()
        # **************************************** RUNNING ***************************************
        if (keys[pg.K_RIGHT] or keys[pg.K_d]) and keys[pg.K_KP_PERIOD]:
            # youre running
            # set the animation to the correct direction
            self.marios_direction = "right"
            self.running = True
            self.walking = False
            self.set_action(keys_dir[pg.K_RIGHT][0])
        elif (keys[pg.K_LEFT] or keys[pg.K_a]) and keys[pg.K_KP_PERIOD]:
            # youre here running to the left
            self.marios_direction = "left"
            self.running = True
            self.walking = False
            self.set_action(keys_dir[pg.K_LEFT][0])
        # ************************************************* END RUNNING ***************************
        # ************************************************** WALKING ******************************
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            # just walking here to the right
            self.walking = True
            self.running = False
            self.marios_direction = "right"
            self.set_action(keys_dir[pg.K_RIGHT][0])
        elif keys[pg.K_LEFT] or keys[pg.K_a] and not keys[pg.K_KP_PERIOD]:
            # just walking left here
            self.walking = True
            self.running = False
            self.marios_direction = "left"
            self.set_action(keys_dir[pg.K_LEFT][0])

        # ************************************************* END WALKING ***************************
        # ************************************************* SQUATTING *****************************
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.walking = False
            self.running = False
            self.set_action(keys_dir[pg.K_DOWN][0])
        # ************************************************ END SQUATTING **************************
            

    def stop(self):
        self.walking = False
        self.running = False
        self.jumping = False
        self.set_action("still_")


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
        print(f'running: {self.running} walking: {self.walking}')
        # this is where we check if he is still alive and update x and y pos
        if self.walking and self.velocity < self.settings.mario_walk_speed:
            # sets the direction if its left its negative if its right its positive
            self.velocity += self.walking_acceleration
        elif self.walking and self.velocity > self.settings.mario_walk_speed:
            # here you were running and switched to a walk but still going run speed
            # so slow down
            self.velocity = self.settings.mario_walk_speed
        elif not self.walking and not self.running:
            if self.velocity > 0:
                self.velocity -= self.friction
            elif self.velocity < 0:
                self.velocity = 0
                self.v.x = 0
            # this is where deceleration would happen or maybe sliding
        elif self.running and self.velocity < self.settings.mario_run_speed:
            self.velocity += self.running_acceleration


        print(f'velocity: {self.velocity}')
        # # Check collisions with all tiles from all layers
        # self.game.ground.check_collisions(self)
        # self.game.blocks.check_collisions(self)
        # self.game.pipes.check_collisions(self)
        # self.game.grass.check_collisions(self)
        # self.game.clouds.check_collisions(self)
        
        
        self.v.x += self.velocity if self.marios_direction == "right" else -self.velocity
        self.posn += self.v
        self.posn, self.rect = self.clamp( self.posn, self.rect, self.settings)
        self.draw()

    # this binds the vector to the image rect. if other objs need it ill put it in a class
    def clamp(self, posn, rect, settings):
        left, top = posn.x, posn.y
        width, height = rect.width, rect.height
        left = max(0, min(left, settings.window_size[0] / 2 - width))
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

