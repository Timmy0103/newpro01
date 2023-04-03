a = input("请输入被除数:")
b = input("请输入除数:")
# # ValueError: invalid literal for int() with base 10: 'a'
# # ZeroDivisionError: division by zero
# if a.isdigit() and b.isdigit():
#     if int(b) != 0:
#         c = int(a) // int(b)
#         print("商是：{0}".format(c))
#     else:
#         print("除数不能为0")
# else:
#     print("数据类型不正确")
try:
    c = int(a) // int(b)
    print("商是：{0}".format(c))
except:
    print("数据类型不正确/除数不能为0")