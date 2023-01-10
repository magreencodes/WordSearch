#clear output function when the user finds a word- clear()
#use dictionary for accounts and for the set words for each topic
#random.choice(string.ascii_uppercase)

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
			grid[i].append('*')

def display():
	for row in grid:
		for col in row:
			print(col," ", end= "" )
		print()

setup()



def place_horizontal(word):
	row = random.randint(0, height-1)
	col = random.randint(0, width-len(word))
	for i in range(len(word)):
		grid[row][col+i]= word[i]
		
# place_hori('cat')


def place_vertical(word):
	row = random.randint(0, height-1)
	col = random.randint(0, width-len(word))
	for i in range(len(word)):
		grid[col+i][row]= word[i]


	
def place_diagonal(word):
	row = random.randint(0, height-1)
	col = random.randint(0, width-len(word))
	for i in range(len(word)):
					
						
place_vertical('dog')
place_horizontal('cat')
# place_diagonal('bird')
display()



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
