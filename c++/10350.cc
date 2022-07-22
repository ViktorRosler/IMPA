#include <bits/stdc++.h>

using namespace std;

int main() 
{
	string s;

	//ifstream cin("10350.txt");

	while (cin >> s) {
		int n,m;
		cin >> n >> m;

		int dist[120][15];

		for (int i=0; i < 120; i++){
        	for (int j=0; j < 15; j++){
            	dist[i][j] = (i == 0 ? 0 : 1e9);
        	}
    	}

    	for (int k=0; k < (n - 1); k++){
       		for (int i=1; i <= m; i++){
            	for (int j=1; j <= m; j++){
                	int travel_cost;
                	cin >> travel_cost;
                	dist[k + 1][j] = min(dist[k + 1][j], dist[k][i] + travel_cost + 2);
            	}
        	}
    	}
    	int lo = 1e9;

    	for (int i=1; i <= m; i++){
        	lo = min(lo, dist[n - 1][i]);
    	}

    	cout << s << endl;
    	cout << lo << endl;

	}

}