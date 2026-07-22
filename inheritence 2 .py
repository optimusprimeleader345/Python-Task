class Person:
    def __init__(self,name,age,contact):
        self.name = name
        self.age = age
        self.contact = contact
    def display(self):
        print(self.name)
        print(self.age)
        print(self.contact)
class Student(Person):
    def __init__(self,name, age, rolls, contact,marks):
        super().__init__(name, age, contact)
        self.rolls = rolls
        self.marks = marks
    def display(self):
        Person.display(self)
        print(self.rolls)
        print(self.marks)
       
s  = Student("steve", 21, 1234567890, 85 , 90)
s.display()