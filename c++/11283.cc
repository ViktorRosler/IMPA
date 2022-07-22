#include <bits/stdc++.h>

using namespace std;

int main() 
{
	//ifstream cin("11283.txt");

	int cases;
	cin >> cases;


	vector<vector<int>> con;
	con.push_back({1,4,5});
	con.push_back({0,2,4,5,6});
	con.push_back({1,3,5,6,7});
	con.push_back({2,6,7});
	con.push_back({0,1,5,8,9});
	con.push_back({0,1,2,4,6,8,9,10});
	con.push_back({1,2,3,5,7,9,10,11});
	con.push_back({2,3,6,10,11});
	con.push_back({4,5,9,12,13});
	con.push_back({4,5,6,8,10,12,13,14});
	con.push_back({5,6,7,9,11,13,14,15});
	con.push_back({6,7,10,14,15});
	con.push_back({8,9,13});
	con.push_back({8,9,10,12,14});
	con.push_back({9,10,11,13,15});
	con.push_back({10,11,14});

	string in = "";
	for (int i{0}; i<cases; ++i) {

		int points = 0;
		vector<char> board;
		for (int j{0}; j<4; ++j) {
			cin >> in;
			for (int k{0}; k<4; ++k) {
				board.push_back(in[k]);
				//cout << j*4 + k << in[k] << endl;
			}
		}

		int words;
		string word;
		cin >> words;
		for (int j{0}; j<words; ++j) {
			cin >> word;
			deque<vector<int>> chains;
			for (int k{0}; k<16; ++k) {
				if (board[k] == word[0]) {
					chains.push_back(vector<int>{k});
				}
			}
			for (int k{1}; k<word.length(); ++k){
				int b = chains.size();
				for (int l{0}; l<b; ++l) {
					vector<int> next = chains.front();
					chains.pop_front();
					for (auto val : con[next[next.size()-1]] ) {
						if (board[val] == word[k] && find(next.begin(), next.end(), val) == next.end())  {
							vector<int> tmp = next;
							tmp.push_back(val);
							chains.push_back(tmp);
						}
					}
				}
			}
			if (chains.size() > 0) {
				if (word.size() <= 4) {
					points += 1;
				} else if (word.size() == 5) {
					points += 2;
				} else if (word.size() == 6) {
					points += 3;
				} else if (word.size() == 7) {
					points += 5;
				} else if (word.size() >= 8) { 
					points += 11;
				}
			}
		}
		cout << "Score for Boggle game #" << i+1 << ": " << points << endl;


	}

}