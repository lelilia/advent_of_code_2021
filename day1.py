""" ADVENT OF CODE day 1 """

import numpy as np

list = np.loadtxt("input1.txt", dtype=int)
count_1 = 0
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        count_1 += 1
print(count_1)

count_2 = 0
last_value = list[0] + list[1] + list[2]
for i in range(1, len(list)-2):
    if list[i] + list[i+1] + list[i+2] > last_value:
        count_2 += 1
    last_value =list[i] + list[i+1] + list[i+2]

print(count_2)


