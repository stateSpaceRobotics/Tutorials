class MyFraction:
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def __str__(self):
		return str(self.numerator) + "/" + str(self.denominator)

	def __add__(self, fraction):
		self.sumNum = self.numerator + fraction.numerator
		self.sumDen = self.gcf(self.denominator, fraction.denominator)
		answer = MyFraction(self.sumNum, self.sumDen)
		return answer

	def __sub__(self, fraction):
		answer = "Calculate the answer. The answer will be a fraction"
		return answer

	def __mul__(self, fraction):
		numerator = self.numerator*fraction.numerator
		denominator = self.denominator*fraction.denominator
		gcd = self.gcf(numerator,denominator)
		numerator = numerator // gcd
		denominator = denominator // gcd
		answer = MyFraction(numerator,denominator)
		return answer

	def __truediv__(self, fraction):
		answer = "Calculate the answer. The answer will be a fraction"
		return answer

	def gcf(self, x, y):
		if x > y:
			smaller = y
		else:
			smaller = x
		for i in range(1, smaller + 1):
			if((x % i ==  0) and (y % i == 0)):
				gcf = i
		return gcf

