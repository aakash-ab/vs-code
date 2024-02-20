class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("hello from user")


class Student(User):
    pass

class Teacher(Student):
    def __init__(self, name, age):
        super().__init__(name,age)
        # self.name = name
        # self.age = age
        print("Hello")


teacher = Teacher("abc",20)




with open('example.txt',"w") as f:
    f.write('hello-world')

f = open("example.txt","r")
f_content = f.read()
print(f_content)
f.seek(0)

f_new = f.read()
print(f_new)









