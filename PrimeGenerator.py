""" Output prime numbers up to a given number
"""

class PrimeGenerator(object):

	prime_num=[]

	def __init__(self):
		pass
	
	# checks if given number is prime
	def is_prime(self, num):
		valid=False 
		
		if num<2:
			return valid

		i=num-1

		while (num%i)!=0:
			i=i-1
		
		if i==1:
			valid=True

		return valid

	def run(self):
		limit=input("Please input a number: ")
		empty_string=""

		# checks if input is a number and not empty
		while not limit.isdigit() or limit==empty_string:
			limit=input("Sorry, wrong input. Try again: ")


		x=int(limit)

	
		for y in range(x):
			if self.is_prime(y):
			   self.prime_num.append(y)


		print (" ".join(str(e) for e in self.prime_num))








    







	

