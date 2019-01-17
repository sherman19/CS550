#Scott Herman
#Ms. Healey
#11/17/19
#https://fantasydata.com
#https://www.cbssports.com/fantasy/
#On my honor, I have neither given nor received unauthorized aid.

import random
import matplotlib.pyplot as plt


Ezekiel_Elliott = plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48], [11,12,16,20,28,16,14,21,38,12,23,15,10,23,21,0,13,1,15,25,12,39,25,15,0,0,0,0,0,0,11,13,13,13,11,29,8,17,3,11,30,25,20,19,18,12,10,0], 'b--', label = 'Ezekiel Elliot')
Todd_Gurley = plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48], [4,6,20,7,14,8,8,6,6,13,8,3,14,3,14,7,15,22,32,27,2,11,20,21,12,10,12,15,24,41,38,0,19,29,19,21,28,33,26,27,13,22,8,28,5,23,0,0], 'r--', label = 'Todd Gurley')
Melvin_Gordon = plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48], [17,17,13,17,11,9,29,15,31,13,8,19,0,0,0,0,13,13,13,2,27,26,3,19,3,14,8,9,13,22,18,12,18,23,14,23,17,32,0,18,22,14,18,0,0,0,11,6], 'y--', label = 'Melvin Gordon')

plt.xlabel('Regular Season Games in Sequence from 2016-2018')
plt.ylabel('Fantasy Points')
plt.title('Fanatsy Points By Star Running Backs the Past 3 Years')
plt.axis([0, 50, 0, 60])
plt.grid(True)
plt.legend()
plt.show()

Odell_Beckham_JR = plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48], [7,8,12,2,11,32,4,16,15,4,21,10,15,12,15,4,0,3,19,9,15,0,0,0,0,0,0,0,0,0,0,0,11,5,10,7,25,4,20,13,19,14,8,16,0,0,0,0], 'b--', label = 'Odell Beckham Jr.')
Julio_Jones = plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48], [12,16,1,36,2,19,17,2,17,13,3,11,0,0,6,15,6,10,9,3,7,15,7,11,5,7,38,2,9,5,14,8,17,6,9,17,6,14,8,18,16,17,12,1,22,14,8,19], 'r--', label = 'Julio Jones')
Antonio_Brown = plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48], [24,3,14,18,13,3,11,14,21,7,27,11,7,5,15,0,18,6,17,3,15,21,12,7,4,32,30,16,21,2,0,0,15,6,11,12,22,16,19,10,15,17,6,21,3,10,30,0], 'y--', label = 'Antonio Brown')

plt.xlabel('Regular Season Games in Sequence from 2016-2018')
plt.ylabel('Fantasy Points')
plt.title('Fanatsy Points By Star Wide Receivers the Past 3 Years')
plt.axis([0, 50, 0, 60])
plt.grid(True)
plt.legend()
plt.show()

Ezekiel_Elliott = plt.plot([2015,2016,2017,2018], [0,293.4,177.2,252.2], 'b--', label = 'Ezekiel Elliot')
Todd_Gurley = plt.plot([2015,2016,2017,2018], [187.4,155.2,319.3,313.1], 'r--', label = 'Todd Gurley')
Melvin_Gordon = plt.plot([2015,2016,2017,2018], [75.3,209.6,230.1,225.5],'y--', label = 'Melvin Gordon')
Odell_Beckham_JR = plt.plot([2015,2016,2017,2018], [223.3,195.6,49,153.3], '-o', label = 'Odell Beckham Jr.')
Julio_Jones = plt.plot([2015,2016,2017,2018], [245.1,176.9,163.9,212.9], '-o', label = 'Julio Jones')
Antonio_Brown = plt.plot([2015,2016,2017,2018], [246.2,201.3,209.3,219.7], '-o', label = 'Antonio Brown')

plt.xlabel('Season')
plt.ylabel('Fantasy Points')
plt.title('Fanatsy Points By Football Stars the Past 4 Years')
plt.axis([2015, 2018, 0, 500])
plt.grid(True)
plt.legend()
plt.show()

