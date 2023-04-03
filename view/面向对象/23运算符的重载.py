class Person:
    def __init__(self,name):
        self.name = name

    def __add__(self, other):
        if isinstance(other,Person):
            return "{0}--{1}".format(self.name,other.name)
        else:
            return "不是同类对象，不能相加"
    def __mul__(self, other):
        if isinstance(other,int):
            return self.name*other
        else:
            return "不是同类对象，不能相乘"
p1 = Person("张麻子")
p2 = Person("王老六")
p3 = "haha"
s = p1 + p2
print(s)
print(p1 + p3)
print(p1*3)
print(p1*'3')
