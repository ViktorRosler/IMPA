#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int dim[3] {1,1,1};
	int blocks, blocks2;
	int sq1, sq2;
	int sum;
	int ans;

	int cases;
	cin >> cases;
	for (int i = 0; i < cases; i++)
	{
		ans = 0xfffffff;
		cin >> blocks;
		sq1 = sqrt(blocks);

		for (int j = 1; j <= sq1; j++)
		{
			if (blocks % j == 0)
			{
				blocks2 = blocks / j;
				sq2 = sqrt(blocks2);
				for (int k = 1; k <= sq2; k++)
				{
					if (blocks2 % k == 0)
					{
						int l = blocks2 / k;
						sum = j*k*2 + j*l*2 + k*l*2;
						if (sum < ans) {ans = sum;}

					}
				}
			}
		}
		cout << ans << endl;
	}
	 
	return 0;	
	
}