import random

# bring in the file and put them all in a list
myWordsFile = open('words.txt', 'r')
myWordsList = []

currentWord = myWordsFile.readline()
while currentWord != '':
	myWordsList.append(currentWord)
	currentWord = myWordsFile.readline()

# choose a random element from the list
listLen = len(myWordsList)
randElementIndex = random.randint(0,listLen)

# print it for the user
print('Here is a random word!')
print(myWordsList[randElementIndex])
