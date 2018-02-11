

def atm(request):
	money = 500
	banknotes = [100, 50, 10, 5, 1]

	if request <= money:
		for banknote in banknotes:
			while request >= banknote:
				print ("give " + str(banknote))
				request-= banknote
		
	else:
		return "You don't have enough money!"

atm(int(input("How many money  do you need? ")))

