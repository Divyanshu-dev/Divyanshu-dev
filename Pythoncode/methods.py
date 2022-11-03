class Student:
    cname='IIT K'
    def __init__(self,name,rollno) -> None:
        self.name=name
        self.rollno=rollno

    def display(self):
        print(self.name)     #instance method 
        print(self.rollno)


    # @classmethod
    def getCollege(cls):
        print(cls.cname) # class method

    def displyAvg(self):
        x=10
        y=11 # static method
        print(x+y/2)

s=Student('div',105)
s.display()
Student.getCollege()
s.getCollege()
# s.displyAvg()