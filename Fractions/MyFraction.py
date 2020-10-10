class MyFraction:
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def __str__(self):
		return self.numerator + "/" + self.denominator

	def __add__(self, fraction):
		answer = "Calculate the answer. The answer will be a fraction"
		return answer

	def __sub__(self, fraction):
		answer = "Calculate the answer. The answer will be a fraction"
		return answer

	def __mul__(self, fraction):
		answer = "Calculate the answer. The answer will be a fraction"
		return answer

	def __truediv__(self, fraction):
		newNum = self.numerator * fraction.denominator
		newDen = self.denominator * fraction.numerator
		if (newNum == newDen):
			answer = MyFraction(1,1)
		else:
			answer = MyFraction(newNum, newDen)
		return answer
