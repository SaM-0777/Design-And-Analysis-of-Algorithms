"""Binary Search in Python"""
"""Author 20bcs126"""

import random
import timeit

a = []
size = 10000000

##Array Input
"""Filling up Array with Random Integers"""
for i in range(size):
    a.append(random.randint(0, size * 10))

"""Sorting of Data"""
a.sort()

"""Data to Search"""
Key = random.randint(0, size)
Data = a[Key]

"""Search"""
def Search(x, data):
    f = 0
    l = size - 1
    index = 0
    while(f <= l):
        index = int((f + l) / 2)
        if(x[index] > data):
            l = index - 1
        elif(x[index] < data):
            f = index + 1
        else:
            return index
    return -1  

if(Search(a, Data) != -1):
    print("Data found on {} Index".format(Search(a, Data)))
else:
    print("Data Not found")


t = timeit.timeit(lambda: Search(a, Data), number = 10)
print("Execution Time for Binary Search : {}".format(t))