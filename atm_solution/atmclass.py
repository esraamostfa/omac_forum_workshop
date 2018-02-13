class ATM:
	def __init__(self, balance, bank_name):
		self.balance = balance
		self.bank_name = bank_name

	def give_banknote(request):

		self.request = request
		self.banknotes = [100, 50, 10, 5, 1]
		self.withdraw = self.request

		for self.banknote in self.banknotes:
			while self.withdraw >= self.banknote:
				print ("give " + str(self.banknote))
				self.withdraw-= self.banknote
		 
	def withdraw(self, request):
		self.request = request

		print("Welcome to "+ self.bank_name)
		print("Current balance = " + str(self.balance))

		if self.request < 0:
			print("More than zero plz!")

		elif self.request > self.balance:
			print("You don't have enough money!")

		else:
			self.give_banknote()
			
		self.balance-= self.request
		#return "Current balance = " + str(balance)

balance1 = 500
balance2 = 1000
		
atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")


atm1.withdraw(int(input("How many money do you need? ")))
atm2.withdraw(int(input("How many money do you need? ")))
