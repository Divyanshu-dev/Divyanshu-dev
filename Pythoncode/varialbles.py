from operator import methodcaller
from tkinter import Variable

from django.template import VariableDoesNotExist


# '''Type of Variable
#1 instance variable ,local variable, static variable

class Student():
    cName='IITK' #static variable
    def __init__(self,Name,RollNo):
        self.RollNo=RollNo #instance variable
        self.Name=Name
    def display(self):
        teamName='Red House'#local Variable
        print("Method Execution")
        print(self.Name,teamName)
        print(self.RollNo)

s=Student('Divyanshu',1000)
print(s.cName)
print(s.Name,s.RollNo)
s.display()