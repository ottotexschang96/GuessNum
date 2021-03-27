import random
r = random.randint(1,100)
while True:
	number = input('Please input your number:')
	if int(number) == r:
		print('You are right!')
		break
	elif int(number) > r:
		print('Number is bigger than answer')
	elif int(number) < r:
		print('Number is smaller than answer')