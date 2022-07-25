// Implementation of Insertion Sort

#include <iostream>
using namespace std;

void insertion_Sort(int A[], int length) {
    int i, max, j = length - 1;

    while (j > 0) {
        max = 0;
        for (i = 0; i <= j; i++) {
            if (A[max] < A[i]) {
                max = i;
            }
        }

        // Swap Values
        int Temp = A[max];
        A[max] = A[j];
        A[j] = Temp;
        j --;
    }

    // Print Array
    cout<<"\nSorted Array :";
    for (int i = 0; i < length; i++) {
        cout << " " << A[i];
    }

    return;
}



int main(void){
    int length = 5;
    int A[length] = {10, 4, 7, -9, 2};

    cout<<"Unsorted Array :";
    for(int i = 0; i < length; i ++) {
        cout<< " " << A[i];
    }

    // Call Insertion Sort Function
    insertion_Sort(A, length);

    return 0;
}