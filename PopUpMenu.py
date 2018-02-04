import pygame, sys
from pygame.locals import *


BLACK = (   0,   0,   0)
RED   = ( 255,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
PURPLE = ( 128,  0, 128)

SCREENWIDTH = 1024
SCREENHEIGHT = 768

HALFWIDTH = SCREENWIDTH / 2
HALFHEIGHT = SCREENHEIGHT / 2


class PopUpMenu:
	def __init__(self, screen):
		self.top = HALFWIDTH
		self.left = HALFHEIGHT
		self.screen = screen
	
	# This function makes the popup that pops up on the screen when an empty square is clicked
	def make_popup(self):
		options = ["Choose tower with the number keys.",
				   "Press W to start the assault of squares!!        ", 
				   "[1] Basic Tower cost: 100, range: 3, dmg: 2       ",
				   "[2] Darter Tower cost: 250, range: 3, dmg: 4       ",
				   "[3] Catapult Tower cost: 500, range: 5, dmg: 8   ",
			       "[4] Uber Tower cost: 1337, range: 6, dmg: 10        ",
			       "[0] Press To Cancel.              "]
		BASICFONT = pygame.font.SysFont("Arial", 24, True, False)
		for i in range(len(options)):
			textSurf = BASICFONT.render(options[i], True, RED, BLACK)
			textRect = textSurf.get_rect()
			textRect.center = (self.top, self.left)
			self.screen.blit(textSurf, textRect)
			self.left += 29
		pygame.display.update()


	# This function has functionality aka what happens when the user chooses a button.
	def do_popup(self):
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				# Basic tower was selected 
				elif event.type == pygame.KEYDOWN and event.key == K_1:
					return 1
				# Machine Gun tower was selected 
				elif event.type == pygame.KEYDOWN and event.key == K_2:
					return 2
				# Catapult Tower was selected
				elif event.type == pygame.KEYDOWN and event.key == K_3:
					return 3
				# Uber Tower was selected 
				elif event.type == pygame.KEYDOWN and event.key == K_4:
					return 4
				# Tower selection was cancelled
				elif event.type == pygame.KEYDOWN and event.key == K_0:
					return 0




