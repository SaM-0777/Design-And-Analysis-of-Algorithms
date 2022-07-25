// Implementation of Knapsack Problem for 0/1

#include <iostream>
using namespace std;

int fractional_Knapsack(int P[], int W[], int N, int Max_Capacity) {

    float p_w[N];
    int total_Profit = 0;

    for (int i = 0; i < N; i++) {
        p_w[i] = (float(P[i]) / float(W[i]));
    }

    int max;

    while (Max_Capacity > 0) {
        max = 0;
        // Find the index of maximum profit to weight ratio
        for (int i = 0; i < N; i ++) {
            if (p_w[max] < p_w[i]) {
                max = i;
            }
        }
        
        Max_Capacity -= W[max];
        // Check Whether item will fit on bag if not then return else calculate profit
        if (Max_Capacity < 0) {
            return total_Profit;
        }
        total_Profit += P[max];

        // Exchange
        int temp = P[max];
        P[max] = P[N - 1];
        P[N - 1] = temp;

        temp = W[max];
        W[max] = W[N - 1];
        W[N - 1] = temp;

        temp = p_w[max];
        p_w[max] = p_w[N - 1];
        p_w[N - 1] = temp;

        N -= 1;
    }

    return total_Profit;
}

int main(void) {

    int N = 5;                       // No. of Objects
    int profit[N] = {1, 5, 4, 2, 6}; // Profit Associated with respective Objects
    int weight[N] = {2, 1, 1, 3, 2}; // Weight of respective Objects
    int max_Capacity = 5;

    cout << "Total Profit : " << fractional_Knapsack(profit, weight, N, max_Capacity) << "\n";

    return 0;
}