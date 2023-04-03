# 选择结构的嵌套
score = int(input('请输入一个0-100之间的分数:'))
grade = ''
if score > 100 or score < 0:
    score = int(input("输入错误，请重新输入一个0-100间的数字:"))
else:
    if score > 90:
        grade = "a"
    elif score > 80:
        grade = 'b'
    elif score > 70:
        grade = 'c'
    elif score > 60:
        grade = 'd'
    else:
        grade = 'e'
    print('分数是{0},等级是{1}'.format(score, grade))

print("**************************************************")
score = int(input('请输入一个0-100之间的分数:'))
grade = 'abcde'
num = 0
if score > 100 or score < 0:
    score = int(input("输入错误，请重新输入一个0-100间的数字:"))
else:
    num = score // 10
    if num < 6:
        num = 5
    print("分数是{0}，等级是{1}".format(score, grade[9-num]))