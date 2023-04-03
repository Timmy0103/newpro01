'''
自定义一个模块
    实现数学的四则运算
    两个数的加减乘除
'''
# 手动添加全局变量__all__之后，from 模块 import * 将不再是默认导入所有的功能，而是导入__all__列表中包含的功能
__all__ = ["add", "sub", "mul"]
def add(a,b):
    '''
    加法运算
    :return: 两个数的和
    '''
    return a + b
def sub(a,b):
    '''
    减法运算
    :return: 两个数的差
    '''
    return a - b
def mul(a,b):
    '''
    乘法运算
    :return: 两个数的积
    '''
    return a * b
def div(a,b):
    '''
    除法运算
    :return: 两个数的积
    '''
    return a // b
if __name__ == '__main__':
    a = 10
    b = 5
    print("和为：{0}".format(add(a,b)))
    print("差为：{0}".format(sub(a,b)))
    print("积为：{0}".format(mul(a,b)))
    print("商为：{0}".format(div(a,b)))
    print(__name__)  # 执行结果为__main__
