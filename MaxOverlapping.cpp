# include <iostream>
using namespace std;

int main(void)
{
    int A[] = {0, 5, 4, 12, 7, 8, 6, 12, 5, 6, 7, 8};
    int f, l = 0;
    int count = 0;
    int length = int(sizeof(A) / sizeof(A[0]));

    for (int i = 0; i < length; i ++)
    {
        count = 0;
        int current = A[i];
        f = i;
        for (int j = 0; j < length; j ++)
        {
            if (A[i] + count + 1 == A[j + 1])
            {
                count ++;
                l = j;
            }

        }
    }

    cout<< "Count : " <<count<<"\n";

    return 0;
}