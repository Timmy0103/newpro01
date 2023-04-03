'''
异常的传递
'''
def test1():
    print("-"*10 + "test1开始" + "-"*10)
    print(aa)
    print("-"*10 + "test1结束" + "-"*10)
def test2():
    print("-" * 10 + "test2开始" + "-" * 10)
    test1()
    print("-" * 10 + "test2结束" + "-" * 10)

def test3():
    print("-" * 10 + "test3开始" + "-" * 10)
    try:
        test2()
    except:
        pass
    print("-" * 10 + "test3结束" + "-" * 10)

test3()