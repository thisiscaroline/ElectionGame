# Player class

class Player:
	
	# Initialize a Player object
	def __init__(self, name, party):
		self.name = name
		self.party = party
		EVs = 0
		self.probGen = 1.0		# All state probability
		self.probHome = 1.25	# Home state prob.
		self.probOR = 1.0		# Oregon prob.
		self.probLA = 1.0		# Louisiana prob.
		self.probSC = 1.0		# South Carolina prob.
		self.probFL = 1.0		# Florida prob.