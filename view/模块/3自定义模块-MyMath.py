'''
import 模块
问题：在导入模块的时候，模块中的代码会被执行一遍
解决方案：在自定义模块中新增控制代码：if __name__ == '__main__':测试代码在执行
'''
#import MyMath
x = 100
y = 2
#print("x和y的和是：{0}".format(MyMath.add(x,y)))

from MyMath import add, mul, sub, div
print(add(x, y), mul(x, y), sub(x, y), div(x, y))

