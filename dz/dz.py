# def calculations(action, n, m):
#     if action == sum:
#         print(n+m)
#         return action
#     if action == min:
#         print(n-m)
#         return action
# print(calculations(min, 8, 7))

# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum + i
#     return theSum
# print(listsum([1,3,5,7,9]))

def arg(*args):
    print(args)
    return args
arg(7, 8, "hello")

# def showEmployee(name, salary = 9000):
#     print(name, salary)
#     return
# print(showEmployee("Kkkkk", 5000))
