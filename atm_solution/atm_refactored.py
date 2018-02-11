balance = 500

def withdraw(balance, request):
	print("Current balance = " + str(balance)) 

	banknotes = [100, 50, 10, 5, 1]
	withdraw = request

	if request <= balance:
		for banknote in banknotes:
			while withdraw >= banknote:
				print ("give " + str(banknote))
				withdraw-= banknote
	
	elif request < 0:
		print("More than zero plz!")

	else:
		print("You don't have enough money!")

	balance-= request
	return "Current balance = " + str(balance)

print(withdraw(balance, int(input("How many money  do you need? "))))
