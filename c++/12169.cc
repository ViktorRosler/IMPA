#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
	//ifstream cin("12169.txt");
	int ra, rb, cases, in, done, min;
	int vec[10000];

	cin >> cases;

	min = 100000000;
	for (int i = 0; i < cases; i++)
	{
        cin >> in;
        if (in < min)
        {
        	min = in;
        }
        vec[i] = in;
	}

	for (int a = 0; a < 10001; a += 2)
	{
		for (int b = a; b < 10001; b++)
		{
			in = vec[0];
			done = 1;
			for (int n = 0; n < cases; n++)
			{
				if (in != vec[n])
				{
					done = 0;
				}
				in = (a * in + b) % 10001;
				in = (a * in + b) % 10001;
			}
			if (done)
			{
				ra = a;
				rb = b;
				a = 10001;
				b = 10001;
				break;
			}
		}

	}
	for (int i = 0; i < cases; i++)
	{
		cout << (ra * vec[i] + rb) % 10001 << endl;
	}
}