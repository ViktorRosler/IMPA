#include <bits/stdc++.h>

using namespace std;

int main() 
{
	ifstream cin("10029.txt");

	int size;
	unordered_map<string, int> words_map {};
	vector<string> words_vec {};
	for (size = 0; size<25005; ++size) {
		string s;
		cin >> s;
		if (s.length() > 0) {
			words_map[s] = size;
			words_vec.push_back(s);
		} else {
			break;
		}
	}
	// cout << words_map["dog"] << "  " << size << endl;

	vector<int> dp(25005, 0);
	int maxv = 0;
	for (int i = 0; i < size; ++i) {
		dp[i] = 1;
		string now = words_vec[i];
		int length = now.length();
		int point = -1;

		// delete
		for (int j = 0; j < length; ++j) {
			string New = "";
			for (int k = 0; k < length; ++k) {
				if (j != k) {
					New += now[k];
				}
			}
			if (words_map.find(New) != words_map.end() && dp[i] <= dp[words_map[New]]) {
				dp[i] = dp[words_map[New]] + 1;
			}
		}

		// add
		for (int j = 0; j <= length; ++j) {
			for (char k = 'a'; k < now[j]; ++k) {
				string New = "";
				for (int l = 0; l < length; ++l) {
					if (j == l) {
						New += k;
					}
					New += now[l];
				}
				if (words_map.find(New) != words_map.end() && dp[i] <= dp[words_map[New]]) {
					dp[i] = dp[words_map[New]] + 1;
				}
			}
		}

		// change
		for (int j = 0; j <= length; ++j) {
			for (char k = 'a'; k < now[j]; ++k) {
				string New = now;
				New[j] = k;
				if (words_map.find(New) != words_map.end() && dp[i] <= dp[words_map[New]]) {
					dp[i] = dp[words_map[New]] + 1;
				}
			}
		}

		maxv = max(maxv, dp[i]);
	}
	cout << maxv << endl;
}