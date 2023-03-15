#------------------------------------------------------------------------------#
#  Description: this is a class to make using sprite sheets easy 			   #
#																			   #
#																			   #
#______________________________________________________________________________#

import pygame as pg

class SpriteSheet:
	# load sheet
	def __init__(self, filename):
		# first load the sheet
		try:
			self.sheet = pg.image.load(filename).convert_alpha()
		except:
			print(f'Unable to load spriteSheet image: {filename}')
		
	def get_image(self, sprite_width, sprite_height, ):
		# first create and empty square
		image = pg.Surface((sprite_width, sprite_height)).convert_alpha()
		# this gets the image from the sheet
		image.blit(self.sheet, (0,0), (30, 0, sprite_width, sprite_height))
		return image



# small mario 30 wide and 15 tall