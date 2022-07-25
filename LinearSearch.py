"""Linear Search"""
"""Author 20bcs126"""


import random
import timeit

x = []      ##Array of Integers
size = 10000000

##Array Input
"""Filling up Array with Random Integers"""
for i in range(size):               
    x.append(random.randint(0, size * 12))

key = random.randint(0, size)
data = x[4999999]

##Linear Search
def Search(Data):
    for i in range(size):
        if(data == x[i]):
            return i
    return -1
    
if(Search(data) != -1):
    print("Data found on {0} Index".format(Search(data)))

else:
    print("No such Data Found")

t = timeit.timeit(lambda: Search(x[0]), number = 10)
print("Execution Time for Linear Search : {}".format(t))