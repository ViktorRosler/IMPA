#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int scen,x,y,x_pos,y_pos,beepers,mini,beeper_pos[11][2];
map<tuple<int,int>,int> dic;


void calc(vector<int> a, int b)
{
	if (a.size() == beepers)
	{
		if (!dic.count(make_tuple(a[a.size()-1],-1)))
		{
			dic[make_tuple(a[a.size()-1],-1)] = abs(x_pos - beeper_pos[a[a.size()-1]][0]) + abs(y_pos - beeper_pos[a[a.size()-1]][1]);
			dic[make_tuple(-1,a[a.size()-1])] = dic[make_tuple(a[a.size()-1],-1)];
		}
		int c = b + dic[make_tuple(a[a.size()-1],-1)];
		mini = min(mini,c);
		return;
	}

	for (int i{0}; i<beepers; ++i)
	{
		bool go_on = true;
		for (int j{0}; j<a.size(); ++j)
		{
			if (a[j] == i) go_on = false;
		}

		if (!go_on) continue;

		if (!dic.count(make_tuple(a[a.size()-1],i)))
		{
			dic[make_tuple(a[a.size()-1],i)] = abs(beeper_pos[i][0] - beeper_pos[a[a.size()-1]][0]) + abs(beeper_pos[i][1] - beeper_pos[a[a.size()-1]][1]);
			dic[make_tuple(i,a[a.size()-1])] = dic[make_tuple(a[a.size()-1],i)];
		}
		vector<int> c = a;	
		int d = b;
		d += dic[make_tuple(c[c.size()-1],i)];
		c.push_back(i);
		calc(c,d);

	}


}

int main() 
{
	ifstream cin("10496.txt");

	

	cin >> scen;

	for (int i{0}; i< scen; ++i)
	{

		cin >> x >> y >> x_pos >> y_pos >> beepers;

		mini = 999999;

		for (int j{0}; j<beepers; ++j)
		{
			cin >> x >> y;
			beeper_pos[j][0] = x;
			beeper_pos[j][1] = y;
		}

		for (int j{0}; j<beepers; ++j)
		{
			dic[make_tuple(-1,j)] = abs(x_pos - beeper_pos[j][0]) + abs(y_pos - beeper_pos[j][1]);
			dic[make_tuple(j,-1)] = dic[make_tuple(-1,j)];
			vector<int> a = {j};
			calc(a,dic[make_tuple(-1,j)]);
		}


		cout << mini << endl;

	}


}