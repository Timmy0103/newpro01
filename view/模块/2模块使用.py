'''
如何使用模块：
    自定义模块
    1、导入模块：
import 模块名1,模块名2,...模块n
模块名.变量
模块名.函数名(参数)
模块名.类
    2、导入模块中相关的数据，导入后可以直接使用
from 模块 import 变量,函数,类
'''
# 导入模块的方式
# import random
# result = random.randint(1, 9)
# print(result)

# 导入模块中相关数据的方式
from random import randint
result = randint(1, 9)
print(result)
