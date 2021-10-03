class Person:
    def __init__(self,age,name):
        self.age = age
        self.name = name
    def myAge(self):
        print('My age is ',self.age)

p1 = Person(29,'Narayanan')
print(p1.age)
print(p1.name)
print(p1.myAge)


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)