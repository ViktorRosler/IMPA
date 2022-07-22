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
	ifstream cin("11101.txt");

	int points;
	int x, y;
	bool bo = true;
	vector<tuple<int,int>> mall1;
	vector<tuple<int,int>> mall2;
	while (cin >> points)
	{
		if (bo)
		{
			bo = false;
			for (int i{0}; i<points; ++i)
			{
				cin >> x >> y;
				mall1.push_back(make_tuple(x,y));
			}
			

		}
		else
		{
			bo = true;
			for (int i{0}; i<points; ++i)
			{
				cin >> x >> y;
				mall2.push_back(make_tuple(x,y));
			}


			int min = 10000;

			int a = mall1.size();
			int b = mall2.size();

			for (int i{0}; i < 100000; ++i)
			{
				int c = rand() % a;
				int d = rand() % b;

				int e = abs(get<0>(mall1[c]) - get<0>(mall2[d])) + abs(get<1>(mall1[c]) - get<1>(mall2[d]));
				if (e < min) {min = e;}
			}

			cout << min << endl;

			mall1.clear();
			mall2.clear();
		}
	}
}