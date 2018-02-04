# coding=utf-8

import pygame
from pygame.locals import *

MULTIPLIER = 64

# 64 jakoluku

class Level:
	def __init__(self, level_map):
		self.level_map = level_map

	# Loads our tile map which contains the map textures
	def load_tile_table(self, filename, width, height):
		image = pygame.image.load(filename).convert()
		image_width, image_height = image.get_size()
		tile_table = []
		for tile_x in range(0, int(image_width/width)):
			line = []
			tile_table.append(line)
			for tile_y in range(0, int(image_height/height)):
				rect = (tile_x*width, tile_y*height, width, height)
				line.append(image.subsurface(rect))
		return tile_table

	# Renders the the textures to the map based on our level array that is downloaded from a file
	def render_map(self, screen):
		table = self.load_tile_table("images/tilesetti.png", 64, 64)
		x = 0
		y = 0
		for value in self.level_map:
			if x == 16:
				y += 1
				x = 0
			#GRASS
			if value == 0:
				screen.blit(table[0][0], (x*MULTIPLIER, y*MULTIPLIER))
			#ROAD
			if value == 1:
				screen.blit(table[1][0], (x*MULTIPLIER, y*MULTIPLIER))
			#BASICTOWER
			if value == 2:
				screen.blit(table[2][0], (x*MULTIPLIER, y*MULTIPLIER))
			#MACHINEGUN
			if value == 3:
				screen.blit(table[0][1], (x*MULTIPLIER, y*MULTIPLIER))
			#CATAPULT
			if value == 4:
				screen.blit(table[1][1], (x*MULTIPLIER, y*MULTIPLIER))
			#UBER
			if value == 5:
				screen.blit(table[2][1], (x*MULTIPLIER, y*MULTIPLIER))
			#FINISH LINE
			if value == 9:
				screen.blit(table[3][0], (x*MULTIPLIER, y*MULTIPLIER))
			x += 1
