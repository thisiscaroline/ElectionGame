# Board class

from random import shuffle

class Board:

	# Initialize a Board object; includes grid and both players
	def __init__(self, player1, player2):
		self.grid = [["__" for x in range(11)] for y in range(11)]
		self.player1 = player1
		self.player2 = player2
		self.stateList = [("Alabama", 10), ("Arkansas", 6), ("California", 6), ("Colorado", 3), 
							("Connecticut", 6), ("Delaware", 3), ("Florida", 4), ("Georgia", 11), 
							("Illinois", 21), ("Iowa", 11), ("Indiana", 15), ("Kansas", 5), 
							("Kentucky", 12), ("Louisiana", 8), ("Maine", 7), ("Maryland", 7),
							("Massachusetts", 13), ("Michigan", 11), ("Minnesota", 5), ("Mississippi", 8),
							("Missouri", 15), ("Nebraska", 3), ("Nevada", 3), ("New Hampshire", 5),
							("New Jersey", 9), ("New York", 35), ("North Carolina", 10), ("Ohio", 22),
							("Oregon", 3), ("Pennsylvania", 29), ("Tennessee", 12), ("Texas", 8), 
							("Rhode Island", 4), ("South Carolina", 7), ("Vermont", 5), ("Virginia", 11),
							("West Virginia", 5), ("Wisconsin", 10)]
		
	# Prints the board
	def printBoard(self):
		print('\n')
		for row in self.grid:
			print(" ".join(map(str,row)))
			
	# Randomly shuffles the list of states - called ONCE
	def shuffleStates(self):
		shuffle(self.stateList)
		print("\n >> \x1b[1;32mShuffle successful.\x1b[0m")
	
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