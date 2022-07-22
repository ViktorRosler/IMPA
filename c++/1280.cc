#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int cs, degree, step, steps;
double tmp, xmin, xmax, org_xmin, summa, part_sum, r, a;

int main() 
{
	ifstream cin("1280.txt");
	cs = 0;

	while (cin >> degree)
	{
		cs += 1;
		summa = 0;
		steps = 0;
		part_sum = 0;
		vector<double> coeff;
		coeff.clear();
		coeff.resize(0);

		for (int i{0}; i<=degree; ++i)
		{
			cin >> tmp;
			coeff.push_back(tmp);
		}

		vector<double> integ;
		for (int i{0}; i<=degree; ++i)
		{
			integ.push_back(coeff[i]/(i+1));
			cout << integ[i] << endl;
		}

		cin >> xmin >> xmax >> step;
		org_xmin = xmin;

		vector<double> step_vec;
		step_vec.clear();
		step_vec.resize(0);

		r = 0;
		for (int i{0}; i<=degree; ++i)
		{ 
			r += integ[i] * pow(xmin, i+1);
		}
		
		summa -= M_PI * r * r;

		r = 0;
		for (int i{0}; i<=degree; ++i)
		{ 
			r += integ[i] * pow(xmax, i+1);
		}

		summa += M_PI * r * r;

		cout << "Case " << cs << ": " << fixed << setprecision(2) << summa << endl;
		if (step_vec.size() == 0)
		{
			cout << "insufficient volume" << endl;
		}
		else
		{
			for (int i{0}; i<step_vec.size(); ++i)
			{
				if (i > 0) {cout << " ";}
				cout << fixed << setprecision(2) << step_vec[i];
			}
			cout << endl;
		}




	}

}