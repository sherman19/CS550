#Scott Herman
#Ms. Healey
#1/11/19
#In Monte Carlo situations, a random walk is taken and the distance from the origin is analyzed.
#Monte Carlo situations are used to evaluate hard probability problems that deal with forecasting risk.

import random
 
Home = [0,0]
Position = [x,y]
x = 0
y = 0

for x in range(10):
	for y in range(10):
		x_direction = random.randint(0,1)
		if x_direction == 0:
			x = x -= 1
		if x_direction == 1:
			x = x += 1

		y_direction = random.randint(0,1)
		if y_direction == 0:
			y = y -= 1
		if y_direction == 1:
			y = y += 1	

walking_home = 0
if abs.x + abs.y >= 4:
	walking_home += 1
percentage = walking_home/1000

#If we perform this simulation many times we can see that the size of the longest walk 
#where you will resturn home more than 50% of the time is 22. 

#If we perform the dart simulation, we get pi. The value becomes more precise with more iterations.

in_circle = 0

for i in range(1000):
	for j in range(1000):
		i = random()
		j = random()
		x = sqrt(i^2 +j^2)

if x <= 1:
	in_circle +=1

percentage2 = in_circle/1000



