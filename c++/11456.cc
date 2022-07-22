#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int cases, train_cars, tmp;

int main() 
{
	ifstream cin("11456.txt");

	cin >> cases;

	for (int i{0}; i<cases; ++i)
	{
		cin >> train_cars;

		vector<int> cars;
		for (int j{0}; j<train_cars; ++j)
		{
			cin >> tmp;
			cars.push_back(tmp);
		}

		vector<int> back;
		back.resize(2500);
		for (int j{train_cars - 1}; j>=0; --j)
		{
			back[j] = 1;
			for (int k{j+1}; k < train_cars; ++k)
			{
				if (cars[j] < cars[k])
				{
					back[j] = max(back[j], back[k] + 1);
				}
			}
		}

		vector<int> front;
		front.resize(2500);
		for (int j{train_cars - 1}; j>=0; --j)
		{
			front[j] = 1;
			for (int k{j+1}; k < train_cars; ++k)
			{
				if (cars[j] > cars[k])
				{
					front[j] = max(front[j], front[k] + 1);
				}
			}
		}

		int ans = 0;
		for (int j{0}; j < train_cars; ++j)
		{
			ans = max(ans, back[j] + front[j] - 1);
		}

		cout << ans << endl;
	}

}