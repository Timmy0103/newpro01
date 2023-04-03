'''
1、模块介绍
Python 模块（Module），是一个Python文件，以.py结尾，包含了Python对象定义和Python语句
模块让你能够有逻辑地组织你的Python代码段
把相关的代码分配到一个模块里让你的代码更好用，更易懂
模块能定义函数、类和变量，模块里也能包含可执行代码
2、模块使用
模块的引入
import module1[,mmodule2,....moduleN]
'''
PI = 3.14
def get_area(r):
    '''
    求圆的面积
    :param r: 半径
    :return: 圆的面积
    '''
    return [r,PI * r ** 2]
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_info(self):
        '''
        展示学生信息
        :return: None
        '''
        print("name:{0},age:{1}".format(self.name,self.age))
print(PI)
print(get_area(2))
print("半斤为{0}的圆的面积为{1}".format(get_area(2)[0],get_area(2)[1]))
stu = Student("张飞",31)
stu.show_info()