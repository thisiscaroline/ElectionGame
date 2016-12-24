#!/usr/bin/env python3

# Election game based off a project I did in APUSH

from board import Board
from player import Player

# Main loop
def main():
	
	p1 = Player('Hayes', 'R')
	p2 = Player('Tilden', 'D')
	newBoard = Board(p1, p2)
	newBoard.printBoard()
	
	newBoard.shuffleStates()
	
	print(newBoard.stateList)
	print(newBoard.stateList[0])
	
	print("\n\n >> \x1b[1;32mokay\x1b[0m")

# Start program from main
if __name__ == '__main__':
	main()