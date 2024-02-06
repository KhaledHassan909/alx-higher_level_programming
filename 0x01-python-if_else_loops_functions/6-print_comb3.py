#!/usr/bin/python3

for i in range(0, 9):
    flag = 0
    for j in range(0, 10):
        if i == 8 and j == 9:
            flag += 1
            print("{}{}".format(i, j))
            break
        if j > i and flag == 0:
            print("{}{}".format(i, j), end=', ')
        
