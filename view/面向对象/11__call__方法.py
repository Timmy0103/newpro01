# 定义了__call__方法的对象，称为“可调用对象”，即该对象可以像函数一样被调用

# 可调用方法__call__()
class SalaryAccount:
    '''工资计算类'''

    def __call__(self, salary):
        print("算工资啦。。。")
        yearSalary = salary*12
        daySalary = salary//22.5
        hourSalary = daySalary//8.5
        return dict(yearSalary=yearSalary,monthSalary=salary,daySalary=daySalary,hourSalary=hourSalary)

s = SalaryAccount()
print(s(30000))