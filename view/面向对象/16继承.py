'''
继承
继承是面向对象程序设计的重要特性，也是实现“代码复用”的重要手段
如果一个新类继承自一个设计好的类，就直接具备了已有类的特性，就大大降低了工作难度。
已有的类，我们称之为“父类或基类”，新的类，我们称之为“子类或派生类”
'''

'''
语法格式
Python支持多重继承，一个子类可以继承多个父类，继承的语法格式如下：
class 子类类名(父类1[,父类2,...]);
    类体

如果在类定义中没有指定父类，则默认父类是object类，也就是说，object是所有类的父类，
里面定义了一些所有类共有的默认实现，比如：__new__()
定义子类时，必须在其构造函数中调用父类的构造函数，调用格式如下：
父类名.__init__(self,参数列表)
'''

class Person:
    def __init__(self, name, age):
        self.name = name   # 实例属性
        self.__age = age   # 私有属性
    def say_age(self):
        print(self.name,"的年龄是:",self.__age)
p = Person("高崎",18)
p.say_age()


class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self,name,age)  # 必须显示调用父类初始化方法，不然解释器不会去调用
        self.score = score
s = Student("李华",8,90)
s.say_age()
print(s.name)
print(s._Person__age)
print(dir(s))
print(Student.mro())  # Student——>Person——>object类