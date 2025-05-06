from collections import namedtuple

Student = namedtuple('Student', ['name','age','grades'])

student1 = Student('Liza', 22, 89)
student2 = Student('Ved', 23, 88)

print(student1.age)
print(student2._asdict())