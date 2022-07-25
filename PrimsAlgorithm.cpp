// Prims Algorithm in C ++

#include <iostream>
using namespace std;

int minimum_key(int k[], int mst[])
{
    int minimum = INT_MIN, min;

    for (int i = 0; i < 5; i ++)
    {
        if (mst[i] == 0 && k[i] < minimum)
        {
            minimum = k[i];
            min = i;
        }
    }
    return min;
}

void Prims_algorithm(int graph[5][5])
{
    int parent[5];
    int k[5];
    int mst[5];
    int count, u, v;

    for (int i = 0; i < 5; i ++)
    {
        k[i] = INT_MAX;
        mst[i] = 0;
    }

    k[0] = 0;
    parent[0] = -1;

    for (count = 0; count < 5 - 1; count ++)
    {
        u = minimum_key(k, mst);
        mst[u] = 1;

        for (v = 0; v < 5; v ++)
        {
            if (graph[u][v] && mst[v] == 0 && graph[u][v] < k[v])
            {
                parent[v] = u;
                k[v] = graph[u][v];
            }
        }
    }

    for (int i = 1; i < 5; i ++)
    {
        cout<< parent[i] << i << graph[i][parent[i]];
    }
}




int main(void)
{
    int Graph[5][5] = {
        {3, 2, 1, 9, 0},
        {5, 1, 2, 10, 4},
        {0, 4, 1, 0, 9},
        {8, 10, 0, 2, 10},
        {1, 6, 8, 11, 0}
    };

    Prims_algorithm(Graph);

    return 0;
}







