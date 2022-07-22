#include <bits/stdc++.h>

using namespace std;

int cases, N, K, tmp;
vector<int> v;

int palin(int i, int j, int n)
{
	
	while(v[i] == v[j] && j - i > 0)
	{
		++i;
		--j;
	}

	if (j - i <= 0) {return n;}
	if (n+1 > K) {return -1;}

	int a = palin(i+1, j, n+1);
	int b = palin(i, j-1, n+1);

	if (a == -1 && b == -1) {return -1;}
	else if (a == -1) {return b;}
	else if (b == -1) {return a;}
	else {return min(a,b);}
}

int main() 
{
	ifstream cin("11753.txt");

	cin >> cases;

	for (int i{0}; i<cases; ++i)
	{
		cin >> N >> K;

		
		v.clear();

		for (int j{0}; j<N; ++j)
		{
			cin >> tmp;
			v.push_back(tmp);
		}

		tmp = palin(0, N-1, 0);

		if (tmp == -1)
		{
			cout << "Case " << i+1 << ": " << "Too difficult" << endl;
		}
		else if (tmp == 0)
		{
			cout << "Case " << i+1 << ": " << "Too easy" << endl;
		}
		else
		{
			cout << "Case " << i+1 << ": " << tmp << endl;
		}

		
	}

}