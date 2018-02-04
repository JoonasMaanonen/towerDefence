import pygame
from pygame.locals import *
from Projectile import *

class Tower:
	def __init__(self, dmg, rangee, towerpos, shotspeed, cost, color):
		self.dmg = dmg # int
		self.range = rangee # int
		self.towerpos = towerpos # Tuple
		self.shotspeed = shotspeed # in ms
		self.cost = cost # int
		self.on_cooldown = False # bool
		self.projectiles = []
		self.missile_color = color

	# This function adds a projectile to the towers projectile list, projectile is added
	# each time when a tower shoots
	def add_projectile(self, currentpos, direction, size, color, shotspeed):
		projectile = Projectile(currentpos, direction, size, color, shotspeed)
		self.projectiles.append(projectile)

	# This function removes the projectile from the projectiles list, when the projectile
	# reaches its destination. It needs to removed so it doesnt get drawn to the screen anymore
	def remove_projectile(self, projectile):
		self.projectiles.remove(projectile)

	# This function uses Projectiles own move function to move all the projectiles in the tower's
	# projectiles list.
	def update_projectiles(self):
		for projectile in self.projectiles:
			if projectile.move_projectile() == False:
				self.remove_projectile(projectile)
			else:
				pass

	# enemypos is a tuple with two coordinates
	def check_range(self, enemypos):
		dist = abs(pow((self.towerpos[0] - enemypos[0]), 2) + pow((self.towerpos[1] - enemypos[1]), 2) )
		return dist 

	# Returns towers range
	def get_tower_range(self):
		return self.range

	# This function handles the shooting functionality of a tower
	def shoot(self, enemy):
		#Shoot if enemy not dead
		if enemy.dead_or_alive():
			enemy.health = enemy.get_hp() - self.dmg
			print("Tower in pos:", self.towerpos, "shot!")
			# Returns 0 If tower killed an Enemy used to increase the cash
			if enemy.health <= 0:
				print("Enemy died by tower: ", self.towerpos)
				enemy.alive = False
				return 0
	
	def get_shotspeed(self):
		return self.shotspeed


	# This function checks whether the player has enough money to buy this particular tower
	def cost_check(self, cash):
		if self.cost > cash:
			print("Player doesn't have enough money.")
			return True


