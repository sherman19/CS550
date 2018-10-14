#Scott Herman 
#Minesweeper Game

import sys
import random

# add 1 around bomb location
def increase_around_bombs(r,c):
	for y in range(r-1, r+2):
		for x in range(c-1, c+2):
			if (board[y][x] is not "*"):
				board[y][x] += 1

# command line info
# +2 to make minesweeper "buffer"
# board larger than actually appears
h = int(sys.argv[1]) + 2
w = int(sys.argv[2]) + 2
mines = int(sys.argv[3])

# create an empty board
def boards():
	global board
	global board2
board = [[0]*w for i in range(h)]

# adding mines. Picks random box at x, y, then assigns a bomb to it.
# also adjusts counts around the edges 
for i in range(mines):
	x = random.randint(1,h-2)
	y = random.randint(1,w-2)
	while board[x][y] == '*':
		x = random.randint(1,h-2)
		y = random.randint(1,w-2)
	board[x][y] = '*'
	increase_around_bombs(x,y)

# creates board without surrounding extras
for i in range (1,len(board)-1):
	for j in range(1,len(board[0])-1):
		print(board[i][j],end=" ")
	print("")

board2 = [["?"]*w for i in range(h)]
for i in board2:
	print(*i)
#making game from board
def play():
	count = 0
	global xc
	global yc
	#winning()
	xc = int(input("choose x coordinates\n\n\n>>")) 
	yc = int(input("choose y coordinates\n\n\n>>")) 
	FlagClear = input("Do you want to clear or flag (clear/flag)\n\n>>")
#user choosing to flag
	if FlagClear == "flag":
		board2[yc][xc] = "f"
		for i in board2:
			print(*i)
		play()		
		if board[yc][xc] == "*":
			count+=1
			if count == mines:
				winning()
				for i in board2:
					print(*i)			
			play()	
#user choosing to clear
	elif FlagClear == "clear":
			if board[yc][xc] == "*":
				losing()
			elif board[yc][xc] == 0:
				checkarea()
				for i in range (1,len(board2)-1):
					for j in range(1,len(board2[0])-1):
						print(board2[i][j],end=" ")
					print("")
				play()
			else:
				board2[yc][xc] = board[yc][xc]
				for i in range (1,len(board2)-1):
					for j in range(1,len(board2[0])-1):
						print(board2[i][j],end=" ")
					print("")
				play()
	else:
		print("try again")
		play()
#zero checking
def checkingzeros(x,y):
	if board[y][x] == 0 and board2[y][x] == "?":
		board2[y][x] = 0

		if x<w-2 and board2[y][x+1] == "?":
			checkingzeros(x+1,y)

		if y<h-2 and board2[y+1][x] == "?":
			checkingzeros(x,y+1)

		if x>0 and board2[y][x-1] == "?":
			checkingzeros(x-1,y)

		if y>0 and board2[y-1][x] == "?":
			checkingzeros(x,y-1)


#checking the area

def checkarea():
	for w in range(h):
		for xc in range(-1,2):
			for yc in range(-1,2):
				checkingzeros(yc,xc)
#winning

def winning():
	print("You won the game!")
	restart = input("Retry the game?\n\n0 for yes \n1 for no\n\n>>")
	if restart == "0":
		boards()
	if restart == "1":
		quit()

#losing

def losing():
	print("You lost.")
	losschoice = input("Retry the game?\n\n0 for yes \n1 for no\n\n>>")
	if losschoice == "0":
		boards()
	if losschoice == "1":
		quit()
	else:
		print("Try again next time.")
		gameover()


boards()
play()









