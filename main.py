class Solver:
	def __init__(self, number, bits):
		self.number = number
		self.bits = bits

	def ror8(self):
		return str(self.number) + " " + str(self.bits)

	def ror16(self):
		return str(self.number) + " " + str(self.bits)

	def ror32(self):
		return str(self.number) + " " + str(self.bits)

	def ror64(self):
		return str(self.number) + " " + str(self.bits)

if __name__ == "__main__":
	test = Solver(10, 2)
	print(test.ror8())
	print(test.ror16())
	print(test.ror32())
	print(test.ror64())
	