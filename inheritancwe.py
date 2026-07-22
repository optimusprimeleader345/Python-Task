class Person:
    def _init(self,name,age,contact):
        self.name = name
        self.age = age
        self.contact = contact
    def display(self):
        print(self.name)
        print(self.age)
        print(self.contact)
class student(Person):
    def _init_(self,name, age, contact):
        super()._init_(name, age, contact)
s  = student("steve", 21, 1234567890)
s.name = "steve"
s.age = 21
s.contact = 1234567890
print(s.name)
print(s.age)
print(s.contact)