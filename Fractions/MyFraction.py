class MyFraction:
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def __str__(self):
		return str(self.numerator) + "/" + str(self.denominator)

	def __add__(self, fraction):
		self.sumNum = self.numerator + fraction.numerator
		self.sumDen = self.gcf(self.denominator, fraction.denominator)
		self.sumgcd = self.gcf(self.sumNum,self.sumDen)
		self.sumNum = self.sumNum // self.sumgcd
		self.sumDen = self.sumDen // self.sumgcd
		answer = MyFraction(self.sumNum, self.sumDen)
		return answer

	def __sub__(self, fraction):
		self.subNum = self.numerator*fraction.denominator - self.denominator*fraction.numerator
		self.subDen = self.denominator*fraction.denominator
		self.subgcd = self.gcf(self.subNum ,self.subDen)
		
		if self.subgcd==0:
			return MyFraction(0,0)
		self.subNum  = self.subNum  // self.subgcd
		self.subDen = self.subDen // self.subgcd
		
		answer = MyFraction(self.subNum ,self.subDen)
		return answer

	def __mul__(self, fraction):
		self.mulNum = self.numerator*fraction.numerator
		self.mulDen = self.denominator*fraction.denominator
		self.mulgcd = self.gcf(self.mulNum,self.mulDen)
		
		if self.mulgcd==0:
			return MyFraction(0,0)
		self.mulNum = self.mulNum // self.mulgcd
		self.mulDen = self.mulDen // self.mulgcd
		answer = MyFraction(self.mulNum,self.mulDen)
		return answer

	def __truediv__(self, fraction):
		self.divNum = self.numerator*fraction.denominator
		self.divDen = self.denominator*fraction.numerator
		self.divgcd = self.gcf(self.divNum,self.divDen)
		if self.divgcd==0:
			return MyFraction(0,0)
		self.divNum = self.divNum // self.divgcd
		self.divDen = self.divDen // self.divgcd
		answer = MyFraction(self.divNum,self.divDen)
		return answer

	def gcf(self, x, y):
		if x > y:
			smaller = y
		else:
			smaller = x
		gcd = 0
		for i in range(1, smaller + 1):
			if((x % i ==  0) and (y % i == 0)):
				gcd = i
		return gcd

