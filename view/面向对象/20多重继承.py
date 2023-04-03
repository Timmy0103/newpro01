'''
Python 支持多重继承，一个子类可以有多个“直接父类”。这样，就具备了“多个父类”的特点。
但是由于这样会被“类的整体层次”搞的异常复杂，尽量避免使用
'''
class A:
    def aa(self):
        print("aa")
    def say(self):
        print("sayAAA")

class B:
    def bb(self):
        print("bb")
    def say(self):
        print("sayBBB")
class C(B,A):
    def cc(self):
        print("cc")
c = C()
c.cc()
c.bb()
c.aa()
print(C.mro())   # 打印类地层次结构
c.say()          # 解释器寻找方法是“从左到右”的方式，此时会执行B类中的say()

'''
Python 支持多继承，如果父类中有相同名字的方法，在子类没有指定父类名时，解释器将“从左到右”按顺序搜索
MRO(Method Resolution Order):方法解析顺序，我们可以通过mro()方法获得“类的层次结构”，
方法解析顺序也是按照这个“类的层次结构”寻找的
'''