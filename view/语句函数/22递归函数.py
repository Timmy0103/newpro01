# 递归函数指的是：自己调用自己的函数，在函数体内部直接或者间接的自己调用自己
'''
每个递归函数必须包含两个部分：
1、终止条件：表示递归什么时候结束，一般用于返回值，不在调用自己
2、递归步骤：把第n步的值和第n-1步相关联
'''
def test01(n):
    print("test01:", n)
    if n == 0:
        print("over")
    else:
        test01(n-1)
    print("test01****:",n)

test01(5)

# 使用递归函数计算阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
result = factorial(5)
print(result)

m = 1
for i in range(5, 0, -1):
    m *= i
print(m)

# 分形几何


