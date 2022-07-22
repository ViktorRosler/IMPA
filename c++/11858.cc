#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;


long int a,n,s;

vector<long int> ms(vector<long int> v)
{
	if (v.size() <= 1) {return v;}

	long int half = v.size() / 2;

	vector<long int> v1;
	vector<long int> v2;
	for (long int i{0}; i<v.size(); ++i)
	{
		if (i < half) {v1.push_back(v[i]);}
		else {v2.push_back(v[i]);}
	}

	v1 = ms(v1);
	v2 = ms(v2);

	vector<long int> out;

	long int i = 0;
	long int j = 0;

	while ( i < v1.size() && j < v2.size())
	{
		if (v1[i] < v2[j]) {out.push_back(v1[i++]);} 
		else 
		{
			s += half - i;
			out.push_back(v2[j++]);
		}	
		
	}

	while (i < v1.size()){out.push_back(v1[i++]);}

	while (j < v2.size()){out.push_back(v2[j++]);}

	return out;
}

int main() 
{
	//ifstream cin("11858.txt");

	while (cin >> n)
	{
		vector<long int> v;
		for (long int i{0}; i<n; ++i)
		{
			cin >> a;
			v.push_back(a);
		}

		s = 0;
		ms(v);

		cout << s << endl;
	}

}