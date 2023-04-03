'''
类属性
类属性是从属于“类对象”的属性，也称之为“类变量”，由于，类属性从属于类对象，可以被所有实例对象共享
类属性的定义方式：
class 类名:
    类变量名 = 初始值
在类中或者类的外面，我们可以通过：“类名.类变量名”来读取
'''

class Student:
    company = "SXT尚学堂"   # 类属性
    count = 0         # 类属性

    def __init__(self, name, score):
        self.name = name             # 实例属性
        self.score = score
        Student.count = Student.count+1

    def say_scoer(self):             # 实例方法
        print("我的公司是:", Student.company)
        print(self.name, "的分数是:", self.score)

s1 = Student("张三", 90)     # s1是实例对象，自动调用__init__()方法
s1.say_scoer()
print('一共创建{0}个Student对象'.format(Student.count))
s2 = Student("李四", 91)
Student.say_scoer(s2)
print('一共创建{0}个Student对象'.format(Student.count))
