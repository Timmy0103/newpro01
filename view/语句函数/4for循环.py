# for循环通常用于可迭代对象的遍历
for x in (10, 20, 30):
    print(x*3)
    pass
for y in "abc":
    print(y, end="\t")
    pass
print()
# 1-100累加和，奇数和，偶数和
sum_all = 0   # 累加和
sum_odd = 0   # 奇数和
sum_even = 0  # 偶数和
for x in range(101):
    sum_all += x
    if x % 2 == 1:
        sum_odd += x
    else:
        sum_even += x
print("1-100累加和{0}，奇数和{1}，偶数和{2}".format(sum_all, sum_odd, sum_even))
pass
