class Solver:
	def __init__(self, number, bits_to_rotate):
		self.number = number
		self.bits_to_rotate = bits_to_rotate

		s = input("Automatic[A] or Manual[M] bits: ")

		if s == "A":
			tmp = len(bin(self.number)[2:])
			if (tmp > 0 and tmp <= 8):
				self.bits = 8
			if (tmp > 8 and tmp <= 16):
				self.bits = 16
			if (tmp > 16 and tmp <= 32):
				self.bits = 32
			if (tmp > 32 and tmp <= 64):
				self.bits = 64
		elif s == "M":
			s = int(input("Enter how many bits is your number: "))
			self.bits = s
		else:
			exit(0)

	def ror(self):
		number = self.number
		bits_to_rotate = self.bits_to_rotate
		bits = self.bits

		x = bin(number)[2:]
		x = "0"*(bits%len(str(x)))+str(x)
		x = x[len(x)-bits_to_rotate:len(x)+1]+x[0:len(x)-bits_to_rotate]
		x = int(x, 2)
		return x

if __name__ == "__main__":
	number = int(input("Enter number to rotate: "))
	bits_to_rotate = int(input("Enter for how many bits rotate your number: "))
	test = Solver(number, bits_to_rotate)
	print(test.ror())
	