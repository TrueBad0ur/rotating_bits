# 
#		Made by truebad0ur for mostly personal usage
#
#		------------------Examples------------------
#
#		ror 2 bits:		31 -> 11111 -> 00011111 -> 11000111 -> 199
#		rol 2 bits:		31 -> 11111 -> 00011111 -> 01111100 -> 124
#
#
#		PS> python.exe main.py
#		PS> Enter number to rotate: 31
#		PS> Y wanna ROL[L] or ROR[R]: R
#		PS> Enter for how many bits rotate your number: 2
#		PS> Automatic[A] or Manual[M] bits: A
#		PS> 199
#		
#		PS> python.exe main.py
#		PS> Enter number to rotate: 31
#		PS> Y wanna ROL[L] or ROR[R]: R
#		PS> Enter for how many bits rotate your number: 2
#		PS> Automatic[A] or Manual[M] bits: M
#		PS> Enter how many bits is your number: 8
#		PS> 199
#
#		PS> Enter number to rotate: 31
#		PS> Y wanna ROL[L] or ROR[R]: L
#		PS> Enter for how many bits rotate your number: 2
#		PS> Automatic[A] or Manual[M] bits: A
#		PS> 124
#
#		PS> Enter number to rotate: 31
#		PS> Y wanna ROL[L] or ROR[R]: L
#		PS> Enter for how many bits rotate your number: 2
#		PS> Automatic[A] or Manual[M] bits: M
#		PS> Enter how many bits is your number: 8
#		PS> 124

class Solver:
    def __init__(self, number, bits_to_rotate):
        self.number = number
        self.bits_to_rotate = bits_to_rotate

        s = input("Automatic[A] or Manual[M] bits: ")

        if s == "A":
            tmp = len(bin(self.number)[2:])
            if (tmp > 0 and tmp <= 8):
                self.bits = 8
            elif (tmp > 8 and tmp <= 16):
                self.bits = 16
            elif (tmp > 16 and tmp <= 32):
                self.bits = 32
            elif (tmp > 32 and tmp <= 64):
                self.bits = 64
            else:
                print("Smth is wrong with your number!")
                exit(0)
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
        x = "0" * (bits % len(str(x))) + str(x)
        x = x[len(x) - bits_to_rotate:len(x) + 1] + x[0:len(x) - bits_to_rotate]
        x = int(x, 2)
        return x

    def rol(self):
        number = self.number
        bits_to_rotate = self.bits_to_rotate
        bits = self.bits

        x = bin(number)[2:]
        x = "0" * (bits % len(str(x))) + str(x)
        x = x[bits_to_rotate:len(x) + 1] + x[0:bits_to_rotate]
        x = int(x, 2)
        return x


if __name__ == "__main__":
    number = int(input("Enter number to rotate: "))
    rol_ror = input("Y wanna ROL[L] or ROR[R]: ")

    if rol_ror != "R" and rol_ror != "L":
        print("Smth went wrong!")
        exit(0)

    bits_to_rotate = int(input("Enter for how many bits rotate your number: "))
    test = Solver(number, bits_to_rotate)

    if rol_ror == "L":
        print(test.rol())
    if rol_ror == "R":
        print(test.ror())
