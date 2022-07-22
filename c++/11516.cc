#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int cases,a,b;
double points,houses;
vector<int> distances;

int main() 
{
	ifstream cin("11516.txt");

	cin >> cases;

	for (int i{0}; i<cases; ++i)
	{
		cin >> points >> houses;

		int h_per_p = ceil(houses / points);

		cout << h_per_p << endl;

		cin >> a;
		for (int j{1}; j<houses; ++j)
		{
			cin >> b;
			distances.push_back(b-a);
			a = b;
		}

	}
	1+1;


}