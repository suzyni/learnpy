# Question 7

from sys import argv

script, x, y = argv
row_num = int(x)
col_num = int(y)
list = []
for i in range(0, row_num):
    list.append([i*j for j in range(0, col_num)])

print list