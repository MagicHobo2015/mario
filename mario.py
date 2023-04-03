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

    small_mario = {"offsetx": 30, "offsety" : 0, "sizex": 17, "sizey": 16,
                   "left": [3, 4, 5], "right": [ 8, 9, 10, 12],
                   "still_right": [7], "still_left": [6],"squatting_right": [7],
                   "squatting_left": [6], "jump_right": [12], "jump_left": [1],"scale": 2}

    dying_mario = {"offsetx": 390, "offsety": 15, "sizex": 15, "sizey": 15,
                   "still_right": [0], "scale": 2}

    large_mario = {"offsetx": 30, "offsety" : 52, "sizex": 19, "sizey": 35,
                   "left": [3, 4, 5], "right": [10, 9, 8],
                   "still_right": [6.9], "still_left": [6], "squatting_right": [13],
                   "squatting_left": [0], "jump_right": [11.9], "jump_left": [1], "scale": 2}
    
    fire_mario = {"offsetx": 25, "offsety" : 120, "sizex": 23, "sizey": 35,
                   "left": [4, 5, 6], "right": [11.4, 10.36, 9.44],
                   "still_right": [8.28], "still_left": [7], "squatting_right": [15.4],
                   "squatting_left": [0], "jump_right": [14.4], "jump_left": [1], "scale": 2}


    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.lives = self.settings.mario_lives
        self.walking_acceleration = .001
        self. running_acceleration = .008
        self.jump_acceleration = 5
        self.friction = .05
        self.velocity = 0.0
        self.jump_velocity = 0.0
        # this is to track the change in y as we jump
        self.deltay = 0
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
        self.posn = Vector()
        self.posn.x = float(self.rect.x)
        self.posn.y = 452.0
        self.rect.centery = self.posn.y
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


    def setup_dying_mario(self):
            offsetx = self.dying_mario["offsetx"]
            offsety = self.dying_mario["offsety"]
            sizex = self.dying_mario["sizex"]
            sizey = self.dying_mario["sizey"]
            
            # this is how much to stretch the image from the sheet
            scale = self.dying_mario["scale"]
            
            image_sheet = SpriteSheet('assets/characters/mario/mario.png')
            
            still_right = [image_sheet.get_image(offsetx * slot, offsety, sizex, sizey, scale)
                                for slot in self.dying_mario["still_right"]]
            
            return {"still_right": still_right}

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
        keys_dir = {pg.K_SPACE: ["jump_", "still_"], pg.K_UP: ["jump_", "still_"],
        pg.K_s: ["squatting_", "still_"], pg.K_DOWN: ["squatting_", "still_"],
        pg.K_a: ["left", "still_"], pg.K_LEFT: ["left", "still_"],
        pg.K_d: ["right", "still_"],pg.K_RIGHT: ["right", "still_", "jump_"]}
        
        # **************************************** RUNNING ***************************************
        if (keys[pg.K_RIGHT] or keys[pg.K_d]) and keys[pg.K_KP_PERIOD]:
            # youre running
            # set the animation to the correct direction
            self.marios_direction = "right"
            self.running = True
            self.delay = 50
            self.walking = False
            self.set_action(keys_dir[pg.K_RIGHT][0])
        elif (keys[pg.K_LEFT] or keys[pg.K_a]) and keys[pg.K_KP_PERIOD]:
            # youre here running to the left
            self.marios_direction = "left"
            self.running = True
            self.delay = 50
            self.walking = False
            self.set_action(keys_dir[pg.K_LEFT][0])
        # ************************************************* END RUNNING ***************************
        # ************************************************** WALKING ******************************
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            # just walking here to the right
            self.walking = True
            self.delay = 100
            self.running = False
            self.marios_direction = "right"
            self.set_action(keys_dir[pg.K_RIGHT][0])
        elif keys[pg.K_LEFT] or keys[pg.K_a] and not keys[pg.K_KP_PERIOD]:
            # just walking left here
            self.walking = True
            self.delay = 100
            self.running = False
            self.marios_direction = "left"
            self.set_action(keys_dir[pg.K_LEFT][0])

        # ************************************************* END WALKING ***************************
        # ************************************************* SQUATTING *****************************
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.walking = False
            self.jumping = False
            self.running = False
            self.set_action(keys_dir[pg.K_DOWN][0])
        # ************************************************ END SQUATTING **************************
        # ********************************************** JUMPING **********************************
        if keys[pg.K_SPACE]:
            self.jumping = True
            self.set_action("jump_")

            # Play the jump sound depending on if he is small or not
            if self.mario_status == "small_mario":
                self.game.sound.play_sound("mario_jump_small")
            elif self.mario_status == "large_mario" or self.mario_status == "fire_mario":
                self.game.sound.play_sound("mario_jump_super")
        # ******************************************* END JUMPING *********************************
            
    # ************************************ USABLE MARIO ACTIONS ***********************************
    def stop(self):
        self.walking = False
        self.running = False
        self.jumping = False
        self.velocity = 0
        self.v = Vector()
        self.set_action("still_")

    def shrink(self):
        self.mario_status = "small_mario"
        self.mario_images = self.which_image[self.mario_status]
        
    def grow(self):
        self.mario_status = "large_mario"
        self.mario_images = self.which_image[self.mario_status]
    
    def damage(self):
        if self.mario_status == "small_mario":
            self.dying = True
        elif self.mario_status == "large_mario" or self.mario_status == "fire_mario":
            self.shrink()
    
    def fire_power_mario(self):
        self.mario_status = "fire_mario"
        self.mario_images = self.which_image[self.mario_status]
        
    # ******************************* END ACTIONS *************************************************
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
        
        # **************************  CHECKING COLLISIONS HERE *******************************
        if self.game.ground.check_collisions(self):
            collisions = self.game.ground.check_collisions(self)
            self.posn.y = collisions[0].y - self.rect.height
        elif self.game.blocks.check_collisions(self):
            collisions = self.game.blocks.check_collisions(self)
            self.posn.y = collisions[0].y
        elif self.game.pipes.check_collisions(self):
            pipe_collisions = self.game.pipes.check_collisions(self)
            self.velocity = 0
            if pipe_collisions:
                for tile in pipe_collisions:
                    # if mario is moving left/right and collides, can assume that he is walking into the pipe
                    # so move his position out of the pipe
                    if self.v.x > 0:
                        self.rect.right = tile.left
                    if self.v.x < 0:
                        self.rect.left = tile.right
            self.stop()
            
        # *************************** END COLLISIONS *****************************************
            
        # this is where we check if he is still alive and update x and y pos
        if self.walking and self.velocity < self.settings.mario_walk_speed:
            # sets the direction if its left its negative if its right its positive
            self.velocity += self.walking_acceleration
        elif self.walking and self.velocity > self.settings.mario_walk_speed:
            # here you were running and switched to a walk but still going run speed
            # so slow down
            self.velocity = self.settings.mario_walk_speed
        elif not self.walking and not self.running and not self.jumping:
            if self.velocity > 0:
                self.velocity -= self.friction
            elif self.velocity < 0:
                self.velocity = 0
                self.v.x = 0
                
            # this is where deceleration would happen or maybe sliding
        elif self.running and self.velocity < self.settings.mario_run_speed:
            self.velocity += self.running_acceleration
        elif self.jumping and self.deltay <= self.settings.mario_jump_height:
            self.jump_velocity += self.jump_acceleration
            self.deltay += self.jump_velocity
        elif not self.jumping and self.deltay >= self.settings.mario_jump_height:
            self.deltay -= self.settings.gravity
            
        self.v.x += self.velocity if self.marios_direction == "right" else -self.velocity

        self.posn.y -= self.jump_velocity if self.jumping else -self.jump_velocity
        self.posn += self.v
        print(f'sending {self.posn.y} to be clamped')
        self.posn, self.rect = self.clamp( self.posn, self.rect, self.settings)
        self.draw()

    # this binds the vector to the image rect. if other objs need it ill put it in a class
    def clamp(self, posn, rect, settings):
        print(f'clamping: {posn.y}')
        left, top = posn.x, posn.y
        width, height = rect.width, rect.height
        left = max(0, min(left, settings.window_size[0] / 2 - width))
        # set lowest point here
        if self.mario_status == "fire_mario":
            if self.marios_action == "squatting_right" or self.marios_action == "squatting_left":
                top = max(0, min(top, settings.window_size[1] - height))
            top = max(0, min(top, settings.window_size[1] - height))
        else: 
            top = max(0, min(top, settings.window_size[1] - height))
        print(f'Top ended up: {top}')
        return Vector(x=left, y=top), pg.Rect(left, top, width, height)

    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.centerx, rect.centery = self.rect.centerx, self.rect.centery
        self.screen.blit(image, rect)

