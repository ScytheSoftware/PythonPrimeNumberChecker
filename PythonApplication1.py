#Prime numbers in Python


# take input from the user
num = int(input("Enter a number to check if it's prime: "))

# prime numbers are greater than 1
if num > 1:
	for i in range(2,num):  #it's not (1,num) because that's prime. so start checking numbers higher than 2
		if (num % i) == 0:
			print(num,"is not a prime number")
			print(i,"times",num//i,"is",num)
			break
	else:
		print(num,"is a prime number")

else: #This will print if the number isn't prime
   print(num,"is not a prime number")