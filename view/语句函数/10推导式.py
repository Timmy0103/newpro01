# 列表推导式
a = [x*2 for x in range(1, 5)]
print(a)
a = []
for x in range(1, 5):
    a.append(x*2)
print(a)

b = [x*2 for x in range(1, 20)if x % 5 == 0]
print(b)
b = []
for x in range(1, 20):
    if x % 5 == 0:
        b.append(x*2)
print(b)

cells = [(row, col) for row in range(1, 3) for col in range(1, 3)]
print(cells)
cells = []
for row in range(1, 3):
    for col in range(1, 3):
        cells.append((row, col))
print(cells)

# 字典推导式
my_test = "笑嘻嘻呵呵你好  小小好细，呵呵"
char_count = {c: my_test.count(c) for c in my_test}
print(char_count)
# 改成for循环有问题，需要修改
my_test = "笑嘻嘻呵呵你好  小小好细，呵呵"
char_count = {}
for c in my_test:
    char_count = {c: my_test.count(c)}
    print(char_count, end="\t")
print()

# 集合推导式
d = {x for x in range(1, 100)if x % 9 == 0}
print(d)

# 生成器推导式（生成元组）
e = (x for x in range(1, 100)if x % 9 == 0)
# print(tuple(e))
# print(tuple(e))
for x in e:   # e是生成器对象，生成器是迭代的对象，只能使用一次
    print(x, end="\t")
print(tuple(e))
