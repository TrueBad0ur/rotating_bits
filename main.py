class Solver:
	def __init__(self, number, bits):
		self.number = number
		self.bits = bits

	def ror8(self):
		number = self.number
		bits = self.bits
		x = bin(number)[2:]
		x = "0"*(8%len(str(x)))+str(x)
		x = x[len(x)-bits:len(x)+1]+x[0:len(x)-bits]
		x = int(x, 2)
		return x

	def ror16(self):
		return str(self.number) + " " + str(self.bits)

	def ror32(self):
		return str(self.number) + " " + str(self.bits)

	def ror64(self):
		return str(self.number) + " " + str(self.bits)

if __name__ == "__main__":
	test = Solver(31, 2)
	print(test.ror8())
	