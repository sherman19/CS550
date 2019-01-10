#Scott Herman
#Ms. Healey
#1/10/19

import random

#player keeps first door choice

for i in range(1000):

	number_of_wins = 0

	l = [1,2,3]

	winning_door = randint(1,3)
	player_first_door = randint(1,3)

	if player_first_door == winning_door:
		number_of_wins = number_of_wins + 1

#player changes door choice

for i in range(1000):

	number_of_wins = 0

	l = [1,2,3]

	winning_door = randint(1,3)
	player_first_door = randint(1,3)

	if player_first_door != winning_door:
		number_of_wins = number_of_wins + 1

#In the Monty Hall problem, it is always better to switch the choice of your door.
#If you keep your door, then you have a 1/3 chance of getting it right.
#Changing your pick is the same as choosing the other two doors.
#It does not matter that pennies are going to be revealed behind one of the doors, there can be only one door with a car.
#Since for any set of two doors there will be at least one door with pennies,
#Switching your guess is the same as picking the two doors that you did not originally pick.
 