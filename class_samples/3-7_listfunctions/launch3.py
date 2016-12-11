a = 0
my_fave_nums = []

while a < 10000:
	# remember that the % operator gives the remainder of division
	if a % 8 == 0:
		my_fave_nums.append(a)
	a = a + 1

print(my_fave_nums)

# What does this program print?

