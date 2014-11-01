

limit=input("Please input a number: ")
empty_string=""

# checks if input is a number and not empty
while not limit.isdigit() or limit==empty_string:
	limit=input("Sorry, wrong input. Try again: ")


x=int(limit)

# checks if given number is prime
def is_prime(num):
	
	valid=False 
	
	if num<2:
		return valid

	i=num-1

	while (num%i)!=0:
		i=i-1
	
	if i==1:
		valid=True

	return valid
	
prime_num=[]


for y in range(x):
	if is_prime(y):
		prime_num.append(y)


print (" ".join(str(e) for e in prime_num))







    







	

