import turtle

t = turtle.Pen()
# my_color = ("black", "blue", "red", "green", 'pink', "yellow")
# t.width(5)
# t.speed(15)
# for i in range(20):
#     t.penup()
#     t.goto(0, -i*10)
#     t.pendown()
#     t.color(my_color[i % len(my_color)])
#     t.circle(10+i*10)
# turtle.done()  # 执行完程序，窗口不关闭

# 画一个18*18的棋盘
t.speed(15)
for n in range(18):
    t.penup()
    t.goto(-300, 300-n*20)
    t.pendown()
    t.goto(40, 300-n*20)
for m in range(18):
    t.penup()
    t.goto(-300+m*20, 300)
    t.pendown()
    t.goto(-300+m*20, -40)
turtle.done()  # 执行完程序，窗口不关闭
