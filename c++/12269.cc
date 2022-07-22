#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int x, y;
	double width;
	bool done;
	
	while (true)
	{
		cin >> x >> y >> width;
		if (x == 0 && y == 0)
		{
			return 0;
		}

		done = false;

		vector<double> xv;
		xv.clear();
		for (int i = 0; i < x; i++)
		{
			double temp;
			cin >> temp;
			xv.push_back(temp);	
		}

		sort(xv.begin(), xv.end());
		if (xv[0] - width/2 > 0 || xv[xv.size()-1] + width/2 < 75) {done = true;}
		for (int i = 0; i < xv.size()-1; i++)
		{
			if (xv[i] + width < xv[i+1]){done = true;} 
		}

		vector<double> yv;
		yv.clear();
		for (int i = 0; i < y; i++)
		{
			double temp;
			cin >> temp;
			yv.push_back(temp);	
		}

		sort(yv.begin(), yv.end());
		if (yv[0] - width/2 > 0 || yv[yv.size()-1] + width/2 < 100) {done = true;}
		for (int i = 0; i < yv.size()-1; i++)
		{
			if (yv[i] + width < yv[i+1]){done = true;} 
		}

		if (done)
		{
			cout << "NO" << endl;
			continue;
		}

		cout << "YES" << endl;

	}

}