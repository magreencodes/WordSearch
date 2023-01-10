#clear output function when the user finds a word- clear()

import string 
import random

grid = []

#later on in the menu the user can selected the dimensions
width = 11
height = 10 

def setup():
	for i in range(height):
		grid.append([])
		for j in range(width):
			grid[i].append(random.choice(string.ascii_uppercase))

def display():
	for row in grid:
		for col in row:
			print(col," ", end= "" )
		print()

setup()


# def place_word(word):
# 	for i in range(len(word)):
# 		for row in grid:
# 			if row - len(word) < 0: 
# 				grid[random.randrange(row)][i] = word[::-1][i]
# 			else:
# 				False 

# place_word("cat")

display()

def place_word(word):
	for i in range(len(word)):
		for row in range(0, width):
			grid[random.randrange(width-len(word))][i]= word[i]
# def place_word(word):
# 	rand_num= [1,2,3,4]
# 	rand_num = random.choice(directions)
# 	if directions == 1:
# 		for i in range(height):
# 			if height-len(word) > 0:
# 				grid[0][1] = word[i]
# 	if directions == 2:
# 		for i in range(height):
# 			if height-len(word) > 0:
# 				grid[0][1] = word[::-1][i]
# 	if directions == 3:
# 		for i in range(width):
# 			if width-len(word) > 0:
# 				grid[1][0] = word[i]
# 		if directions == 4:
# 				for i in range(width):
# 					if width-len(word) > 0:
# 						grid[1][0] = word[::-1][i]
						
						

place_word('dog')


 # [1,1]- going diagonally 


# class Board:
# 	def __init__(self, grid, height=10, width=11):
# 		self.height = height 
# 		self.width = width
# 		self.grid = []
# 		self.create_grid()
		
# 	def create_grid(self):
# 		for i in range(self.height):
# 			self.grid.append([])
# 			for j in range(self.width):
# 				self.grid[i].append('*')
		
# 	def display(self):
# 		# self.grid = self.height*self.width
# 		for row in self.grid:
# 			for col in row:
# 				print(col," ", end= "" )
# 			print()

		#def place_word(word):
			# for i in range(len(word)):
		# rowsize= self.width - len(word)
		# colsize= self.height - len(word)

	#WORK IN PROGRESS 
	# def fit_word(self, word):
	# 	if direction[0] == 0: #means that the word is not moving to the right if true then that's the width 
	# 	else:
	# 		self.width - len(word)
				

		
def main1():

	animals = Board(10, 11)
	print(animals.height, animals.width,)

	# history.create_grid()
	# history.display()

	

# main1()

