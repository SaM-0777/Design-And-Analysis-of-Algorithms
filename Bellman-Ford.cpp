// Bellman-Ford Impelementation in CPP

#include <iostream>
using namespace std;

struct Edge
{
    int src, dest, weight;
};


void Bellman_Ford(int G[][5], struct Edge Edge_list[])
{
    int V = 5;
    int E = 8;
    
    // choosing 1 as starting vertex and intializing all vertex cost as INFINITY
    int cost[5] = {0, INT_MAX, INT_MAX, INT_MAX, INT_MAX};

    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < E; j++)
        {
            if ((cost[Edge_list[j].src - 1] + Edge_list[j].weight) < cost[Edge_list[j].dest - 1])
            {
                cost[Edge_list[j].dest - 1] = cost[Edge_list[j].src - 1] + Edge_list[j].weight;
            }
        }
        
    }

    for (int i = 0; i < 5; i++)
    {
        cout << "Vertex : " << i + 1 << "\t" << "Cost : " << cost[i] << "\n";
    }

    return;
}

int main(void)
{
    int Graph[5][5] = {
        {0, -1, 4, INT_MAX},
        {INT_MAX, 0, 3, 2, 2},
        {INT_MAX, INT_MAX, 0, INT_MAX, INT_MAX},
        {INT_MAX, 1, 5, 0, INT_MAX},
        {INT_MAX, INT_MAX, INT_MAX, -3, 0}
    };

    // Define Edges
    struct Edge Edge_list[8];
    // Edge 1
    Edge_list[0].src = 1;
    Edge_list[0].dest = 2;
    Edge_list[0].weight = -1;
    // Edge 2
    Edge_list[1].src = 1;
    Edge_list[1].dest = 3;
    Edge_list[1].weight = 4;
    // Edge 3
    Edge_list[2].src = 2;
    Edge_list[2].dest = 3;
    Edge_list[2].weight = 3;
    // Edge 4
    Edge_list[3].src = 2;
    Edge_list[3].dest = 4;
    Edge_list[3].weight = 2;
    // Edge 5
    Edge_list[4].src = 2;
    Edge_list[4].dest = 5;
    Edge_list[4].weight = 2;
    // Edge 6
    Edge_list[5].src = 4;
    Edge_list[5].dest = 2;
    Edge_list[5].weight = 1;
    // Edge 7
    Edge_list[6].src = 4;
    Edge_list[6].dest = 3;
    Edge_list[6].weight = 5;
    // Edge 8
    Edge_list[7].src = 5;
    Edge_list[7].dest = 4;
    Edge_list[7].weight = -3;

    // Call Bellman Ford function
    Bellman_Ford(Graph, Edge_list);

    return 0;
}