class Student(object):
	""" Encapsulates a Student, their gpa, and college app list. """

	def __init__(self, name, gpa, fave_snack):
		self.name = name
		self.gpa = gpa
		self.fave_snack = fave_snack

		self.collegeList = []
	
	def getSnack(self):
		return self.fave_snack

# code execution starts here
myFirstStudent = Student("Jenny", 4.0, "carrots")
print(myFirstStudent.getSnack())

mySecondStudent = Student("Kelvin", 3.9, "Takis")
print(mySecondStudent.getSnack())
