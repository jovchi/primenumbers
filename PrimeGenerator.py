""" Output prime numbers up to a given number
"""
import math

class PrimeGenerator(object):
    prime_num = []

    def __init__(self):
        pass

    # checks if given number is prime
    def is_prime(self, num):

        valid = False

        if num < 2:
            return valid

        i = int(math.sqrt(num) + 1)

        while (num % i) != 0:
            i -= 1

        if i == 1:
            valid = True

        return valid

    def run(self):
        limit = input("Please input a number: ")
        empty_string = ""

        # checks if input is a number and not empty
        try:
            x = int(limit)
        except ValueError:
            print "Sorry, your input was not a number"
            return

        if (x >= 2):
            self.prime_num.append(2)

        for y in range(1,x+1,2):
            if self.is_prime(y):
                self.prime_num.append(y)

        print (" ".join(str(e) for e in self.prime_num))







    







	

