# 将字符串str当成有效的表达式来求值并返回计算结果
# 语法：eval(soure[,globals[,locals]]) -> value
'''
参数：
1、soure：一个python表达式或函数compile()返回的代码对象
2、globals:可选，必须是dictionary
3、locals：可选，任意映射对象
'''

s = "print('abcd')"
eval(s)

a = 10
b = 20
c = eval("a+b")
print(c)

dict1 = dict(a=100, b=200)
d = eval("a+b")
print(d)
d = eval("a+b", dict1)
print(d)
