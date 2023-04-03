'''
设计模式是面向对象特有的内容，是我们在面临某一类问题时候固定的做法，设计模式有很多种，比较流行的是：GOF23种设计模式。
对于初学者，我们学习两种最常见的模式：工厂模式和单例模式
工厂模式实现了创建者和调用者的分离，使用专门的工厂类将选择实现类、创建对象进行统一的管理和控制
'''
# 工厂模式
class CarFactory:
    def create_car(self,brand):
        if brand =="奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

factory = CarFactory()
c1 = factory.create_car("奔驰")
c2 = factory.create_car("比亚迪")
c3 = factory.create_car("大众")
print(c1)
print(c2)
print(c3)
