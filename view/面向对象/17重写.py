'''
成员继承：子类继承了父类除构造方法之外的所有成员
方法重写：子类可以重新定义父类中的方法，这样就会覆盖父类的方法，也称为“重写”
'''

class Person:
    def __init__(self, name, age):
        self.name = name   # 实例属性
        self.__age = age   # 私有属性（子类继承了但是不能直接用）
    def say_age(self):
        print("我的年龄是:",self.__age)
    def say_name(self):
        print("我的名字是:{0}".format(self.name))

class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self,name,age)  # 必须显示调用父类初始化方法，不然解释器不会去调用
        self.score = score
    def say_name(self):
        '''重写父类的方法'''
        print("报告首长，我的名字是{0}".format(self.name))

s = Student("李华",8,90)
s.say_age()
s.say_name()