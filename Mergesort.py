"""Merge sort in Python
Author : 20bcs126"""

import random
import timeit

##User Input Array size
length = int(input("Enter Array size : "))

##Merge Sort Function
def Mergesort(x):
    
    ##Creating 2 Temporary Empty list
    Left = Right = []
    
    ##Dividing the Larger Array into 2 smaller Array Named Left and Right
    if len(x) > 1:
        midIndex = int(len(x) / 2) ##Middle Index of the Larger Array
        
        ##Dividing the larger array to 2 equal halves named Left and Right
        Left = x[ : midIndex]
        Right = x[midIndex : ]
        
        ##Dividing Process will go on until the smaller Arrays have only 1 or 2 elements
        Mergesort(Left)
        Mergesort(Right)

    ##Checking for each elements and arranging them in sorted order
    i = j = k = 0
    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
            x[k] = Left[i]
            i += 1
        else:
            x[k] = Right[j]
            j += 1
        k += 1

    ##This loops will check for remaining elements in both Left and Right array and arrange them in sorted order
    while i < len(Left):
        x[k] = Left[i]
        i += 1
        k += 1

    while j < len(Right):
        x[k] = Right[j]
        j += 1
        k += 1
    

## Number of Times code will run to calculate the average Time of Execution
NumberofCases = int(input("Enter Number of Times : "))

## Calculate the Execution Time of Merger sort function
ExecutionTime = 0.00

##This loop will run for NumberofCases times
for i in range(0, NumberofCases):

    #Declare a new array
    array = []
    #Random Integer Array Input
    for j in range(0, length):
        array.append(random.randint(-length * 10, length * 10))
    
    #Print the array before sorting 
    print("Unsorted Array : ", array)
    #This will record the Execution time of Merge sort Algorithm
    t = timeit.timeit(lambda : Mergesort(array), number = 1)
    #Add the Execution Time (t) for ofr each run
    ExecutionTime += t
    #Print the sorted array
    print("Sorted Array : ", array)
    print('\n')

##Calculate the average of each run 
avgTime = float(ExecutionTime / NumberofCases)
##Final Output will display the average execution time for Merge Sort
print("Average Execution Time of Merge Sort for {0} Elements is {1} seconds".format(length, avgTime))
