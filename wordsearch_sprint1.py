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



def replace_blanks():
	for row in grid:
			grid.replace('*', random.choice(string.ascii_uppercase) )


def place_horizontal(word):
	word = random.choice([word, word[::-1]])
	row = random.randint(0, height-1)
	col = random.randint(0, width-len(word))
	for i in range(len(word)):
		grid[row][col+i]= word[i]



def place_vertical(word):
	word = random.choice([word, word[::-1]])
	row = random.randint(0, height-1)
	col = random.randint(0, width-len(word))
	for i in range(len(word)):
		grid[col+i][row]= word[i]



def place_diagonal(word):
	word = random.choice([word, word[::-1]])
	row = random.randint(0, height-1)
	col = random.randint(0, width-len(word))
	for i in range(len(word)):
		grid[col+i][row]= word[i]	
		row+=1

setup()

place_vertical('dog')
place_horizontal('cat')
place_diagonal('bird')
display()
# replace_blanks()

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
				
		
def main1():

	animals = Board(10, 11)
	print(animals.height, animals.width,)

	# history.create_grid()
	# history.display()

	

# main1()

		
#know where the words are- starting point and direction- later on when you check ud they got all of the words 
#idea for later: list of where the words are on the grid check to see for word a boolean- need to store 
