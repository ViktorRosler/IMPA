#include <bits/stdc++.h>

using namespace std;

int inp;

vector<long long int> primes;
set<int> semi_primes;

int main() 
{
	ifstream cin("11105.txt");

	for (int i{1}; i<=200001; i += 4)
	{
		bool prime = true;
		for (int j{5}; j*j<=i; j += 4)
		{
			if (i % j == 0)
			{
				prime = false;
				break;
			}
		}
		if (prime) {primes.push_back(i);}
	}

	for (long long int i{0}; i<primes.size(); ++i)
	{
		for (long long int j{i}; j<primes.size(); ++j)
		{
			long long int a = primes[i] * primes[j];
			if (a > 1 && a <= 1000001)
			{
				semi_primes.insert(a);
			}
			else{break;}	
		}
	}

	int val = 0;
	set<int>::iterator it = semi_primes.begin();
	vector<int> aa(1000001);
	for (int i{0}; i<aa.size(); ++i)
	{
		if(i+1 == *it)
		{
			if (it != semi_primes.end()) {it++;}
			val++;
		}
		aa[i] = val;
	}                           

	
	while (true)
	{
		cin >> inp;
		if (inp == 0) {break;}

        cout << inp << " " << aa[inp-1] << endl;
	}
}
