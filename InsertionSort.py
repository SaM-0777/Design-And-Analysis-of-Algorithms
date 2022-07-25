##Insertion Sort in Python

import random
import timeit

def Insertion_Sort(x):
    i = 1
    min = 0
    for i in range(len(x)):
        ##Find the index where min element is present
        for j in range(i, len(x)):
            if x[j] < x[min]:
                min = j
        
        ##swap the element with first element
        temp = x[min]
        x[min] = x[i - 1]
        x[i - 1] = temp

        min = i
    
    print("Sorted Array : ", x)
    return


size = int(input("Enter Length of Array : "))
N = int(input("Number of Execution : "))
t = 0.0

for i in range(N):
    X = []
    ##Random Integeres Input
    for j in range(0, size):
        X.append(random.randint(-size * 2, size * 2))
    print("Unsorted Array : ", X)
    t += timeit.timeit(lambda : Insertion_Sort(X), number = 1)

print("Average Execution Time for Insertion sort : ", float(t / N))