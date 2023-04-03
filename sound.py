import pygame as pg
import time

class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(1)
        self.sounds = {"mario_jump_small": pg.mixer.Sound("assets/sounds/smb_jump_small.wav"),
                       "mario_jump_super": pg.mixer.Sound("assets/sounds/smb_jump_super.wav"),}

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def play_sound(self, sound):
        self.sounds[sound].play()

    def gameover(self): 
        self.stop_bg() 
        pg.mixer.music.load('assets/sounds/smb_gameover.wav')
        self.play_bg()
        time.sleep(3.8)
