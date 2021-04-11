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

import argparse
import sys


class Solver:
    def __init__(self, number, bits_to_rotate, bits):
        self.number = number
        self.bits_to_rotate = bits_to_rotate
        self.bits = bits

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


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int)
    parser.add_argument('-m', '--manual', type=int, default=0)
    parser.add_argument('-b', '--bitsToRotate', type=int, default=1)
    parser.add_argument('-r', '--ror', choices=['R', 'L'], default='R')

    return parser


def get_bits(number):
    if 0 < number <= 8:
        bits = 8
    elif 8 < number <= 16:
        bits = 16
    elif 16 < number <= 32:
        bits = 32
    elif 32 < number <= 64:
        bits = 64
    else:
        print("Smth is wrong with your number!")
        exit(0)
    return bits


if __name__ == "__main__":
    parser = create_parser()
    if len(sys.argv) > 1:
        namespace = parser.parse_args(sys.argv[1:])
        if namespace.manual == 0:
            bits = get_bits(len(bin(namespace.number)[2:]))
        else:
            bits = namespace.manual

        test = Solver(namespace.number, namespace.bitsToRotate, bits)

        if namespace.ror == "L":
            print(test.rol())
        if namespace.ror == "R":
            print(test.ror())
        else:
            print("Smth went wrong!")
            exit(0)
    else:
        number = int(input("Enter number to rotate: "))
        rol_ror = input("Y wanna ROL[L] or ROR[R]: ")
        rol_ror = rol_ror.upper()

        if rol_ror != "R" and rol_ror != "L":
            print("Smth went wrong!")
            exit(0)

        bits_to_rotate = int(input("Enter for how many bits rotate your number: "))
        s = input("Automatic[A] or Manual[M] bits: ")
        s = s.upper()

        if s == "A":
            bits = get_bits(len(bin(number)[2:]))
        elif s == "M":
            s = int(input("Enter how many bits is your number: "))
            bits = s
        else:
            exit(0)

        test = Solver(number, bits_to_rotate, bits)

        if rol_ror == "L":
            print(test.rol())
        if rol_ror == "R":
            print(test.ror())
