# prints the multiples of a user-given # up to 1000

print('For what number would you like multiples?')
num = float(raw_input())

multiple = 0
product = 0

while product < 1000:
	product = multiple * num
	print(str(multiple) + " times " + str(num) + " equals " + str(product))
	multiple = multiple + 1

print('Those are all of the multiples up to 1000! Have a nice day.') 
