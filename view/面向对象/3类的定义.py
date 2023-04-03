'''
定义类的语法格式如下：
Class 类名:
    类体
要点如下：
1、类名必须符合“标识符”的规则：一般规定，首字母大写，多个单词使用“驼峰原则”
2、类体中我们可以定义属性和方法
3、属性用来描述数据，方法（即函数）用来描述这些数据的相关操作
'''

class Student:  # 类名一般首字母大写，多个单词采用驼峰原则
    def __init__(self, name, score):  # self必须位于第一个参数
        self.name = name     # 实例属性
        self.score = score

    def say_score(self):   # self必须位于第一个参数   # 实例方法
        print("{0}的分数是{1}".format(self.name, self.score))

s1 = Student("高崎", 80)
s1.say_score()
s1.name = "haha"
s1.age = 28
s1.say_score()

s2 = Student("高希希", 100)
s2.say_score()
Student.say_score(s2)    # 实例对象的方法调用本质

print(dir(s2))

print(s2.__dict__)

print(isinstance(s2, Student))
