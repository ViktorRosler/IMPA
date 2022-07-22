#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>
#include<time.h>

using namespace std;

int cases, people, lsum, rsum, dummy, rande, max_diff, lres, rres, nr_left, nr_right;


int main() 
{
	ifstream cin("10032.txt");

	srand(time(0));

	cin >> cases;

	for (int i{0}; i<cases; ++i)
	{
		cin >> people;

		max_diff = 999999;

		vector<int> ppl_vec;
		ppl_vec.clear();
		for (int j{0}; j<people; ++j)
		{
			cin >> dummy;
			ppl_vec.push_back(dummy);
		}

		sort(ppl_vec.begin(), ppl_vec.end(), greater<int>()); 

		// rand tries
		for (int k{0}; k<10000; ++k)
		{
			lsum = 0;
			rsum = 0;
			nr_left = 0;
			nr_right = 0;
			for (int j{0}; j<people; ++j)
			{
				if (nr_left - nr_right > (people-j-1))
				{
					rsum += ppl_vec[j];
					nr_right += 1;
				}
				else if (nr_right - nr_left > (people-j-1))
				{
					lsum += ppl_vec[j];
					nr_left += 1;
				}
				else if (lsum - rsum > ppl_vec[j] * 10)
				{ 
					rsum += ppl_vec[j]; 
					nr_right += 1;
				}
				else if (rsum - lsum > ppl_vec[j] * 10)
				{ 
					lsum += ppl_vec[j]; 
					nr_left += 1;
				} 
				else
				{
					rande = rand() % 2;
					if (rande == 0) 
					{ 
						rsum += ppl_vec[j]; 
						nr_right += 1;
					}
					else 
					{ 
						lsum += ppl_vec[j]; 
						nr_left += 1;
					}
				}
				//cout << lsum << " " << rsum << " " << nr_left << " " << nr_right << endl;
				
			}
			//cout << nr_left << " " << nr_right << endl;
			if (abs(nr_left - nr_right) <= 1 && abs(rsum-lsum) < max_diff)
			{
				max_diff = abs(rsum-lsum);
				if (rsum < lsum) 
				{
					lres = rsum;
					rres = lsum;
				}
				else
				{
					lres = lsum;
					rres = rsum;
				}
			}
		}
		if (i > 0) {cout << endl;}
		cout << lres << " " << rres << endl;
	}

}