// C ++ code for Hoffman Compression

#include <iostream>
#include <string.h>
using namespace std;

int main(void)
{
    string message = "BCCABBDDAECCBBAEDDCC";    // 20 letters
    string charactres = "";

    for (int i = 0; i < message.length(); i ++)
    {
        for (int j = 0; j < charactres.length(); j ++)
        {
            if (message[i] == charactres[j])
            {
                continue;
            }
            else
            {
                charactres[charactres.length()] == message[i];
            }
        }
    }







    return 0;
}