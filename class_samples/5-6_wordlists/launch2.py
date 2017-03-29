# myGrades.txt contains the following lines:
# Biology 95
# History 85
# CS 99

myFile = open('myGrades.txt', 'r')

myGradeLine = myFile.readline()
while myGradeLine != '':
	myData = myGradeLine.split()
	print("My " + myData[0] + " grade is a " + myData[1] + ".")
	myGradeLine = myFile.readline()
	
