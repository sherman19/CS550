#Scott Herman
#Ms. Healey
#Game of Moo//Guess a Number
#CS550
#11/13/18
#On my honor, I have neither given nor received unauthorized aid.

import random

def game():

#First form a random secret, s, having four different digits. 

#There are 10*9*8*7 = 5040 possible secrets. 

	r = random.randint(0,5039)

#debugging
#print(r)

	s = [0,0,0,0]

#Get the first digit s[0].

	s[0] = r%10
	r = int(r/10)

#Get the second digit s[1] and make sure it is different.

	s[1] = r%9
	r = int(r/9)
	if s[1] >= s[0]:
		s[1] += 1

#Get the third digit s[2] and make sure it is different.

	s[2] = r%8
	r = int(r/8)
	if s[2] >= s[0]:
		s[2] += 1

	if s[2] >= s[1]:
		s[2] += 1

	if s[2] == s[0]:
		s[2] += 1

#Get the fourth digit s[3] and make sure it is different.

	s[3] = r

	if s[3] >= s[0]:
		s[3] += 1

	if s[3] >= s[1]:
		s[3] += 1

	if s[3] >= s[2]:
		s[3] += 1

	while s[3] == s[0] or s[3] == s[1] or s[3] == s[2]:
		s[3] +=1

#debugging	
#print(s)

#Set up for the main loop.

	g = [0,0,0,0]
	count = 0
	bulls = 0

#Main loop for the game

	while bulls < 4:

#Verify we have a good input.

		while True:
			guess = (input("Choose a Number:"))

			if len(guess) != 4:
				print("Input Error.")
				continue
			try:
				g[0] = int(guess)
			except ValueError:
				print("Input Error\n")
				continue

			if g[0] > 9876 or g[0] < 123:
				print("Input Error.")
				continue
			break
			
#debugging
#print(g)

#Chop up the input string.

		g[1] = int(g[0]/10)
		g[0] %= 10
		g[2] = int(g[1]/10)
		g[1] %= 10
		g[3] = int(g[2]/10)
		g[2] %= 10
#debugging
#print(g)

#It must have four different digits.

		if g[0] == g[1] or g[0] == g[2] or g[0] == g[3] or g[1] == g[2] or g[1] == g[3] or g[2] == g[3]:
			print("Input Error.")
			continue
		
#We have a good input.

		count += 1
		cows = 0
		bulls = 0

#Count the number of hits.

		for i in range(0,4):
			if s[i] == g[i]:
				bulls += 1

			for j in range(0,4):
				if s[i] == g[j] and i != j:
					cows += 1

#Deal with the annoyance of singular and plural.

		if bulls == 1 and cows == 1:
			print("1 bull, 1 cow")

		elif cows == 1:
			print(str(bulls) + " bulls " + str(cows) + " cow")

		elif bulls == 1:
			print(str(bulls) + " bull " + str(cows) + " cows")

		else:
			print(str(bulls) + " bulls " + str(cows) + " cows")

		if bulls == 4:
			if count == 1:
				print("Jackpot!")
			else:
				print("You won in " + str(count) + " guesses.")
			return
	game()

print("Welcome to Moo")

while True:

	In = input("Enter N for a new game, H for help, and Q for quit: ")
	if In == "Q" or In == "q":
		break
	if In == "H" or In == "h":
		print("\nThe objective of the game is to guess a secret four digit number.")
		print("The number will have four different digits and the goal is to")
		print("guess it in as few attepmts possible. Each correct digit in the")
		print("wrong place is a cow, and each correct digit in the right place")
		print("is a bull, so 4 bulls wins.\n")
		continue
	if In == "N" or In == "n":
		game()


