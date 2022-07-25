// Implementation of Selection sort in cpp

#include <iostream>
using namespace std;

void selection_Sort(int A[], int length) {
    int i = 1;
    int j = 0;
    int Temp;

    while (i < length) {
        for (j = 0; j < i; j ++) {
            if (A[i] < A[j]) {
                Temp = A[i];
                A[i] = A[j];
                A[j] = Temp;
            }
        }
        i ++;
    }
    
    // Print Sorted Array
    cout<< "\nSorted Array :";
    for (i = 0; i < length; i ++) {
        cout<< " " <<A[i];
    }
    
    return;
}

int main() {
    int length = 5;
    int A[length] = {10, 4, 7, -9, 2};

    cout<<"Unsorted Array:";
    for (int i = 0; i < length; i ++) {
        cout<< " " <<A[i];
    }

    // Call Selection Sort
    selection_Sort(A, length);

    return 0;
}