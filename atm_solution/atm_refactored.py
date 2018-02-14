class ATM:
	def __init__(self, balance, bank_name):
		self.balance = balance
		self.bank_name = bank_name
		self.withdrawals_list = []

	def give_banknote(self, request, banknotes = [100, 50, 10, 5, 1]):

		for banknote in banknotes:
			while request >= banknote:
				print ("give " + str(banknote))
				request-= banknote		 

	def withdraw(self, request):

		print("Welcome to "+ self.bank_name)
		print("Current balance = " + str(self.balance))

		if request < 0:
			print("More than zero plz!")

		elif request > self.balance:
			print("There is no enough money!")

		else:
			self.give_banknote(request)
			self.withdrawals_list.append(request)
			self.balance-= request

		return self.balance

	def show_withdrawals(self):
		print("withdrawals of " + self.bank_name + ":")

		for self.withdrawal in self.withdrawals_list:
			print(self.withdrawal)


balance1 = 500
balance2 = 1000
		
atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

balance1= atm1.withdraw(277)
balance1= atm1.withdraw(150)

balance2= atm2.withdraw(100)
balance2= atm2.withdraw(250)
balance2= atm2.withdraw(320)

withdrawals1= atm1.show_withdrawals()
withdrawals2= atm2.show_withdrawals()