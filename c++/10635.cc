#include <iostream>
#include <tuple>
#include <cmath>
#include <vector>
#include <random>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// FIND Longest Increasing Subsequence in O(n log n) 
// based on algorithm (not code) at https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

int lis(vector<int>& v) 
{ 
    vector<int> tail;

    // rule 1
    tail.push_back(v[0]);

    int length = 1;
  
    for (size_t i = 1; i < v.size(); i++) { 
    	
    	// rule 2
        if (v[i] > tail[length - 1]) 
        {
            tail.push_back(v[i]);
            length++; 
        }
        // rule 3
        else
        {
        	for (size_t j{0}; j < length; ++j)
        	{
        		if (tail[j] >= v[i])
        		{
        			tail[j] = v[i];
        			break;
        		}
        	}
        }
    } 
  
    return length; 
} 

int main() 
{
	//ifstream cin("10635.txt");
	int cases,n,p,q,t;
	int arr[70000];
	vector<int> seq;
	cin >> cases;

	for (int k{0}; k < cases; ++k)
	{
		memset(arr, 0, 70000);
		seq.clear();

		cin >> n >> p >> q;

		for (int i{1}; i < p+2; ++i)
		{
			cin >> t;
			arr[t] = i;
		}

		for (int i{0}; i < q+1; ++i)
		{
			cin >> t;
			if (arr[t] != 0) {seq.push_back(arr[t]);}
		}

		cout << "Case " << k+1 << ": " << lis(seq) << endl;

	}

}