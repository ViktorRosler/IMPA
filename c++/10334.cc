#include <bits/stdc++.h>

using namespace std;

map<int, unsigned long long int> dp;

unsigned long long int fib(int n)
{
	if (n == 0) {return 1;}
	else if (n == 1) {return 2;}
	else 
	{
		if (dp.count(n) == 0) {dp[n] = fib(n-1) + fib(n-2);}
		return dp[n];
	}
}

int in;

int main() 
{
	ifstream cin("10334.txt");

	while (cin >> in) {cout << fib(in) << endl;}
}