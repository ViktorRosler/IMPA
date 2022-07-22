#include <iostream>
#include <tuple>
#include <cmath>
#include <vector>
#include <random>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() 
{
    ifstream cin("10306.txt");

    int probs,coins,value;

    int squares[300];
    for (int i{0}; i<300; ++i)
    {
        squares[i] = (i+1)*(i+1);
    }

    vector<int> coin_vec;

	cin >> probs;

    for (int i{0}; i < probs; ++i)
    {
        cin >> coins >> value;

        coin_vec.clear();
        for (int j{0}; j < coins; ++j)
        {
            int a,b;
            cin >> a >> b;
            coin_vec.push_back(k+1);
            cout << a*a + b*b << " ";
        }
        sort(coin_vec.begin(), coin_vec.end(), greater<int>());

        int sum, coin_count;
        for (int j{0}; j < coin_vec.size(); ++j)
        {
            while (sum + coin_vec[j] < value*value)
            {
                sum += coin_vec[j];
                coin_count += 1;
            }
        }

        cout << coin_count << endl;


    }


    
}