class Person:    # 默认继承object类

    def __init__(self, name):
        self.name = name   # 实例属性

    def __str__(self):
        return "名字是：{0}".format(self.name)

s = Person("李华")
print(s)