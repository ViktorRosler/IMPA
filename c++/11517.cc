
#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main()
{
	//ifstream cin("11517.txt");
	int cases;
	cin >> cases;

	while (cases--)
	{
		int price;
		int n;
		cin >> price >> n;

		vector<int> dp(10001, -1);
		vector<int> amount(10001, 0);

		dp[0] = 0;

		for (int i{0}; i < n; ++i)
		{
			int coin;
			cin >> coin;

			for (int j{price}; j > 0; --j)
			{
				int idx = j - coin;
				if (idx >= 0)
				{

					if (dp[idx] != -1)
					{
						int now = dp[idx] + coin;
						int use = amount[idx] + 1;
						if (now < dp[j] || dp[j] == -1)
						{
							dp[j] = now;
							amount[j] = use;
							
						}
						else if (now == dp[j] && amount[j] > use)
						{
							amount[j] = use;
						}
					}
	
				}
				else if (dp[j] == -1 || dp[j] >= coin)
				{
					dp[j] = coin;
					amount[j] = 1;
				}
			}

		}
		cout << dp[price] << " " << amount[price] << "\n";

	}


}