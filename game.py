#---------------------------------------------------------------------------#
#            _____               .__                                        #
#           /     \ _____ _______|__| ____                                  #
#          /  \ /  \\__  \\_  __ \  |/  _ \                                 #
#         /    Y    \/ __ \|  | \/  (  <_> )                                #
#         \____|__  (____  /__|  |__|\____/                                 #
#                 \/     \/                                                 #
#                                                                           #
# By: Joshua Land                                                           #
# Description: This is the main driver for the game                         #
#---------------------------------------------------------------------------#

# Imports go here
import pygame as pg
import sys
# hand crafted imports
from settings import Settings
from vector import Vector
from mario import Mario
from vector import Vector
from spriteSheet import SpriteSheet
import pytmx

tmx_data = pytmx.TiledMap("map.tmx")
print(tmx_data.layers)

class Game():
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(self.settings.window_size)
        pg.display.set_caption("Mario!")
        self.running = True
        # helps limit frames per second
        self.clock = pg.time.Clock()
        self.mario = Mario(self)


    def check_events(self):
        keys_dir = {pg.K_w: [Vector(0, -1), "left", "still_left"], pg.K_UP: [Vector(0, -1), "left", "still_left"],
            pg.K_s: [Vector(0, 1), "squatting", "still_right"], pg.K_DOWN: [Vector(0, 1), "squatting", "still_right"],
            pg.K_a: [Vector(-1, 0), "left", "still_left", "jump_left"],
            pg.K_LEFT: [Vector(-1, 0), "left", "still_left", "jump_left"],
            pg.K_d: [Vector(1, 0), "right", "still_right", "jump_right"],
            pg.K_RIGHT: [Vector(1, 0), "right", "still_right", "jump_right"]}
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # if you got here its time to shut down
                self.game_over()
            elif event.type == pg.KEYDOWN:
                key = event.key
                if key in keys_dir:
                    self.mario.v += self.settings.mario_speed * keys_dir[key][0]
                    self.mario.set_action(keys_dir[key][1])
            elif event.type == pg.KEYUP:
                key = event.key
                if key in keys_dir:
                    self.mario.v = Vector()
                    # set mario to still
                    self.mario.set_action(keys_dir[key][2])

    def game_over(self):
        # run shutdown animation
        #shutdown everything
        self.running = False
        # clean up pygame
        pg.quit()
        sys.exit()
        
        
    def draw(self):
        # to clear the screen
        self.screen.fill((0, 0, 0))
        self.mario.update()
        pg.display.flip()

    def play(self):
        # Main loop for the game happens here, for now
        while self.running:
            # check events for quit
            self.check_events()
            # a little something for debuggin
            if self.settings.show_fps: print(self.clock.get_fps())
            
            self.draw()
            pg.display.update()
            self.clock.tick(60)
        

# minimum stuff here
def main():
    game = Game()
    game.play()

# just to trigger main
if __name__ == "__main__":
    main()