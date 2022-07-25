// job Sequencing with Deadline Problem

#include <iostream>
using namespace std;

void maxProfit(int Profit_list[], int Deadline[], int total_TimeSlots, int N) {
    float total_Profit = 0.0;

    int Time = 1;
    int max;

    while (Time <= total_TimeSlots) {
        for (int i = 0; i < N; i ++){
            if (Deadline[i] == Time){
                max = i;
                break;
            }
        }

        for (int i = 0; i < N; i++) {
            if (Profit_list[i] >= Profit_list[max] && Deadline[i] == Time) {
                max = i;
            }
        }

        total_Profit += Profit_list[max];
        Time += 1;

        int Temp = Profit_list[N - 1];
        Profit_list[N - 1] = Profit_list[max];
        Profit_list[max] = Temp;

        Temp = Deadline[N - 1];
        Deadline[N - 1] = Deadline[max];
        Deadline[max] = Temp;

        N -= 1;
    }

    cout<<"Total Profit : "<<total_Profit;
    return;
}

int main(void) {
    
    int N = 5;

    int Profit_list[N] = {20, 15, 5, 10, 5};
    int Deadline[N] = {2, 1, 1, 3, 2};

    int total_TimeSlots = 3;

    // Call maxProfit fn
    maxProfit(Profit_list, Deadline, total_TimeSlots, N);

    return 0;
}


