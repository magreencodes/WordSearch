import string
import random

grid = []


# row is like the x
# col is like the y

height = 10
width = 10


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
	for row in range(height):
		for col in range(width):
			if grid[row][col] == '*' :
				grid[row][col] = random.choice(string.ascii_uppercase)


def place_horizontal(word):
	word = random.choice([word, word[::-1]])
	row = random.randint(0, height-1) # height then width
	col = random.randint(0, width-len(word))
	for i in range(len(word)):
		grid[row][col+i]= word[i]


def place_vertical(word):
	word = random.choice([word, word[::-1]])
	row = random.randint(0, height-len(word)) # was 1
	col = random.randint(0, width-len(word))
	for i in range(len(word)):
		grid[col+i][row]= word[i]


def place_diagonalright(word):
	word = random.choice([word, word[::-1]])
	row = random.randint(0, height- len(word))
	col = random.randint(0, width- len(word))
	for i in range(len(word)):
		grid[col+i][row+i]= word[i]


def place_diagonalleft(word):
	word = random.choice([word, word[::-1]])
	row = random.randint(0, height- len(word))
	col = random.randint(0, width- len(word))
	for i in range(len(word)):
		grid[col+i][row-i]= word[i]



# def check():

# before you put in dog you check all of the places that you plan to put down then keep trying to you place it


def place(word,grid):
	# for word in words:
	# 	placed_wrd = True
	# 	while not placed_wrd:
	word_directions = [ '1', '2', '3', '4']
	word_directions = random.choice(word_directions)

	if word_directions == '1':
		place_horizontal(word)

	if word_directions == '2': #backwards horizontal
		place_vertical(word)

	if word_directions == '3': # forward vertical
		place_diagonalright(word)

	if word_directions == '4': # backwards vertical
		place_diagonalleft(word)



# 	last_letterx = x + len(word)
# 	last_lettery = y + len(word)




word = 'cat'
grid = place(word,grid)

setup()
# place_horizontal('cat')
replace_blanks()
# place_vertical('dog')

# place_diagonalright('bird')
# place_diagonalleft('frog')
display()



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

