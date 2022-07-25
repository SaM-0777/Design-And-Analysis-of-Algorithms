# Implementation of Quick sort in Python

import random
import timeit

def Partition(A, l, r):
    pivot_index = l
    pivot = A[l]

    while l < r:
        while l < len(A) and A[l] <= pivot:
            l += 1

        while A[r] > pivot:
            r -= 1

        if l < r:
            A[l], A[r] = A[r], A[l]

    A[r], A[pivot_index] = A[pivot_index], A[r]
    return r


def Quick_Sort(A, l, r):

    if l < r:
        P = Partition(A, l, r)

        Quick_Sort(A, l, P - 1)
        Quick_Sort(A, P + 1, r)

# Quick Sort Algorithm Ends here

# Function to Inputs Random Elements in Array
def ArrayInput(length):
    A = []
    for i in range(length):
        A.append(random.randint(-50, 50))
    
    return A

# Quick Sort with Random Elements
def random_Inputs(length, N):
    Time = 0.0
    for i in range(N):
        Array = ArrayInput(length)
        print("Unsorted Array : ", Array)
        Time += timeit.timeit(lambda : Quick_Sort(Array, 0, length - 1), number = 1)
        print("Sorted Array : ", Array)
        print()
    
    print("Average Time for Execution with {0} Random Inputs : {1}".format(length, float(Time / N)))
    return

# Quick Sort with Elements in Decreasing Order
def dec_Inputs(length, N):
    A = []
    Time = 0.0
    for i in range(length):
        A.append(length - i)
    print("Unsorted Array : ", A)

    for j in range(N):
        A = []
        for i in range(length):
            A.append(length - i)
        
        Time += timeit.timeit(lambda: Quick_Sort(A, 0, length - 1), number = 1)
        
    print("Sorted Array : ", A)
    print("Average Execution Time with {0} Elements in Decreasing Order : {1}".format(length, Time / N))
    return

# Quick Sort with Elements in Increasing Order
def inc_Inputs(length, N):
    A = ArrayInput(length)
    Quick_Sort(A, 0, length - 1)
    print("Array : ", A)
    Time = timeit.timeit(lambda : Quick_Sort(A, 0, length - 1), number = N)
    print("Resultant Array : ", A)
    print("Avergae Execution time with {0} Elements in Incresing Order : {1}".format(length, Time / N))
    return

# Quick Sort with same Elements
def same_Inputs(length, N):
    A = []
    for i in range(length):
        A.append(20)
    print("Array : ", A)
    Time = timeit.timeit(lambda : Quick_Sort(A, 0, length - 1), number = N)
    print("Average Execution time with {0} same Elements : {1}".format(length, float(Time / N)))
    return

# Main Function
if __name__ == "__main__":

    N = int(input("\nNumber of times you want to execute to calculate Average Execution Time : "))
    length = int(input("Array length : "))
    
    print("\nArray with Random Elements")
    random_Inputs(length, N)

    print("\nArray with Elements in Decreasing Order")
    dec_Inputs(length, N)
    
    print("\nArray with Elements in Incresing Order")
    inc_Inputs(length, N)
    
    print("\nArray with Same Elements")
    same_Inputs(length, N)
    
    print()

