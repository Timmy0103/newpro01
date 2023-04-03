# 嵌套函数：在函数内部定义的函数（内部函数）
def outer():
    print("outer running")
    def inner():
        print("inner running")
    inner()
outer()
#inner()
'''
一般在什么情况下使用嵌套函数？
1、封装-数据隐藏：外部无法访问“嵌套函数”
2、贯彻DRY（Don't Repeat Yourself）原则：嵌套函数可以让我们在函数内部避免重复代码
3、闭包'''

def printChineseName(name, familyName):
    print("{0} {1}", format(familyName, name))
def printEnglishName(name, familyName):
    print("{0} {1}", format(name, familyName))

def printName(isChinese, name, familyName):
    def inner_print(a, b):
        print("{0} {1}".format(a, b))
    if isChinese:
        inner_print(familyName, name)
    else:
        inner_print(name, familyName)
printName(True,"磊","张")
printName(False,"Ivanka","Turmp")