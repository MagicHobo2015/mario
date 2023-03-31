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
import pytmx
import os
# hand crafted imports
from settings import Settings
from vector import Vector
from mario import Mario
from vector import Vector
from spriteSheet import SpriteSheet
from ground import Ground
from blocks import Blocks
from pipe import Pipes
from grass import Grass
from clouds import Clouds

class Game():
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(self.settings.window_size)
        pg.display.set_caption("Mario!")
        # helps limit frames per second
        self.clock = pg.time.Clock()
        
        # Get the path to the map.tmx file and store it in tmx_data
        # This store all the data for the entire level, including all the blocks and their coordinates
        tmx_data = pytmx.load_pygame(os.path.join(os.path.dirname(__file__), "assets", "level_one", "map.tmx"))
        self.running = True

        # Get all the non-empty blocks in the layer "Ground"
        ground = tmx_data.get_layer_by_name("Ground")
        self.ground = Ground(game=self, layer=ground)

        # Get all the non-empty blocks in the layer "Blocks"
        blocks = tmx_data.get_layer_by_name("Blocks")
        self.blocks = Blocks(game=self, layer=blocks)

        # Get all the non-empty blocks in the layer "Pipes"
        pipes = tmx_data.get_layer_by_name("Pipes")
        self.pipes = Pipes(game=self, layer=pipes)

        # Get all the non-empty blocks in the layer "Grass"
        grass = tmx_data.get_layer_by_name("Grass")
        self.grass = Grass(game=self, layer=grass)

        # Get all the non-empty blocks in the layer "Clouds"
        clouds = tmx_data.get_layer_by_name("Clouds")
        self.clouds = Clouds(game=self, layer=clouds)

        self.mario = Mario(self)
        
    def check_events(self):
          
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # if you got here its time to shut down
                self.game_over()
            else:
                keys = pg.key.get_pressed()
                self.mario.move_mario(keys)


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
        self.ground.update()
        self.blocks.update()
        self.pipes.update()
        self.grass.update()
        self.clouds.update()
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