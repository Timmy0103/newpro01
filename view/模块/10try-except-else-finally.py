'''
try:
except 异常 as 变量：
else：
    没有异常，执行的代码
finally：
    最终一定要执行的代码
'''
# 案例：将一些字符串数据写入到文件中
try:
    file = open('123.txt', 'w', encoding="utf-8")
    file.write('Hello-')
    file.write('World')
    # write只能将字符串数据写入到文件中
#    file.write([1, 2, 3])
    print("写入完毕")
except Exception as e:
    print(e.args)
    print("写入的数据存在异常")
else:
    print("写入的数据不存在异常")
finally:
    #最后一定要执行的代码
    # 关闭文件
    file.close()
    print("关闭文件，谢谢使用")