#include <iostream>
using namespace std;

struct Edge{
    int src, destiny, weight;
};

int main(void){
    // Define the graph using Adjacency Matrix
    int Graph[5][5] = {
        {0, 1, 7, 10, 5},
        {1, 0, 3, INT_MAX, INT_MAX},
        {7, 3, 0, 4, INT_MAX},
        {10, INT_MAX, 4, 0, 2},
        {5, INT_MAX, INT_MAX, 2, 0}
    };

    // Make a array of struct to store the source Node, Destiny Node and Weight of Edge
    struct Edge E[7];
    int k = 0;

    // Store the above info in the array
    for (int i = 0; i < 5; i ++)
    {
        for (int j = i + 1; j < 5; j ++)
        {
            if (Graph[i][j] != INT_MAX)
            {
                E[k].src = i + 1;
                E[k].destiny = j + 1;
                E[k].weight = Graph[i][j];
                k ++;
            }
        }
    }

    // Sort the Array according to weight in increasing order
    int len = (int(sizeof(E)) / int(sizeof(E[0])));
    int max = 0;
    for (int i = 0; i < len; i ++)
    {
        for (int j = 0; j < len - i; j ++)
        {
            if (E[j].weight > E[max].weight)
            {
                max = j;
            }
        }
        struct Edge Temp = E[max];
        E[max] = E[len - i - 1];
        E[len - i - 1] = Temp;

        max = 0;
    }

    int Total_cost = 0;
    int selected_edges = 1;

    // Pick one edge at a time from the Array until all the vertices are included
    while (selected_edges < 5)
    {
        Total_cost += E[selected_edges - 1].weight;
        cout << E[selected_edges - 1].src << " -- " << E[selected_edges - 1].destiny << " : " << E[selected_edges - 1].weight << endl;
        selected_edges ++;
    }

    cout << "Total Cost : " << Total_cost;

    return 0;
}

