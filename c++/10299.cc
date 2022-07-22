#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int phi(int n) {
    int result = n;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0)
                n /= i;
            result -= result / i;
        }
    }
    if (n > 1)
        result -= result / n;
    return result;
}

int n;

int main() 
{
    ifstream cin("10299.txt");

    bool first = true;

    while(true)
    {
        cin >> n;
        if (n == 0) {break;}

        //if (!first) {cout << endl;}
        //first = false;

        if(n == 1) 
        {
            cout << 0 << endl;
            continue;
        }

        n = phi(n);
        cout << n << endl;

    }

}

