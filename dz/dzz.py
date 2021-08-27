import random

f = open('file.txt', 'w')
for _ in range(100):
    line = ''
    for i in range(10):
        i = str(random.randint(0,100))
        ret = line
        line = line + i + " "
    f.write(line)
    f.write("\n")
    del line

def func(file_name):
    r = open(file_name, "a")
    ret = 0
    for n in r:
        ret = n*n
    r.close()
    return ret

print(func("file.txt"))
