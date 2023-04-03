# 内置函数：copy(浅拷贝)、deepcopy(深拷贝)
# 浅拷贝：不拷贝子对象的内存，只拷贝子对象的引用
# 深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影响源对象
import copy
def testcopy():
    '''定义浅拷贝'''
    a = [10,20,[5,6]]
    b = copy.copy(a)
    print("a:", a)
    print("b:", b)
    b.append(30)
    b[2].append(7)
    print("浅拷贝...")
    print("a:", a)
    print("b:", b)

def testdeepcopy():
    '''定义深拷贝'''
    a = [10,20,[5,6]]
    b = copy.deepcopy(a)
    print("a:", a)
    print("b:", b)
    b.append(30)
    b[2].append(7)
    print("深拷贝...")
    print("a:", a)
    print("b:", b)

testcopy()
print("*****************************")
testdeepcopy()

# 传递不可变对象时，不可变对象里包含的子对象是可变的，则方法内修改了这个可变对象，源对象也发生了变化
aa = (10, 20, [5, 6])
print("aa", id(aa))
def test03(y):
    print("y", id(y))
    y[2][0] = 888
    print(y)
    print("y", id(y))
test03(aa)
print(aa)