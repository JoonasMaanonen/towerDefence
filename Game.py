# coding=utf-8
import pygame, sys
from pygame.locals import *
from GameState import *
from Enemy import *
from Levels import *
from Tower import *
from Wave import *
from PopUpMenu import *

# VÄRIT:
BLACK = (   0,   0,   0)
RED   = ( 255,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
PURPLE = ( 128,  0, 128)
PINK = (255, 102, 255)
CYAN = (51, 255, 255)
ORANGE = (255,140,0)
BLUE = (0,0,255)

LEVEYS = 16
KORKEUS = 12

SCREENWIDTH = 1024
SCREENHEIGHT = 768

# Game class that takes care of running the game.
class Game():
	def __init__(self, screen):
		self.gamestate = GameState() # the current gamestate
		self.screen = screen
		self.towers = list() # List of all the towers in the game
		self.start_flag = False # This prevents the waves from spawning until the player has placed his towers
		self.player_money = 500
		self.hitpoints = 25
		self.level = [] # Level that the user selected
		self.route = [] # Route that the minions will take
		self.wave = Wave(screen, self.route) # Minion wave that is currently coming out of the enemyplace

# This function updates the game every frame.
	def update_game(self):
		# Renders the level that was loaded from a file
		level = Level(self.level)
		level.render_map(self.screen)

		# If user has pressed W the flag will be set to True and the enemies will be spawning
		if self.start_flag == True:
			lost_hitpoints = self.wave.update_wave()
			self.hitpoints -= lost_hitpoints
		else:
			pass

		# Loops through all the towers and projectiles and draws the projectiles to the screen
		for torni in self.towers:
			for projectile in torni.projectiles:
				pygame.draw.circle(self.screen, projectile.color, projectile.currentpos, projectile.size)

		# After they have drawn their position can be updated
		for torni in self.towers:
			torni.update_projectiles()

		# This is to handle the cash counter in the left upper corner
		BASICFONT = pygame.font.SysFont("Arial", 20, True, False)
		money_text = "Cash: " + str(self.player_money)
		textSurf = BASICFONT.render(money_text, True, PURPLE, BLACK)
		textRect = textSurf.get_rect()
		textRect.center = (45,15)
		self.screen.blit(textSurf, textRect)

		# This handles the hitpoints counter
		money_text = "Askin pizzat: " + str(self.hitpoints)
		textSurf = BASICFONT.render(money_text, True, RED, BLACK)
		textRect = textSurf.get_rect()
		textRect.center = (200,15)
		self.screen.blit(textSurf, textRect)

		# Update the screen and flip it
		pygame.display.update()
		pygame.display.flip()

		# Ifplayer has no hitpoints the game will and aka freeze
		if self.hitpoints <= 0:
			self.gamestate.current_state = self.gamestate.GAMEOVER
			self.state_handler()

	# This function loads the map that the is drawn to the screen, by using the the file that is given to it.
	def load_map(self, file):
		with open(file) as fp:
			for line in fp:
				cleaned_line = line.replace(" ", "").replace("\n", "")
				for letter in cleaned_line:
					numero = int(letter)
					self.level.append(numero)
		fp.close()

	# This function loads the route that the enemies will take, by using the the file that is given to it.
	# NOTE: Route can only go forward or stay the same on the x-axis, cannot go backwards since the enemy
	# 		move algorithm cant handle backwards movement yet
	def load_route(self, file):
		MULT = 64
		with open(file) as fp:
			for line in fp:
				split = line.replace("\n", "").split(",")

				piste = (int(split[0])*MULT, int(split[1])*MULT)
				self.route.append(piste)
		fp.close()
		self.wave = Wave(self.screen, self.route)


	# This function is the statemachine that handles the transitioning between different states of the program
	def state_handler(self):
		if(self.gamestate.current_state == self.gamestate.SPLASHSCREEN):
			splashscreen = pygame.image.load("images/splashscreen.png").convert()
			self.screen.blit(splashscreen, (0, 0))
			pygame.display.flip()

		elif(self.gamestate.current_state == self.gamestate.MAINMENU):
			mainmenu = pygame.image.load("images/mainmenu.png").convert()
			self.screen.blit(mainmenu, (0,0))
			pygame.display.flip()

		elif(self.gamestate.current_state == self.gamestate.GAMEPLAY):
			self.update_game()

		elif(self.gamestate.current_state == self.gamestate.GAMEOVER):
			BASICFONT = pygame.font.SysFont("Arial", 48, True, False)
			money_text = "Havisit Pelin, askin pizzat varastettiin "
			textSurf = BASICFONT.render(money_text, True, RED, BLACK)
			textRect = textSurf.get_rect()
			textRect.center = (SCREENWIDTH/2,SCREENHEIGHT/2)
			self.screen.blit(textSurf, textRect)
			pygame.display.flip()

			for event in pygame.event.get():
				if event.type == QUIT:
						pygame.quit
						sys.exit

	# This function handles user input
	def event_handler(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				return 0
			#Handle Keyboard events
			if event.type == pygame.KEYDOWN:
				if event.key == K_RETURN:
					if self.gamestate.current_state == self.gamestate.SPLASHSCREEN:
						self.gamestate.current_state = self.gamestate.MAINMENU
						self.state_handler()
				# User chose map 1
				elif event.key == K_1:
					if self.gamestate.current_state == self.gamestate.MAINMENU:
						self.load_map("maps/map1.txt")
						self.load_route("routes/route1.txt")
						self.gamestate.current_state = self.gamestate.GAMEPLAY
						self.state_handler()
				# User chose map 2
				elif event.key == K_2:
					if self.gamestate.current_state == self.gamestate.MAINMENU:
						self.load_map("maps/map2.txt")
						self.load_route("routes/route2.txt")
						self.gamestate.current_state = self.gamestate.GAMEPLAY
						self.state_handler()
				# User chose map 3
				elif event.key == K_3:
					if self.gamestate.current_state == self.gamestate.MAINMENU:
						self.load_map("maps/map3.txt")
						self.load_route("routes/route3.txt")
						self.gamestate.current_state = self.gamestate.GAMEPLAY
						self.state_handler()
				# User chose the secret map
				elif event.key == K_9:
					if self.gamestate.current_state == self.gamestate.MAINMENU:
						self.load_map("maps/map4.txt")
						self.load_route("routes/route4.txt")
						self.gamestate.current_state = self.gamestate.GAMEPLAY
						self.state_handler()
				# This is the starting toggle which will start the minions waves to come
				elif event.key == K_w:
					if self.gamestate.current_state == self.gamestate.GAMEPLAY:
						if self.start_flag == False:
							self.start_flag = True
			# This event handles mouse clicks which in our case handles the selection of towers
			elif event.type == pygame.MOUSEBUTTONUP:
				fx, fy = pygame.mouse.get_pos()
				# Change mouse position coordinates to integers
				ix = int(fx/64)
				iy = int(fy/64)
				print("Mouse pos (x, y)",ix,iy) # Mouse position on map

				# Adds tower only if we are on a LEVEL
				if self.gamestate.current_state == self.gamestate.GAMEPLAY:
					#ALGORITHM for changing matrix coordinates to 1 dimensional array
					index = (iy*(LEVEYS) + ix)
					if self.level[index] == 0:
						popupmenu = PopUpMenu(self.screen)
						popupmenu.make_popup()
						tower_value = popupmenu.do_popup()

						# The If structure ahead, creates a tower based on the user input
						if tower_value == 1:
							towerpos = (ix,iy)
							tower = Tower(2, 3, towerpos, 24, 100, PINK)
							# This checks if the player has the required cash to purchase this tower
							if tower.cost_check(self.player_money):
								break
							self.level[index] = 2 # Index determines which texture is rendered to the screen
							self.towers.append(tower)
							self.player_money -= tower.cost
							print("User selected Regular Tower")

						if tower_value == 2:
							towerpos = (ix, iy)
							tower = Tower(4, 3, towerpos, 24, 250, RED)
							# This checks if the player has the required cash to purchase this tower
							if tower.cost_check(self.player_money):
								break
							self.level[index] = 3
							self.towers.append(tower)
							self.player_money -= tower.cost
							print("User selected Dart Tower")

						if tower_value == 3:
							towerpos = (ix, iy)
							tower = Tower(8, 5, towerpos, 12, 500, BLUE)
							# This checks if the player has the required cash to purchase this tower
							if tower.cost_check(self.player_money):
								break
							self.level[index] = 4
							self.towers.append(tower)
							self.player_money -= tower.cost
							print("User selected Catapult Tower")

						if tower_value == 4:
							towerpos = (ix, iy)
							tower = Tower(10, 6, towerpos, 12, 1337, ORANGE)
							# This checks if the player has the required cash to purchase this tower
							if tower.cost_check(self.player_money):
								break
							self.level[index] = 5
							self.towers.append(tower)
							self.player_money -= tower.cost
							print("User selected Uber Tower")

						if tower_value == 0:
							print("User didn't select a tower")


	# This function loops through all the towers and handles their shooting actions and all the consequences
	def tower_shooting(self):
		for torni in self.towers:
			torni.on_cooldown = False
			for enemy in self.wave.enemies:
				enemypos = enemy.get_pos()
				#Calculates distance between enemy and tower
				dist = torni.check_range(enemypos)
				#Shoot
				if (torni.get_tower_range() >= dist and torni.on_cooldown == False):

					# enemypos is in single coordinates like 0, 1, 2
					# so it needs to be multiplied by 64 since the draw functions
					# handle everything in pixels nad 1 square is 64x64 pixels large
					enemy_y = enemypos[0] * 64
					enemy_x = enemypos[1] * 64

					tower_y = torni.towerpos[0] * 64
					tower_x = torni.towerpos[1] * 64

					# Need to convert to integers since this will be used in the add_projectile() function
					# with another integer
					tower_pixel_pos = (int(tower_y + 32), int(tower_x + 32))
					enemy_pixel_pos = (int(enemy_y), int(enemy_x))

					torni.add_projectile(tower_pixel_pos, enemy_pixel_pos, 10, torni.missile_color, torni.shotspeed)
					# Enemy died if returns 0
					if torni.shoot(enemy) == 0:
						if enemy.name == "Pleb":
							self.player_money += 10
						if enemy.name == "Jonne":
							self.player_money += 25
						if enemy.name == "Boss":
							self.player_money += 200
						if enemy.name == "Imba":
							self.player_money += 10000

					torni.on_cooldown = True
				else:
					pass


