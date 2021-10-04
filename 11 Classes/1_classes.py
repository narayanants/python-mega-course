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


class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks 

    def myMarks(self):
        print(' You scored this', self.marks)


p1 = Student('Narayanan',29,90)
print(p1.myMarks())


class Person(Student):
    def __init__(self, name, age, marks):
        super().__init__(name, age, marks)

p2 = Person('Girija',53,99)
print(p2.myMarks())
