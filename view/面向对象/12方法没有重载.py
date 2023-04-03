# python中没有方法的重载，定义多个同名方法，只有最后一个有效

class Person:
    def say_hi(self):
        print("hello")
    def say_hi(self,name):
        print("{0},hello".format(name))

p1 = Person()
# p1.say_hi()   #报错TypeError: Person.say_hi() missing 1 required positional argument: 'name'
p1.say_hi("timmy")

# 方法的动态性（方法也是对象，函数也是对象，一切都是对象）
class Person1:
    def work(self):
        print("努力上班")

def play_game(s):
    print("{0}在玩游戏".format(s))

def work2(s):
    print("好好工作，努力赚钱")

Person1.play = play_game
p = Person1()
p.work()
p.play()  # Person1.play(p)
Person1.work = work2
p.work()
