print('How many cats do you have?')
cats = int(raw_input())

if cats <= 2:
	print('Cool!')
elif cats == 3:
	print('Be careful with all those cats...')
else:
	print('Hmmm, you might be a crazy cat person.')
