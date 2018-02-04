# coding=utf-8
import pygame
from pygame.locals import *


class Projectile:
	def __init__(self, currentpos, direction, size, color, speed):
		self.currentpos = currentpos
		self.direction = direction
		self.size = size
		self.color = color
		self.speed = speed

	# This function moves the projectile using a shitty algorithm
	def move_projectile(self):
		y_difference = self.direction[0] - self.currentpos[0]
		x_difference = self.direction[1] - self.currentpos[1]

		if (abs(y_difference) < 25 and abs(x_difference) < 25):
			return False

		if y_difference < 0:
			y = self.currentpos[0] - self.speed
		elif y_difference > 0:
			y = self.currentpos[0] + self.speed
		else:
			y = self.currentpos[0]


		if x_difference < 0:
			x = self.currentpos[1] - self.speed
		elif x_difference > 0:
			x = self.currentpos[1] + self.speed
		else:
			x = self.currentpos[1]

		self.currentpos = (y, x)

	# returns 0 if the projectile reached the target 1 otherwise
	def reached_target(self):
		if self.currentpos == self.direction:
			return 0
		else:
			return 1
