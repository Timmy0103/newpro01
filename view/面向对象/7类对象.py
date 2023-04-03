# 类定义格式中，“class 类名:”。实际上，当解释器执行class语句时，就会创建一个类对象
class Student:
    pass

print(type(Student))    # 执行结果为<class'type'>    type为模具类
print(id(Student))

Stu2 = Student
s1 = Stu2()
print(s1)