def add(a,b):
    print("计算两个数的和：{0},{1},{2}".format(a,b,(a+b)))
    return a+b

def test02():
    print("001")
    print("002")
    return  # return两个作用：1、返回值 2、结束函数的执行
    print("003")

def test03(x,y,z):
    return [x*10,y*10,z*10]

c = add(10,20)
print(c*3)

d = test02()
print(d)

e = test03(1,2,3)
print(e*2)