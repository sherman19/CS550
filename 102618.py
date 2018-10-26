class Bank():
	#constructor
	#initializes properties
	def__init__(self, balance, PIN, name, accountnumber, money):
		self.balance = balance
		self.PIN = PIN
		self.name = name
		self.accountnumber = accountnumber
		self.money = money

#methods/functions
	
	def withdraw(self, balance, money):
		status = ""
		if balance > 0:
			self.balance -= money
			status = self.name+"just took money from the account."
		elif money > balance:
			print("You do not have that much money to take out.")
		else:
			status = self.name+"did not take out or add money."
		return status

	def deposit(self, balance, money):
		status = ""
		if balance > 0:
			self.balance += money
			status = self.name+"just added money to the account."
		else:
			status = self.name+"did not take out or add money."
		return status

	def stats(self):
		return "Name: "+self.name+"\nbalance: "+str(self.balance)+"\nPIN: "+str(self.PIN)

	def PIN(self):
		status = ""
		return status

bankPIN = input("What is your PIN?")
