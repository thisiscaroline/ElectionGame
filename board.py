# Board class

import random

class Board:

	# Initialize a Board object; includes grid and both players
	def __init__(self, player1, player2):
		self.grid = [[0 for x in range(11)] for y in range(11)]
		self.player1 = player1
		self.player2 = player2
		
	# Prints the board
	def printIt(self):
		print('\n')
		for row in self.grid:
			print(" ".join(map(str,row)))
			
	"""
	TODO:
		- Add in DIE ROLL function
		- Add State Card Deck (key/val dict)
		- Rearrange board tiles
		- Add MOVE PLAYER function
		- Election Road tiles
		- Customizable player inputs
		- Probability moderators
	"""