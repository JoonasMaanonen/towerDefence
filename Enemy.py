import pygame
from pygame.locals import *

# TODO: Put this route creation to another place and do it in a smarter way.
KERROIN = 64

class Blob():
	def __init__(self, screen, color, health, speed, name, route):
		self.speed = speed # Division of 64
		self.screen = screen
		self.route_index = 0
		self.color = color
		self.health = health
		self.alive = True
		self.name = name 
		self.at_goal = False 
		self.route = route
		self.ylist = [y[0] for y in route] 
		self.xlist = [x[1] for x in route]
		self.x = self.route[0][1] + 16
		self.y = self.route[0][0]
		self.rect = Rect(self.y,self.x,20,25)

	def dead_or_alive(self):
		if self.health <= 0:
			self.alive = False
		return self.alive


	def draw(self):
		if self.dead_or_alive() == True:
			pygame.draw.rect(self.screen, self.color, self.rect)
		else:
			pass

	# This functions uses an algorithm to move the enemies
	def move(self):
		if self.alive:					
			# Distance between route point and enemypoint
			ydist = (self.ylist[self.route_index+1] - self.y) + 16
			xdist = (self.xlist[self.route_index+1] - self.x) + 16

			#Goal has been reached
			if (self.x - 16 == self.xlist[-1] and self.y - 16 == self.ylist[-1]):
				return 0

			#Next point has been reached
			if (abs(xdist) == 0 and abs(ydist) == 0):
				self.route_index += 1

			# Move the enemy according to direction
			if  abs(xdist) != 0:
				if xdist < 0:
					self.x -= self.speed
				if xdist > 0:
					self.x += self.speed
			if abs(ydist) != 0:
				if ydist < 0:
					self.y -= self.speed
				if xdist > 0:
					self.y += self.speed
				self.y += self.speed


			self.rect = Rect(self.y, self.x, 20, 25)
			self.rect.move(self.y,self.x)


	def get_pos(self):
		pos = (self.y/64, self.x/64)
		return pos

	def get_hp(self):
		return self.health

