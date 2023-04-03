'''
多个异常时，使用顺序为：子类在前父类在后
'''
a = input("请输入被除数:")
b = input("请输入除数:")
try:
    a = int(a)
    b = int(b)
    c = a // b   # 求商
    print("商是：{0}".format(c))
except ValueError:
    print("数据类型不正确")
except ZeroDivisionError:
    print("除数不能为0")
except Exception:   # 最后必须放一个Exception或BaseException，防止漏掉未发现的异常情况
    print("其他异常")
