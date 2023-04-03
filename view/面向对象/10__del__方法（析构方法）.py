'''
__del__方法称为“析构方法”，用于实现对象被销毁时所需的操作。释放对象占用的支援
例如：打开的文件资源、网络连接等
Python实现自动的垃圾回收，当对象没有被引用（引用计数为0），由垃圾回收器调用__del__方法
我们也可以通过del语句删除对象，从而保证调用__del__方法
系统会自动提供__del__方法，一般不需要自定义析构方法
'''

# 析构函数
class Person:
    def __del__(self):
        print("销毁对象：{0}".format(self))

p1 = Person()
p2 = Person()
del p2
print("程序结束")
