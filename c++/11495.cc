#include <bits/stdc++.h>

using namespace std;

long long moves = 0;

vector<int> merge(vector<int> a, vector<int> b)
{
    int i,j = 0;
    vector<int> c;
    while (i < a.size() && j < b.size())
    {
        if (a[i] < b[j])
        {
            c.push_back(a[i]);
            i += 1;
        }
        else
        {
            c.push_back(b[j]);
            j += 1;
            moves += a.size()-i;
        }
    }

    while(i < a.size())
    {
        c.push_back(a[i]);
        i += 1;
    }

    while(j < b.size())
    {
        c.push_back(b[j]);
        j += 1;
    }

    return c;
}

vector<int> merge_sort(vector<int> a)
{
    if (a.size() < 2) {return a;}

    int m = a.size() / 2;
    vector<int> b(a.begin(), a.begin() + m);
    b = merge_sort(b);
    vector<int> c(a.begin() + m, a.end());
    c = merge_sort(c);
    vector<int> d = merge(b,c);


    return d;
}

int main() 
{
    //ifstream cin("11495.txt");

    int cnt;
    while (true) {
        
        cin >> cnt;
        if (cnt == 0) {break;}

        vector<int> asdf = {};

        for (int i{0}; i<cnt; ++i) {
            int tmp;
            cin >> tmp;
            asdf.push_back(tmp);
        }

        moves = 0;
        merge_sort(asdf);

        cout << (moves % 2 ? "Marcelo\n" : "Carlos\n");

    }

}