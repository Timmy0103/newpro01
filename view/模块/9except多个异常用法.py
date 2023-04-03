# 使用元组存储多个异常时，多个异常之间没有顺序要求
a = input("请输入被除数:")
b = input("请输入除数:")
try:
    a = int(a)
    b = int(b)
    c = a // b   # 求商
    print("商是：{0}".format(c))
except (Exception, ValueError, ZeroDivisionError) as e:
    print(type(e))
    print(e.args)
    print("遇到异常")
