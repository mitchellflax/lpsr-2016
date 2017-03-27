class Cat(object):
	def __init__(self, name):
		self.name = name
		self.lives = 9

	def fallOffCounter(self):
		self.lives  = self.lives - 1

	def getSummary(self):
		report = self.name + " has " + str(self.lives) + " lives."
		return report

myCat = Cat("Sheldon")
myCat.fallOffCounter()
myCat.fallOffCounter()
print(myCat.getSummary())
		
