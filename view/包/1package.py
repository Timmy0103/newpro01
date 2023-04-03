'''
包的概念：
包是一个分层次的文件目录结构，它定义了一个有模块及子包和子包下的子包等组成的Python的应用环境，
包中要包含一个__init__.py模块
包的作用：
1、将模块归类，方便整理
2、防止模块名冲突
模块中的包名：

包名.模块名
包中的模块如何使用：
1、import 包名.模块名
2、from 包名.模块名 import 变量,函数,类
'''
#import package1.MyMath
from package1.MyMath import sub
from package1.MyMath import mul
x = 100
y = 20
# print(package1.MyMath.add(x,y))
print(sub(x,y))
print(mul(x,y))


