'''编写循环时，遵循下面三个原则可以大大提高运行效率，避免不必要的低效计算：
1、尽量减少循环内部不必要的计算
2、嵌套循环中，尽量减少内层循环的计算，尽可能向外放
3、局部变量查询较快，计量使用局部变量'''
# 链接多个字符串，使用join()而不使用+
# 列表进入元素查询和删除，尽量在列表尾部操作
import time
start = time.time()
for i in range(1000):
    result = []
    for m in range(10000):
        result.append(i*1000+m*100)
end = time.time()
print("耗时：{0}".format(end - start))

start1 = time.time()
for i in range(1000):
    result = []
    c = i*1000  # 优化了计算
    for m in range(10000):
        result.append(c+m*100)
end1 = time.time()
print("耗时：{0}".format(end1 - start1))
