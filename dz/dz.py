#def uniq(input):
#  output = []
#  for x in input:
#    if x not in output:
#      output.append(x)
#  return output

#z = [3, 7, 8, 9]
#x = []
#x = z.copy()
#print(x)

#s1 = [5, 3, 6, 7]
#s2 = [5, 3, 9, 7]
#s3 = [x for x in s1 if x not in s2]
#print(s3)

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dic4 = dic1.update(dic2)
dic5 = dic1.update(dic3)
print(dic1)