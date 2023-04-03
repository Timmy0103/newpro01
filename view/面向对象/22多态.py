'''
多态（polymorphism）是指同一个方法调用由于对象不同可能会产生不同的行为。
关于多态要注意以下2点：
1、多态是方法的多态，属性没有多态
2、多态的存在有2个必要条件：继承、方法重写
'''

class Animal:
    def shout(self):
        print("动物叫了一声")
class Dog(Animal):
    def shout(self):
        print("小狗，汪汪汪")
class Cat(Animal):
    def shout(self):
        print("小猫，喵喵喵")

def animalshout(m):
    if isinstance(m,Animal):
        m.shout()  # 多态，一个方法调用，根据对象不同调用不同的方法
    else:
        print("哑口无言")
animalshout(Cat())
animalshout(Dog())
animalshout(Dog)
