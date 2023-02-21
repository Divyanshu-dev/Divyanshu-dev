class Studen:
    def __init__(self,name,rollNo) -> None:
        print(id(self))
        self.name=name
        self.rollNo=rollNo
#self is a reference variable which is always pointing to the current object.       

t=Studen("div",33)
print(t.id)
print(t.name)