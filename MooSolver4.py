#Scott Herman
#Ms. Healey
#MooSolver
#http://vixra.org/pdf/1601.0302v1.pdf
#http://slovesnov.users.sourceforge.net/bullscows/bulls_and_cows.pdf
#On my honor, I have neither given nor received unauthorized aid.

#The objective of this program is to solve the game Moo.
#Moo is a game where a user tries to guess four different digits.
#A bull indicates the right number in the right sport and a cow
#indicates the right number but in teh wrong spot.
#This program uses a strategy of guessing 0123 
#and then guessing the samllest number that is still consistent
#with the previous bulls and cows information.

#Play 10 games of Moo 
#	using a simple strategy:
#		guess the smallest value consistent
#		with the previous guesses

import random

scorelist = []
gamecount = 10

for game in range(0, gamecount):

#Pick a secret

#First form a random "secret" having four different digits. 

#There are 10*9*8*7 = 5040 possible secrets. 

	r = random.randint(0,5039)

#debugging
#print(r)

	secret = [0,0,0,0]

#Get the first digit secret[0].

	secret[0] = r%10
	r = int(r/10)

#Get the second digit secret[1] and make sure it is different.

	secret[1] = r%9
	r = int(r/9)
	if secret[1] >= secret[0]:
		secret[1] += 1

#Get the third digit secret[2] and make sure it is different.

	secret[2] = r%8
	r = int(r/8)
	if secret[2] >= secret[0]:
		secret[2] += 1

	if secret[2] >= secret[1]:
		secret[2] += 1

	if secret[2] == secret[0]:
		secret[2] += 1

#Get the fourth digit secret[3] and make sure it is different.

	secret[3] = r

	if secret[3] >= secret[0]:
		secret[3] += 1

	if secret[3] >= secret[1]:
		secret[3] += 1

	if secret[3] >= secret[2]:
		secret[3] += 1

	while secret[3] == secret[0] or secret[3] == secret[1] or secret[3] == secret[2]:
		secret[3] +=1

#debug
	print("Secret ", secret)


#Construct the all list containing all possible secrets set to True (possible)
#For each combination, 10 choose 4, the 24 permutations are added to the list
 
	all = []
	possible = 5040

	first  = 0
	second  = 1
	third = 2
	fourth = 2
# "fourth" will be incremented to 3 on the first pass
	

	while len(all) < 5040:
	# get the next increasing combination of 4 different digits
		while first != 6:
			if fourth != 9:
				fourth += 1
				break
			elif third != 8:
				third += 1
				fourth = third + 1
				break
			elif second != 7:
				second += 1
				third = second + 1
				fourth = third + 1
				break
			else:
				first += 1
				second = first + 1
				third = second + 1
				fourth = third + 1
				break
	#debug
	#	print("combination ", first, second, third, fourth)

	# then append all 24 permutations to the all list
		all.append([first, second, third, fourth, True])
		all.append([first, second, fourth, third, True])
		all.append([first, third, second, fourth, True])
		all.append([first, third, fourth, second, True])
		all.append([first, fourth, second, third, True])
		all.append([first, fourth, third, second, True])
		all.append([second, first, third, fourth, True])
		all.append([second, first, fourth, third, True])
		all.append([second, third, first, fourth, True])
		all.append([second, third, fourth, first, True])
		all.append([second, fourth, first, third, True])
		all.append([second, fourth, third, first, True])
		all.append([third, first, second, fourth, True])
		all.append([third, first, fourth, second, True])
		all.append([third, second, first, fourth, True])
		all.append([third, second, fourth, first, True])
		all.append([third, fourth, second, first, True])
		all.append([third, fourth, first, second, True])
		all.append([fourth, first, third, second, True])
		all.append([fourth, first, second, third, True])
		all.append([fourth, third, first, second, True])
		all.append([fourth, third, second, first, True])
		all.append([fourth, second, first, third, True])
		all.append([fourth, second, third, first, True])

#Guessing loop, pick the first possible, still True, entry from "all" as next guess

	guesscount = 0
	bulls = 0

	while bulls != 4: # More work to do

		guesscount += 1
		for n in range(0, 5040):
			if all[n][4] == True: # Found next guess
				break

		guess = all[n]
		print("Guess ", guess)

# evaluate the guess with respect to the secret
		cows = 0
		bulls = 0
		for i in range(0,4):
			if secret[i] == guess[i]:
				bulls += 1
			for j in range(0,4):
				if secret[i] == guess[j] and i != j:
					cows += 1

#debug
#		print("bulls ", bulls, " cows ", cows)

# Set inconsistent entries in the all list to False and decrement possible solutions

		for i in range(0,5040):

			if all[i][4] == True: # only look at ones still possible

				b = 0
				c = 0
				
				for k in range(0, 4):
				
					if all[i][k] == guess[k]:
						b += 1

					for j in range(0, 4):
						if all[i][k] == guess[j] and k != j:
							c += 1

				if c != cows or b != bulls: # inconsistent
					all[i][4] = False
					possible -= 1

#debug
#		print("possible ", possible)


#Secret found, 4 bulls, record number of guesses and continue main loop to play next game

	scorelist.append(guesscount)

# Print results and summary

print("Scores: ", scorelist)
worst = 0
total = 0
for i in range(0, gamecount):
	if scorelist[i] > worst:
		worst = scorelist[i]
	total += scorelist[i]
mean = float(total) / gamecount
print("Worst: ", worst, " Mean: ", mean)








