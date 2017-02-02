
class Student(object):
    """ Encapsulates a Student and their gpa & college app list. """
    
    collegeList = []
    
    def __init__(self, name, gpa, fave_snack):
        self.name = name
        self.gpa = gpa
        self.fave_snack = fave_snack
        
    def getSnack(self):
        """ Returns student's favorite snack. """
        return self.fave_snack
 
    def getShortSummary(self):
        summary = "The student name is " + self.name + " and he/she has a " + str(self.gpa) + "."
        return summary
        
    def getColleges(self):
      return self.collegeList
      
    def addCollege(self, collegeName):
      self.collegeList.append(collegeName)
      
    def getGPA(self):
      return self.gpa
      
    def getLongSummary(self):
      summary = self.getShortSummary()
      summary = summary + " His/her favorite snack is " + self.fave_snack + ". He/she is applying to the following schools: " + str(self.collegeList)
      return summary
      
      
   # to implement:
   # 1) a getGPA() method that returns the float for gpa
   # 2) a getLongSummary() method that returns a summary that includes the student's favorite snack and the list of colleges the student has applied to
   # 3) an addCollege(collegeName) method that allows the user to add a college to the list of colleges the student has applied to
   # 4) a getColleges() method that returns the list of colleges she's applying to


  
# make a student, test methods
myFirstStudent = Student("Jenny", 4.0, "carrots")
print(myFirstStudent.getSnack())

# make another student, test methods for both
mySecondStudent = Student("Kelvin", 3.9, "Takis")
print(mySecondStudent.getShortSummary())
print(myFirstStudent.getShortSummary())



    
# test the new functions
myFirstStudent.addCollege("Stanford")
myFirstStudent.addCollege("Duke")
mySummary = myFirstStudent.getLongSummary()
print(mySummary)


 
