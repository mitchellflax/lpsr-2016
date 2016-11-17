# Ms. Nolan's advisor rating goes up each time she gives an advisee a compliment.
# It stops rising when she doesn't give any compliments. :(
compliments = 1000
rating = 0

while compliments != 0:
	print('How many compliments has Ms. Nolan given you today?') 	
	compliments = int(raw_input())
	rating = rating + (compliments * 10)
	print('Ms. Nolan\'s rating is now ' + str(rating))


