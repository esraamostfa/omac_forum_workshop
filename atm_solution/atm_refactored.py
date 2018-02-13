balance = 500

def give_banknote(request):

	banknotes = [100, 50, 10, 5, 1]
	withdraw = request

	for banknote in banknotes:
		while withdraw >= banknote:
				print ("give " + str(banknote))
				withdraw-= banknote
	

def withdraw(balance, request):
	new_balance = balance
	print("Current balance = " + str(new_balance)) 
	
	if request < 0:
		print("More than zero plz!")

	elif request > balance:
		print("You don't have enough money!")

	else:
		balance-=request
		give_banknote(request)

	return balance


balance = withdraw(balance, 280)
balance = withdraw(balance, 150)
