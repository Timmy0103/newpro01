# @property 可以将一个方法的调用方式改变成“属性调用”

class Employee:
    @property
    def salary(self):
        print("salary run...")
        return 10000

emp1 = Employee()
#emp1.salary()
print(emp1.salary)

class Employee1:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("录入错误！年龄在0-100之间")


'''
    def get_age(self):
        return self.__age

    def set_age(self,age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("录入错误！年龄在0-100之间")
'''
emp2 = Employee1("高乐", 20)
'''
print(emp2.get_age())
emp2.set_age(10)
print(emp2.get_age())
'''
print(emp2.age)
emp2.age = 30   # -30
print(emp2.age)