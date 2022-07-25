// Implementation of Max-Heapify, Build-Max_Heap and Heapsort in C ++
// By :- 20bcs126

#include <iostream>
using namespace std;

void Max_Heapify(int A[], int heapsize, int i) {

    int largest = i;
    int l = (2 * i) + 1;
    int r = (2 * i) + 2;
    int temp;

    if (l < heapsize && A[l] > A[largest]) {
        largest = l;
    }

    if (r < heapsize && A[r] > A[largest]) {
        largest = r;
    }

    if (largest != i) {
        temp = A[i];
        A[i] = A[largest];
        A[largest] = temp;
        Max_Heapify(A, heapsize, largest);
    }
}

void Build_Max_Heapify(int A[], int heapsize) {

    for (int i = heapsize / 2 - 1; i >= 0; i --) {
        Max_Heapify(A, heapsize, i);
    }
}

void Heap_Sort(int A[], int heapsize) {
    Build_Max_Heapify(A, heapsize);
    int temp;
    for (int i = heapsize - 1; i >= 0; i --) {
        temp = A[0];
        A[0] = A[i];
        A[i] = temp;
        Max_Heapify(A, i, 0);
    }
}

int main()
{
    int size;
    cout << "Array Size : ";
    cin >> size;

    int A[size];
    cout << "Input Array Element :\n";
    for (int i = 0; i < size; i++)
    {
        cin >> A[i];
    }

    // Display Unsorted Array
    cout << "Unsorted Array : ";
    for (int i = 0; i < size; i++)
    {
        cout << A[i] << " ";
    }

    Heap_Sort(A, size);

    // Display Sorted Array
    cout << "\nSorted Array : ";
    for (int i = 0; i < size; i++)
    {
        cout << A[i] <<" ";
    }

    return 0;
}