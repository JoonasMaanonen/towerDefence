# coding=utf-8
import pygame, io, sys

from pygame.locals import *
from GameState import *
from Game import *
from Enemy import *

WIDTH = 1024
HEIGHT = 768
FPS = 33
TOWERSHOOTINGFREQ = 500 # ms
ENEMYSPAWNINGFREQ = 1000 # ms


def main():
	# Initialise screen
	pygame.init()

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	screen.fill((255,255,255))
	pygame.display.set_caption('Ultimate Tower Defence')

	# Inits Game Class
	game = Game(screen)
	# Inits Event loop
	game.state_handler()

	#Setups clock
	clock = pygame.time.Clock()
	time_elapsed_since_last_shot = 0
	spawning_time = 0

	# *------------------GAME LOOP------------------*

	while True:
		pygame.time.wait(FPS)
		#This function handles keyboard presses ETC. Return 0 if Game is exited
		if game.event_handler() == 0:
			return

		# The Tower shoot at the speed of TOWERSHOOTINGFREQ which is the delay in MS
		dt = clock.tick()

		time_elapsed_since_last_shot += dt

		if game.start_flag:
			if time_elapsed_since_last_shot > TOWERSHOOTINGFREQ:
				game.tower_shooting()
				time_elapsed_since_last_shot = 0

			#Enemies are spawned according to the frequency and towers shoot according to a frequency too.
			spawning_time += dt
			if spawning_time > ENEMYSPAWNINGFREQ:
				if game.wave.spawn_wave_members() == 0:
					if(game.wave.is_wave_dead()):
						print("Uusi Wave spawnautuu nyt!")
						game.wave.mobcount = 0
						game.wave.next_wave()
						game.wave.spawn_wave_members()
				spawning_time = 0

		# When the game is on LEVEL state the game updates every frame.
		if game.gamestate.current_state == game.gamestate.GAMEPLAY:
			game.update_game()


if __name__ == '__main__': main()
