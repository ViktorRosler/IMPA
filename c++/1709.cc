#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int p,a,b,c,d,n;
double ans, diff, maxi;

int main() 
{
	ifstream cin("1709.txt");

	while (cin >> p)
	{
		cin >> a >> b >> c >> d >> n;

		maxi = 0;
		diff = 0;
		for (int k{1}; k<=n; ++k)
		{
			ans = p * (sin(a*k+b) + cos(c*k+d) + 2);

			maxi = max(ans,maxi);
			if (ans < maxi)
			{
				diff = max(diff, maxi-ans);
			}
		}

		cout << setprecision(12) << diff << endl;
	}

}