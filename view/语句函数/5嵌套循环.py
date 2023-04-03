# 一个循环体内可以嵌入另一个循环
for x in range(5):
    for y in range(5):
        print(x, end="\t")
    print("\n")  # 起到换行作用
    pass
# 打印九九乘法表
for m in range(1, 10):
    for n in range(1, m+1):
        print("{0}*{1}={2}".format(m, n, (m*n)), end="\t")
    print()
# 使用列表和字典存储表格的数据
r1 = dict(name="高小一", age=18, salary=10000)
r2 = dict(name="高小二", age=19, salary=20000)
r3 = dict(name="高小三", age=20, salary=30000)
tb = [r1, r2, r3]
# 打印工资大于15000的列表信息
for x in tb:
    if x.get("salary") > 15000:
        print(x)
