# cort = (7, 8, 9, "Hello")
# cort = list(cort)
# print(cort)

# l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# print([t[:-1] + (100,) for t in l])

# c1 = (1, 2, 3, 4)
# c2 = (3, 5, 2, 1)
# c3 = (2, 2, 3, 1)
# q, w, e, r = c1
# t, y, u, i = c2
# a, s, d, f = c3
# c4 = (q+t+a, w+y+s, e+u+d, r+i+f)
# print(c4)

# import random
# s1 = set()
# for _ in range(0, 10):
#     s1.add(random.randint(0, 100))
# print(s1)
# s = int(input())
# if s in s1:
#     print("yes")
# else: print("no")


# import random
# s1 = set()
# s2 = set()
# f = False
# for _ in range(0, 10):
#     s1.add(random.randint(0, 100))
# print(s1)
# for _ in range(0, 10):
#     s2.add(random.randint(0, 100))
# print(s2)
# for i in s1:
#     if i in s2:
#         f = True
#         break
# print(f)

# import random
# s1 = set()
# s2 = set()
# s3 = set()
# for _ in range(0, 10):
#     s1.add(random.randint(0, 100))
# print(s1)
# for _ in range(0, 10):
#     s2.add(random.randint(0, 100))
# print(s2)
# for i in s1:
#     if i not in s2:
#         s3.add(i)
# print(s3)

import random
s1 = set()
s2 = set()
for _ in range(0, 10):
    s1.add(random.randint(0, 100))
print(s1)
for _ in range(0, 10):
    s2.add(random.randint(0, 100))
print(s2)
for i in s1:
    if i in s2:
        s1.remove(i)
        break
print(s1)
