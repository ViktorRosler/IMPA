#include <bits/stdc++.h>

using namespace std;

int main() 
{
	ifstream cin("1079.txt");

	int c = 0;
	int n;

	while (true) {
		cin >> n;

		if (n == 0) {break;}

		vector<pair<double, double>> a;
		for (int i{0}; i<n; ++i) {
			double s,t;
			cin >> s >> t;
			a.push_back(make_pair(s*60,t*60));
		}
		sort(a.begin(), a.end());

		double m = -1;
		do {
			double low = 0;
			double high = 1440 * 60;
			double best = -1;
			while (fabs(low - high) >= 0.1) {
				double mid = (low + high) / 2.0;
		
				bool doable = true;
				double current = 0;
				for (int j{0}; j<a.size(); ++j) {
					if (j == 0) {
						current = a[j].first;
					} else if (j == a.size() - 1) {
						if (current + mid <= a[j].second) {break;}
						doable = false;
					} else {
						if (a[j].first > current + mid) {
							current = a[j].first;
						} else if (a[j].second >= current + mid) {
							current += mid;
						} else {
							doable = false;
							break;
						}
					}
				}
				if (doable) {
					low = mid;
					best = max(best, mid);
				}
				else {high = mid;}
			}
			m = max(m, best);
		} while (next_permutation(a.begin(), a.end()));
		m = (int)(m + 0.5);
		string s;
		if ((int)m%60 < 10) {
			s = "0" + to_string((int)m%60);
		} else {
			s = to_string((int)m%60);
		}

		cout << "Case " << ++c << ": " << (int)m/60 << ":" << s << endl;

	}
	

}