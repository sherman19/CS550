import random
x = random.randint(0,100)	
count = 0
def game():
	global count
	count += 1
	choice = int(input("Choose Number"))
	if ValueError:
		print("Please enter a number.")
	if x == choice:
		print("You guessed it.")
	elif x < choice: 
		print("That was too high. Guess again.")
		game()
	elif x > choice:
		print("That was too low. Guess again.")
		game()
	else:
		print("Wrong input. Try again.")
		game()

game()

while True:
	if count < 2:
		print("Good job. You are a good guesser.")
		break
	elif count < 5:
		print("You did an okay job. It took you fewer than five attempts.")
		break
	elif count < 8: 
		print("Okay job. It took you fewer than eight attempts.")
		break
	else:
		print("It took you more than seven attempts. Try harder next time.")
		break


