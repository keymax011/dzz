# def bubble_sort(l):
#     t = l.copy()
#     for n in range(0, len(t)):
#         for i in range(len(t) - 1):
#             if t[i] > t[n]:
#                 t[i], t[n] = t[n], t[i]
#     return t
#
# nums = [4, 5, 1, 8]
# sort = bubble_sort(nums)
# print(sort)

tuples = []

lists = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

lists2 = [[24387, ' на русском', 2, 4.59],
[18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
[87236, 'C Programming Absolute Beginners Guide', 1, 23.55],
[58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]]

for i in lists:
    tuples.append(tuple(i))

for n in lists2:
    tuples.append(tuple(n))

sort = []
for f in tuples:
    sort.append(sorted(tuples, key = lambda price: price[3]))
    break
print(sort)

filtred = []
for h in tuples:
    filtred.append(tuple(filter(lambda x: h[2] >= 5, h)))
print(filtred)
