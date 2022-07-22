//  Created by Sengxian on 2/14/16.
//  Copyright (c) 2015年 Sengxian. All rights reserved.
//  UVa 662 DP + 决策优化
#include <bits/stdc++.h>
#define br putchar('\n');
using namespace std;

inline int ReadInt() {
    int n = 0, ch = getchar(); bool flag = false;
    while(!isdigit(ch)) flag |= ch == '-', ch = getchar();
    while(isdigit(ch)) n = (n << 3) + (n << 1) + ch - '0', ch = getchar();
    return flag ? -n : n;
}
const int maxn = 200 + 3, maxk = 30 + 3, INF = 0x3f3f3f3f;
int n, K, pos[maxn], sum[maxn];
int dp[maxn][maxk];
typedef pair<int, int> state;
state choice[maxn][maxk];

inline int Sum(int i, int j) {
    return sum[j] - sum[i - 1];
}

inline int cost(int i, int j, int &c) {
    c = (i + j) / 2; //选择中位数建立
    return pos[c] * (2 * c - i - j) - Sum(i, c - 1) + Sum(c + 1, j);
}

void print(int i, int j) {
    if(i == 0 && j == 0) return;
    print(choice[i][j].first - 1, j - 1);
    if(choice[i][j].first == i) printf("Depot %d at restaurant %d serves restaurant %d\n", j, choice[i][j].second, i);
    else printf("Depot %d at restaurant %d serves restaurants %d to %d\n", j, choice[i][j].second, choice[i][j].first, i);
}

void solve() {
    memset(dp[0], INF, sizeof(dp[0]));
    dp[0][0] = 0;
    for(int i = 1; i <= n; ++i) {
        memset(dp[i], INF, sizeof(dp[i]));
        for(int j = 1; j <= min(K, i); ++j)
            for(int k = j; k <= i; ++k) {
                int c, val = dp[k - 1][j - 1] + cost(k, i, c);
                if(val < dp[i][j]) choice[i][j] = state(k, c), dp[i][j] = val;
            }
    }
    print(n, K);
    printf("Total distance sum = %d\n\n", dp[n][K]);
}

int main() {
    //ifstream cin("662.txt");
    int caseNum = 0;
    while(n = ReadInt(), K = ReadInt(), n + K) {
        sum[0] = 0;
        for(int i = 1; i <= n; ++i)
            sum[i] = (pos[i] = ReadInt()) + sum[i - 1];
        printf("Chain %d\n", ++caseNum);
        solve();
    }
    return 0;
}