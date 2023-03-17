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
		# scale up the image
		# TODO:scale here
		
	def get_image(self, sprite_locationx, sprite_locationy, sprite_width, sprite_height, ):
		# first create and empty surface
		image = pg.Surface((sprite_width, sprite_height), pg.SRCALPHA)
		# this gets the image from the sheet
		image.blit(self.sheet, (0,0), (sprite_locationx, sprite_locationy, sprite_width, sprite_height))
		# i may need to do this somewhere else its for mario
		image = pg.transform.rotozoom(image, 0, 6)
		return image



# small mario 30 wide and 15 tall - offsetx=30
