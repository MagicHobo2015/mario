class Settings():
    def __init__(self):
        self.window_size = [1200, 800]
        self.tile_size = 32
        self.mario_speed = 2
        self.mario_walk_speed = .05
        self.mario_run_speed = .5
        self.mario_jump_height = 10
        self.gravity = 2
        self.mario_lives = 3
        # debugging settings
        #if set to true frames count is displayed in the console
        self.show_fps = False

