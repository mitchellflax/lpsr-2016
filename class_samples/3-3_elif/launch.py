print('How many mins did you study?')
mins_studying = int(raw_input())

print('How many minutes did you exercise?')
mins_exercising = int(raw_input())

if mins_studying >= 30 or mins_exercising >= 45:
	print('All right, you can go out with your friends.')
