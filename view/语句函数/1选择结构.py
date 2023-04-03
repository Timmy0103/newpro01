# print('fighting')
# 双分支选择结构
num = input("请输入数字：")
if int(num) < 10:
    print(num)
else:
    print("数字太大")
''' 三元条件运算符：
    条件为真时的值 if (条件表达式) else 条件为假时的值'''
num = input("请输入一个数字：")
print("{0}是大于10的数字".format(num) if int(num) > 10 else "数字太小")

# 多分支结构
score = int(input("请输入分数："))
grade = ''
if score < 70:
    grate = "成绩一般"
elif 70 <= score <= 80:
    grate = '还可以'
elif 90 >= score > 80:
    grate = '挺好'
else:
    grate = '太棒了'

print('分数是{0}，等级是{1}'.format(score, grate))

# 练习：打印坐标（x，y）的象限
x = int(input('请输入x坐标:'))
y = int(input('请输入y坐标:'))
if x == 0 and y == 0:
    print("原点")
elif x == 0:
    print("Y轴")
elif y == 0:
    print("X轴")
elif x > 0 and y > 0:
    print('第一象限')
elif x > 0 and y < 0:
    print("第二象限")
elif x < 0 and y < 0:
    print('第三象限')
else:
    print("第四象限")
    pass



