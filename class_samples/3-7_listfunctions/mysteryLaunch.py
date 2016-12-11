print("What number would you like to test?")
n = int(raw_input())
div_num = 2

while div_num < n:
	if n % div_num == 0:
		print('Nope, it\'s not.')
		exit()
	div_num = div_num + 1

# if we get this far without exiting...
print('Yup, it is!')

# 1: Be the computer and run this for the numbers 5 and 6. What does it output in each case?
# 2: What do you think this program is for? Explain it in words.
