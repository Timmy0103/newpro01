def printMax(a, b):
    '''实现两个数的比较，并返回较大的之'''
    if a > b:
        print(a, "较大值")
    else:
        print(b, "较大值")


printMax(10, 20)
printMax(30, 5)
'''
上面的printMax函数中，在定义是写的printMax(a,b)。a和b称为“形式参数”，简称“形参”。
也就是说，形式参数是在定义函数时使用的。形式参数的命名只要符合“标识符”命名规则即可。
在调用函数时，传递的参数称为“实际参数”，简称“实参”。上面代码中，printMax(10,20),10和20就是实参。
'''

# 调用help(函数名.__doc__)可以打印输出函数的文档字符串
help(printMax.__doc__)

