class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self, name, age,marks):
        super().__init__(name, age)
        self.marks=marks

    def display(self):
        super().display()
        print(self.marks)

class Employee (Person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary=salary

    def display(self):
        super().display()
        print(self.salary)

s=Student('rida',23,120)
s.display()
