'''while、for循环可以附带一个else语句（可选），如果for、while语句没有被break语句结束，
则会执行else子句，否则不执行。 '''
# 员工4人，录入他们的薪资，全部录入后，打印提示“您已经全部录入4名员工的薪资”。打印输出录入的薪资和平均薪资
salarySum = 0
salarys = []
for i in range(4):
    s = input("请依次输入4名员工的薪资（输入Q或q结束）：")
    if s.upper() == 'Q':
        print("录入结束")
        break
    if float(s) < 0:
        continue
    salarys.append(float(s))
    salarySum += float(s)
else:
    print("您已经全部录入4名员工的薪资")
print("录入薪资：",salarys)
print("平均薪资{0}".format(salarySum/4))
