#include <bits/stdc++.h>

using namespace std;

int main() 
{
	ifstream cin("10278.txt");
	int cases;

	cin >> cases;

	for (int i{0}; i<cases; ++i) {
		int x,y,dist;
		int nr_stations;
		int nr_intersections;
		int intersections[501][501];
		int firestations[101];

		cin >> nr_stations >> nr_intersections;

		for (int j{0}; j<501; ++j) {
			for (int k{0}; k<501; ++k) {
				intersections[j][k] = 999999999;
			}
			intersections[j][j] = 0;
		}

		for (int j{0}; j<nr_stations; ++j) {
			cin >> firestations[j];
		}

		string line;
		getline(cin,line);
		while (true) {
			getline(cin,line);
			if (line.empty()) {break;}

			string x_s = line.substr(0, line.find(" "));
			line.erase(0, line.find(" ") + 1);
			string y_s = line.substr(0, line.find(" "));
			line.erase(0, line.find(" ") + 1);

			intersections[stoi(x_s)][stoi(y_s)] = stoi(line);
			intersections[stoi(y_s)][stoi(x_s)] = stoi(line);
		}

		//cout << nr_stations << " " << nr_intersections << endl;

		// Floyd–Warshall algorithm
		for (int j{1}; j <= nr_intersections; ++j) {
			for (int k{1}; k <= nr_intersections; ++k) {
				for (int l{1}; l <= nr_intersections; ++l) {
					if (intersections[k][l] > intersections[k][j] + intersections[j][l]) {
						intersections[k][l] = intersections[k][j] + intersections[j][l];
					}
				}
			}
		}

		int station;
		int max_dist = 999999999;
		for (int j{1}; j<=nr_intersections; ++j) {
			int current_max_dist = 0;
			for (int k{1}; k<=nr_intersections; ++k) {
				int current_dist = intersections[k][j];
				for (int l{0}; l<nr_stations; ++l) {
					current_dist = min(current_dist, intersections[k][firestations[l]]);
				}
				current_max_dist = max(current_dist, current_max_dist);
			}
			if (current_max_dist < max_dist) {
				station = j;
				max_dist = current_max_dist;
			}
		}


		if (i > 0) {cout << endl;}
		cout << station << endl;


		

	}

}