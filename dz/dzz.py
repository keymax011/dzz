# def number(num):
#     return num%10 + number(num//10) if num > 9 else num
# print(number(123))

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(10))

# def mult(a, b):
#    if a == 0:
#       return 0
#    elif a == 1:
#       return b
#    else:
#       return b + mult(a-1, b)
# print(mult(7, 5))

# def step(n):
#    if n & (n - 1) :
#       print("NO")
#    else:
#       print("YES")
#
# print(step(4))

# Создайте inner функцию для вычисления сложения следующим
# образом:
# a. Создайте внешнюю функцию, которая будет принимать два
# параметра, a и b
# b. Создайте внутреннюю функцию внутри внешней функции,
# которая будет вычислять сложение a и b
# c. Наконец, внешняя функция добавит 5 и вернет ее.

# a = int(input())
# b = int(input())
# def inner ():
#    global a, b
#    print(a+b)
#
# print(inner())

def inner (a, b):
   print(a+b)

print(inner(4, 4))
