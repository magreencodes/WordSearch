import string 
import random
import shelve
import time
 

class Board:
	def __init__(self, grid, height=12, width=12):
		self.height = height 
		self.width = width
		self.grid = []
		self.create_grid()
		
	def create_grid(self):
		for i in range(self.height):
			self.grid.append([])
			for j in range(self.width):
				self.grid[i].append('*')
		
	def display(self):
		for row in self.grid:
			for col in row:
				print(col," ", end= "" )
			print()
			
	def replace_blanks():
		for row in range(self.height):
			for col in range(self.width):
				if self.grid[row][col] == '*' :
					self.grid[row][col] = random.choice(string.ascii_uppercase)



def place_horizontal(word):
	word = random.choice([word, word[::-1]])
	row = random.randint(0, height-len(word)) 
	col = random.randint(0, width-len(word))  
	for i in range(len(word)):
		grid[row][col+1]= word[i]



def place_vertical(word):
	word = random.choice([word, word[::-1]])
	row = random.randint(0, height-len(word)) 
	col = random.randint(0, width-len(word)) 
	for i in range(len(word)):
		grid[col+1][row]= word[i]



def place_diagonalright(word):
	word = random.choice([word, word[::-1]])
	row = random.randint(0, height-len(word)) 
	col = random.randint(0, width-len(word))  
	for i in range(len(word)):
		grid[col+1][row+1]= word[i]	



def place_diagonalleft(word):
	word = random.choice([word, word[::-1]])
	row = random.randint(0, height-len(word)) 
	col = random.randint(0, width-len(word)) 
	for i in range(len(word)):
		grid[col+1][row-1]= word[i]	



def place(word,grid):
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

		# print [row],[col]

		# for i in rowrange(0,len(word)):
		# 	grid[col + word_directions[1]*i][row + word_directions[0]*i] = word[i]

list_wrd = ['lists', 'shelve', 'variable']
for word in list_wrd:
	place(word,grid)
			
def game_countdown(t):
	while t:
		mins = t // 60
		secs = t % 60 
		timer = '{02d}:{02d}'.format(mins,secs)
		print(timer, end = "\r" ) 
		time.sleep(1)
		t -= 1
		print('Times Up! Stop word search!')
		

users = []
pswd = []
accounts= {}
def new_user():
	global users
	global pswd 

	account_num = random.randint(0,10)
	
	
	with shelve.open('datastorage') as ds:
		while True:
			if 'users' in ds:
				users = ds['users']
			if 'pswd' in ds:
				pswd = ds['pswd']
					
			create_username = input('enter username:')
			create_password = input('enter password:')
			confirm_password = input('re-enter password:') 
			
			if create_password == confirm_password:
				print('Password Accepted. Your account has been created!')
				users.append(create_username) 
				pswd.append(create_password)
				accounts[account_num] = [create_username, create_password, list_wrd]
				break	
			else:
				print('Passwords Do Not Match! Try again.')
				
		ds['users'] = users
		ds['pswd'] = pswd

def old_user():
	
	with shelve.open('datastorage') as ds:
		if 'users' in ds:
			users = ds['users']
		if 'pswd' in ds:
			pswd = ds['pswd']
		
	enter_username = input('enter username:')
	enter_password = input('enter password:')

	if enter_username in users:
		index = users.index(enter_username)  
		if enter_password == pswd[index]:
			print("Login successful!")
			return True
		
	print(" User doesn't exist or wrong password! Try again!")
	menu()
	


response = ''

def menu():
	while True:
		print('Welcome to THE WORD SEARCH STUDY GUIDE')
		response =  input ('Do you have an account? yes or no: ')
		if response == 'yes':
			old_user()
		elif response == 'no':
			new_user()

		print(" 1. View Account 2.Play Game 3. Quit")
		choice = input('What would you like to do?')

		if choice == '1':
			print(accounts)
			print(accounts.get(account_num))

		if choice == '2':
			response = input('READY TO PLAY? yes or no: ')
			if response == 'yes':
				Board()
				place()
				print('_'* 15)
				print(list_wrds)
				game_countdown(300)
	
				enter_word = input('Enter word: ')
				for enter_word in list_wrds:
					'Great job!'
			
		elif response == 'no':
			while response != 'no':
				menu()
				
		if choice == '3':
			menu()
							
menu()	
