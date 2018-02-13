balance = 500

def give_banknote(request):

	banknotes = [100, 50, 10, 5, 1]
	withdraw = request

	for banknote in banknotes:
		while withdraw >= banknote:
				print ("give " + str(banknote))
				withdraw-= banknote
	

def withdraw(balance, request):
	print("Current balance = " + str(balance)) 
	
	if request < 0:
		print("More than zero plz!")

	elif request > balance:
		print("You don't have enough money!")

	else:
		give_banknote(request)

	balance-= request
	return "Current balance = " + str(balance)

print(withdraw(balance, int(input("How many money  do you need? "))))