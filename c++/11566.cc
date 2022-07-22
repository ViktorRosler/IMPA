#include <bits/stdc++.h>

using namespace std;

int main() 
{
	ifstream cin("11566.txt");

	while (true) {
		int N,x,T,K;
		cin >> N >> x >> T >> K;

		// cout << N << " " << x << " " << T << " " << K << endl;

		if (N == 0) {break;}

		int max_cost = floor((double)(x * (N + 1)) / 1.1 + 1e-6) - (N + 1) * T;

		vector<pair<int, int>> items;
		for (int i{0}; i<K; ++i) {
			int value, sum, temp;
			sum = 0;
			cin >> value;
			for (int j{0}; j<=N; ++j) {
				cin >> temp;
				sum += temp;
			}

			items.push_back(make_pair(value, sum));
			items.push_back(make_pair(value, sum));
		}



		vector<vector<vector<int>>>dp(250,vector<vector<int>>(1200,vector<int>(30,0)));
		for (int i{1}; i<=items.size(); ++i) {
			for (int j{0}; j<=max_cost; ++j) {
				for (int k{1}; k<=2*(N+1); ++k) {
					if (items[i-1].first > j) {
						dp[i][j][k] = dp[i-1][j][k];
					} else {
						dp[i][j][k] = max(dp[i-1][j][k], 
							dp[i-1][j-items[i-1].first][k-1] + items[i-1].second);
					}
				}
			}
		}
		cout << fixed << setprecision(2) << (double)(dp[items.size()][max_cost][2*(N+1)]) / (N+1) << endl;
	}

}