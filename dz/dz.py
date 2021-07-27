import random
l = []
for i in range(10):
    l.append(random.randint(0, 100))
print(l)
print(list(set(l)))

# import random
# l1 = []
# for i in range(10):
#     l1.append(random.randint(0, 100))
# print(l1)
# l2 = []
# for i in l1:
#     l2.append(i)
# print(l2)

# import random
# l1 = []
# l2 = []
# l3 = []
# for i in range(10):
#     l1.append(random.randint(0, 100))
# print(l1)
# for i in range(10):
#     l2.append(random.randint(0, 100))
# print(l2)
# for i in l1:
#     if i in l2:
#         l3.append(i)
# print(l3)

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)

# import random
# d = {}
# x = 0
# for x in range(0, 1):
#     x = random.randint(0, 15)
# print(x)
# y = x*x
# print(y)
# d = {x: y}
# print(d)