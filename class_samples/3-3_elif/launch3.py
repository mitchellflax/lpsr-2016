print('How many servings of veggies have you had this week?')
servings_week = float(raw_input())
servings_day = servings_week / 7

if servings_day < 2:
	print('We need to get you some spinach!')
else:
	print('Good job!')

#1: What does this program enter for someone who has had 21 servings of veggies this week?
#2: Why did we use the float() function in line 2?
#3: What is the difference between servings_week and servings_day?

