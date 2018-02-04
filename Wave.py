# coding=utf-8
from Enemy import *


BLACK  = (   0,   0,   0)
RED    = ( 255,   0,   0)
WHITE  = ( 255, 255, 255)
GREEN  = (   0, 255,   0)
PURPLE = ( 128,   0, 128)
CYAN =   (  51, 255, 255)
PINK = (255, 102, 255)


# Viholliset: Violetti -- Pleb
#  		      Musta    -- Jonne
# 		      Punainen -- Boss
#

#TODO: Make the wavedata loadable from a file

wavedata1 = {"Count": 50 ,"Pleb": 40, "Jonne": 9, "Boss": 1, "Imba": 0}
wavedata2 = {"Count": 45 ,"Pleb": 10, "Jonne": 30, "Boss": 5, "Imba": 0}
wavedata3 = {"Count": 20 ,"Pleb": 0, "Jonne": 0, "Boss": 20, "Imba": 0}
wavedata4 = {"Count": 20 ,"Pleb": 0, "Jonne": 0, "Boss": 0, "Imba": 100}


class Wave:
	def __init__(self, screen, route):
		self.screen = screen
		self.enemies = []
		self.wavecount = wavedata1["Count"]
		self.plebcount = wavedata1["Pleb"]
		self.jonnecount = wavedata1["Jonne"]
		self.bosscount = wavedata1["Boss"]
		self.imbacount = wavedata1["Imba"]
		self.mobcount = 1
		self.route = route # route that the wave follows
		self.wave_index = 1 # Increments by one when a whole wave dies, determines which wave to spawn next

	# This function handles the spawning of the the monsters
	def spawn_wave_members(self):
		if self.mobcount == self.wavecount:
			return 0

		if self.plebcount != 0:
			vihollinen = Blob(self.screen, PURPLE, 15, 4, "Pleb", self.route)
			self.enemies.append(vihollinen)
			self.plebcount -= 1
			return 1

		if self.jonnecount != 0:
			vihollinen = Blob(self.screen, BLACK, 30, 4, "Jonne", self.route)
			self.enemies.append(vihollinen)
			self.jonnecount -= 1
			return 1

		if self.bosscount != 0:
			vihollinen = Blob(self.screen, RED, 200, 2, "Boss", self.route)
			self.enemies.append(vihollinen)
			self.bosscount -= 1
			return 1

		if self.imbacount != 0:
			vihollinen = Blob(self.screen, CYAN, 1400, 8, "Imba", self.route)
			self.enemies.append(vihollinen)
			self.imbacount -= 1
			return 1

		self.mobcount += 1


	# This function moves the whole wave using the Blob classes own move function for each enemy
	def move_wave(self):
		lost_hitpoints = 0
		for enemy in self.enemies:
			if enemy.dead_or_alive():
				if enemy.move() == 0:
					lost_hitpoints += 5
					enemy.at_goal = True
			else:
				self.enemies.remove(enemy)
		return lost_hitpoints

	# This function draws the all the enemies to the screen using their own draw functions from the Blob naming
	def draw_wave(self):
		for enemy in self.enemies:
			if enemy.dead_or_alive() and enemy.at_goal == False:
				enemy.draw()
			else:
				self.enemies.remove(enemy)

	# This function updates the wave state aka removes enemies from the wave if they die or reach the end
	def update_wave(self):
		if not self.enemies:
			self.next_wave()
			self.spawn_wave_members()

		for enemy in self.enemies:
			if enemy.dead_or_alive == False:
				self.enemies.remove(enemy)
		# Player loses hitpoints when enemy has died
		else:
			self.draw_wave()
			lost_hitpoints = self.move_wave()
		return lost_hitpoints

	# This determines if the whole has died
	def is_wave_dead(self):
		if len(self.enemies) == 0:
			return True
		else:
			return False

	# This function loads the next wave when the current wave has died it uses the self.wave_index to determine
	# which wave to spawn the value increments by one each time a wave has completely diseapeared.
	def load_next_wave(self):
		if self.wave_index == 2:
			self.wavecount = wavedata2["Count"]
			self.plebcount = wavedata2["Pleb"]
			self.jonnecount = wavedata2["Jonne"]
			self.bosscount = wavedata2["Boss"]
			self.imbacount = wavedata2["Imba"]

		if self.wave_index == 3:
			self.wavecount = wavedata3["Count"]
			self.plebcount = wavedata3["Pleb"]
			self.jonnecount = wavedata3["Jonne"]
			self.bosscount = wavedata3["Boss"]
			self.imbacount = wavedata3["Imba"]

		if self.wave_index == 4:
			self.wavecount = wavedata4["Count"]
			self.plebcount = wavedata4["Pleb"]
			self.jonnecount = wavedata4["Jonne"]
			self.bosscount = wavedata4["Boss"]
			self.imbacount = wavedata4["Imba"]

	# This spawns the next wave by using the load_next_wave() function
	def next_wave(self):
		if self.mobcount == 0:
			self.wave_index += 1
			self.load_next_wave()
