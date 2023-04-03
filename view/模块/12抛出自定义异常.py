'''
1、自定义异常
class 自定义异常(BaseException):
    def __init__(self):
        pass
2、抛出自定义异常
    raise 异常对象

定义一个学生类，私有属性gender，提供对应的设置值以及访问值的方法
'''
# 定义一个异常类
class GenderException(BaseException):
    def __init__(self):
        super().__init__()
        self.errMsg = "性别只能设置成'男'或'女'"
class Student():
    def __init__(self, name, gender):
        self.name = name
        # self.__gender = gender
        self.setGender(gender)
    #设置性别
    def setGender(self,gender):
        if gender == '男' or gender =='女':
            self.__gender = gender
        else:
            # 抛出异常（性别异常）
           raise GenderException()
    #获取性别
    def getGender(self):
        return self.__gender

    def showInfo(self):
        print("我叫{0}，我的性别是{1}".format(self.name,self.__gender))

try:
    stu = Student("张利", "男同")
except BaseException as e:
    print(type(e))
    print(e.args)
    print(e.errMsg)

# try:
#     stu.setGender("男男")
# except BaseException as e:
#     print(type(e))
#     print(e.args)
#     print(e.errMsg)

# stu.showInfo()