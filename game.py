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


class Game():
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(self.settings.window_size)
        pg.display.set_caption("Mario!")
        self.running = True


    def check_events(self):
        # keys_dir = {pg.K_w: Vector(0, -1), pg.K_UP: Vector(0, -1), 
        #     pg.K_s: Vector(0, 1), pg.K_DOWN: Vector(0, 1),
        #     pg.K_a: Vector(-1, 0), pg.K_LEFT: Vector(-1, 0),
        #     pg.K_d: Vector(1, 0), pg.K_RIGHT: Vector(1, 0)}
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # if you got here its time to shut down
                self.running = False
                pg.quit()
                sys.exit()

    def draw(self):
        self.screen.fill((255, 255, 255))

    def play(self):
        # Main loop for the game happens here, for now
        while self.running:
            # check events for quit
            self.check_events()
        

# minimum stuff here
def main():
    game = Game()
    game.play()

# just to trigger main
if __name__ == "__main__":
    main()