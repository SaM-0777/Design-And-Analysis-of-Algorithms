// Prim's Algorithm in C++

#include <iostream>
using namespace std;

int main()
{
    int Graph[5][5] = {
        {0, 9, 75, 0, 0},
        {9, 0, 95, 19, 42},
        {75, 95, 0, 51, 66},
        {0, 19, 51, 0, 31},
        {0, 42, 66, 31, 0}
    };

    int edges = 0; // Number of edges

    int selected[5];

    // initially there is no selected vertex
    for (int i = 0; i < 5; i ++)
    {
        selected[i] = false;
    }

    // choosing 0th vertex first
    selected[0] = true;

    int x; 
    int y;


    cout << "Edge" << " : " << "Weight\n";
    while (edges < 4)
    {
        int min = INT_MAX;
        x = 0;
        y = 0;

        for (int i = 0; i < 5; i++)
        {
            if (selected[i])
            {
                for (int j = 0; j < 5; j++)
                {
                    if (!selected[j] && Graph[i][j])
                    {
                        if (min > Graph[i][j])
                        {
                            min = Graph[i][j];
                            x = i;
                            y = j;
                        }
                    }
                }
            }
        }
        cout << x << " - " << y << " :  " << Graph[x][y] <<endl;
        selected[y] = true;
        edges ++;
    }

    return 0;
}