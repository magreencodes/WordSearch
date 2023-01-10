#using these later on with random.choice(string.ascii_uppercase)
import string
import random

grid = []

# def setup():
# 	for i in range(10):
# 		grid.append([])
# 		for j in range(11):
# 			grid[i].append('*')

# def display():
# 	for row in grid:
# 		for col in row:
# 			print(col," ", end= "" )
# 		print()

# setup()


#Original Place word
# def place_word(word):
# 	for i in range(len(word)):
# 		grid[0][i] = word[::-1][i]

#ERROR HERE- working on randomizing the placement of the word now
# def place_word(word):
# 	for i in range(len(word)):
# 		word = random.choice(word, word[::-1][i])
# 		format= [grid[i][0], grid[0][i], grid[i][i]]
# 		random.choice(tuple(format)) = word # [1,0]- going to the right, [0,1]- going down, [1,1]- going diagonally

# place_word("cat")
# display()


class Board:
	def __init__(self, height=10, width=11, word):
		# self.grid = grid
		self.height = height
		self.width = width
		self.word = word

	def create_grid(self):
		for i in range(self.height):
			grid.append([])
			for j in range(self.width):
				grid[i].append('*')

	def display(self, grid):
		# self.grid = self.height*self.width
		for self.width in grid:
			for self.height in self.width:
				print(self.height, " ", end=" ")
			print()

	#WORK IN PROGRESS
	# def fit_word(self, word):
	# 	if direction[0] == 0: #means that the word is not moving to the right if true then that's the width
	# 	else:
	# 		self.width - len(word)



def main1():

	animals = Board(10, 11, 'cat')
	print(animals.height, animals.width, animals.word)

	# history.create_grid()
	# history.display()



main1()



#know where the words are- starting point and direction- later on when you check ud they got all of the words
#idea for later: list of where the words are on the grid check to see for word a boolean- need to store
