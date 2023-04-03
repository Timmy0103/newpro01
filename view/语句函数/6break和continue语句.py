# break语句可用于while和for循环，用于结束整个循环。当有嵌套循环时，break语句只能跳出最近一层的循环。
while True:
    a = input("请输入一个字符（输入Q或者q结束）：")
    if a.upper() == "Q":  # if a == 'q' or a == "Q":
        print("循环结束，推出程序")
        break
    else:
        print(a)

# continue语句用于结束本次循环，继续下一次。多个循环嵌套时，continue也是应用于最近的一层循环。

'''输入员工的薪资，若薪资小于0则重新输入。最后打印出录入员工的数量、薪资和平均薪资'''
empNum = 0
salarySum = 0
salarys = []
while True:
    s = input("请输入员工的薪资（输入Q或q，结束）：")
    if s.upper() == 'Q':
        print("结束")
        break
    if float(s) < 0:
        continue
    empNum += 1
    salarys.append(float(s))
    salarySum += float(s)
print("员工数{0}".format(empNum))
print("员工薪资:", salarys)
print("平均工资{0}".format(salarySum/empNum))

