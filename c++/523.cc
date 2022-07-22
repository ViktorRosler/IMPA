#include <bits/stdc++.h>

using namespace std;

int main() 
{
	ifstream cin("523.txt");

	int cases, tmp;
	cin >> cases;

	string st;
	getline(cin, st);
	getline(cin, st);

	for (int i{0}; i<cases; ++i) {
		if (i > 0) {cout << endl;}
		vector<vector<int>> matrix;
		matrix.push_back(vector<int>{});
		getline(cin, st);
		stringstream ss(st);
		int n = 0;
		while(ss>>tmp) {
			if (tmp == -1) {matrix[0].push_back(999999999);}
			else {matrix[0].push_back(tmp);}
			++n;
		}
		for (int j{1}; j<n; ++j) {
			matrix.push_back(vector<int>{});
			getline(cin, st);
			stringstream ss(st);
			while(ss>>tmp) {
				if (tmp == -1) {matrix[j].push_back(999999999);}
				else {matrix[j].push_back(tmp);}	
			}
		}
		vector<int> taxes;
		getline(cin, st);
		stringstream ss2(st);
		while(ss2>>tmp) {
			taxes.push_back(tmp);
		}
		vector<vector<int>> nexts;
		for (int j{0}; j<n; ++j) {
			nexts.push_back(vector<int>{});
			for (int k{0}; k<n; ++k) {
				nexts[j].push_back(k);
			}
		}
		
		for (int u{0}; u<n; ++u) {
			for (int s{0}; s<n; ++s) {
				if (matrix[s][u] != 999999999) {
					for (int t{0}; t<n; ++t) {
						// cout << matrix[u][t] << " " << matrix[s][t] << " " << taxes[u] << " " << matrix[u][t] << endl;
						if (matrix[u][t] != 999999999 && matrix[s][t] > matrix[s][u] + taxes[u] + matrix[u][t]) {			
							matrix[s][t] = matrix[s][u] + taxes[u] + matrix[u][t];
							nexts[s][t] = nexts[s][u];
						}
					}
				}

			}
		}

		bool printed = false;
		while (true) {
			getline(cin, st);

			if (st == "") {break;}
			stringstream ss3(st);
			int s,e,u;
			ss3 >> s >> e;
			if (printed) {
				cout << endl;
			} else {
				printed = true;
			}
			--s;
			--e;
			cout << "From " << s+1 << " to " << e+1 << " :" << endl;
			cout << "Path: " << s+1;
			if (s != e) {
				u = s;
				while (u != e) {
					u = nexts[u][e];
					cout << "-->" << u+1;
				}
			}
			cout << endl;
			cout << "Total cost : " << matrix[s][e] << endl;
		}


	}

}