#include <bits/stdc++.h>

using namespace std;

int main() 
{
	//ifstream cin("10690.txt");

	int n, m;
	while(cin >> n >> m) {
		vector<int> input;
		int total = 0;
		int maxi = -999999999;
		int mini = 999999999;

		int temp;
		for(int i{0}; i< n+m; ++i) {
			cin >> temp;
			total += temp;
			input.push_back(temp);
		}

		int c = min(n,m);

		int dp[55][5200];
		for (int i{0}; i < 51; ++i) {
			for (int j{0}; j < 5100; ++j) {
				dp[i][j] = 0;
			}
		}

		dp[0][2550] = 1;
		for (int i{0}; i < input.size(); ++i) {
			vector<pair<int, int>> d;
			for (int j{0}; j <= i && j <= c; ++j) {
				for (int k{0}; k < 5100; ++k) {
					if (dp[j][k] == 1) {
						d.push_back(make_pair(j+1, k + input[i]));
					}
				}
			}
			for (int j{0}; j < d.size(); ++j) {
				dp[d[j].first][d[j].second] = 1;
			}
		}

		for (int i{0}; i < 5100; ++i) {
			if (dp[c][i] == 1) {
				maxi = max(maxi, (i - 2550) * (total - i + 2550));
				mini = min(mini, (i - 2550) * (total - i + 2550));
			}
		}

		cout << maxi << " " << mini << endl;

	}
	
}
