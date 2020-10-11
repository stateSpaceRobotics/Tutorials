from MyFraction import MyFraction

def main():
	fraction1 = MyFraction(1,2)
	fraction2 = MyFraction(1,2)

	addResult = fraction1 + fraction2
	print("Addition result was: " + str(addResult) + ". The correct answer is: 1/1 or 2/2")

	#subResult = fraction2 - fraction1
	#print("Subtraction result was: " + subResult + ". The correct answer is: 0/0")

	multResult = fraction1 * fraction2
	print("Multiplication result was: " + str(multResult) + ". The correct answer is: 1/4")

	#divResult = fraction1 / fraction2
	#print("Division result was: " + divResult + ". The correct answer is: 1/1")

main()
