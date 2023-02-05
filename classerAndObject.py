class Person:
    # contructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # toString
    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)


# inheritance
class Student(Person):
    pass


x = Student("Mike", 24)
print(x.__str__())


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    #thêm hàm init, lớp con sẽ k kế thừa hàm inti của lớp cha
  def __init__(self, fname, lname):
    #Giữ tính kế thừa từ lớp cha
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname,year):
    #kế thừa tất cả thuộc tính và phương thức từ lớp cha
    super().__init__(fname, lname)
    self.year =year

x = Student("Mike", "Olsen",2019)
x.printname()
print(x.year)

