// Implementation of Fractional Knapsack

#include <iostream>
using namespace std;

float fractional_Knapsack(int P[], int W[], int N, int Max_Capacity) {
    float p_w[N];
    for (int i = 0; i < N; i ++){
        p_w[i] = (float(P[i]) / float(W[i]));
    }

    float total_Profit = 0.0;
    int max;

    while(Max_Capacity > 0) {
        max = 0;
        for (int i = 0; i < N; i ++) {
            if (p_w[max] < p_w[i]) {
                max = i;
            }
        }

        Max_Capacity -= W[max];
        if (Max_Capacity < 0) {
            Max_Capacity += W[max];
            break;
        }
        total_Profit += P[max];

        // Exchange
        int Temp = P[max];
        P[max] = P[N - 1];
        P[N - 1] = Temp;

        Temp = W[max];
        W[max] = W[N - 1];
        W[N - 1] = Temp;

        Temp = p_w[max];
        p_w[max] = p_w[N - 1];
        p_w[N - 1] = Temp;

        N -= 1;
    }

    total_Profit += Max_Capacity * (float(P[max]) / float(W[max]));

    return total_Profit;

}

int main(void) {

    int N = 5;
    int Profit[N] = {1, 2, 4, 1, 3};
    int Weight[N] = {2, 3, 2, 1, 4};
    int Max_capacity = 6;

    cout<<"Total Profit : "<<fractional_Knapsack(Profit, Weight, N, Max_capacity)<<"\n";

    return 0;
}