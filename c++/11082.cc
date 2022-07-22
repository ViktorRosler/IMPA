#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int cases, row, col, in;

int main() 
{
	ifstream cin("11082.txt");

	cin >> cases;

	for (int i{0}; i<cases; ++i)
	{
		cin >> row >> col;

		int m[row][col];
		std::memset(m, 0, sizeof m);

		int total = 0;
		int d;
		vector<int> c;
		for (int j{0}; j<row; ++j)
		{		
			cin >> d;
			d -= (total);
			c.push_back(d);
			total += d;
		}

		for (int j{0}; j<row; ++j)
		{
			m[j][0] = c[j] - col + 1;
			for (int k{1}; k<col; ++k)
			{
				m[j][k] = 1;
			}	
		}

		int a[col];
		total = 0;
		for (int j{0}; j<col; ++j)
		{
			cin >> a[j];
			a[j] -= total;
			total += a[j];	
		}

		for (int j{0}; j<col; ++j)
		{
			int sum = 0;
			for (int k{0}; k<row; ++k)
			{
				if (m[k][j] > 20)
				{
					m[k][j+1] += m[k][j] - 20; 
					m[k][j] = 20;
				}
				sum += m[k][j];
			}

			while (sum != a[j])
			{
				int mini = 10000;
				int ind = 0;
				for (int k{0}; k<row; ++k)
				{
					if (m[k][j] > 1 && m[k][j+1] < mini)
					{
						ind = k;
						mini = m[k][j+1];
					}
				}
				m[ind][j] -= 1;
				m[ind][j+1] += 1;
				sum -= 1;
			}
		}
		if (i > 0) {cout << endl;}
		cout << "Matrix " << i+1 << endl;
		for (int j{0}; j<row; ++j)
		{
			for (int k{0}; k<col; ++k)
			{
				if (k > 0) {cout << " ";}
				cout << m[j][k];
			}
			cout << endl;
		}

	}


}