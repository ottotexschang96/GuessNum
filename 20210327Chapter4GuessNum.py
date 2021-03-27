import random
r = random.randint(1,100)
count = 0

while True:
	count += 1 #this is equal to count = count + 1
	number = input('Please input your number:')
	if int(number) == r:
		print('You are right!')
		print('This is your', count, 'time(s) trial')
		break
	elif int(number) > r:
		print('Number is bigger than answer')
	elif int(number) < r:
		print('Number is smaller than answer')
	print('This is your', count, 'time(s) trial')