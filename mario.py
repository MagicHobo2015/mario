import pygame as pg
from pygame import sprite


class character(sprite):
	def __init__(self, game):
		super().__init__()
		self.screen = game.screen
		self.settings = game.settings