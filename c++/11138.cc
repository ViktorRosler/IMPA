// https://en.wikipedia.org/wiki/Hopcroft-Karp_algorithm

#include <bits/stdc++.h>

using namespace std;

bool bfs() {

}

bool dfs() {

}

int main() {
	int cases;
	cin >> cases;

	for (int i{0}; i<cases; ++i) {
		int bolts, nuts;
		cin >> bolts >> nuts;

		vector<vector<int>> data(nuts + bolts + 1, vector<int>);

		int inp;
		for (int j{0}; j<bolts; ++j) {
			for (int k{0}; k<nuts; ++k) {
				cin >> inp;
				if (inp) {data[j].push_back(k+bolts)}
			}
		}
	}


}