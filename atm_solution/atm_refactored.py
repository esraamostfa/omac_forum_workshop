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

	if request <= balance:
		give_banknote(request)
	
	elif request < 0:
		print("More than zero plz!")

	else:
		print("You don't have enough money!")

	balance-= request
	return "Current balance = " + str(balance)

print(withdraw(balance, int(input("How many money  do you need? "))))