#include <bits/stdc++.h>

using namespace std;

int main()
{  
    ifstream cin("429.txt");

    int N;
    cin >> N;
    while (N--)
    {
        vector<string> words;
        
        string word;
        while (cin >> word, word != "*")
        {
            words.push_back(word);
        }

        cin.ignore();

        string line;
        while (getline(cin, line) && line != "")
        {
            stringstream ss(line);
            string s, t;
            ss >> s >> t; 

            // BFS
            queue<string> q;
            map<string, int> m;

            m[s] = 0;
            q.push(s);
            while (!q.empty() && m.count(t) == 0)
            {
                string u = q.front();
                q.pop();
                // Loop over every word in the dictionary.
                for (size_t i = 0; i < words.size(); ++i)
                {
                    const string &v = words[i];
                    if (m.count(v) == 0 && u.length() == v.length())
                    {
                        int diff = 0;
                        for (size_t j = 0; j < u.length(); ++j)
                            if (u[j] != v[j])
                                ++diff;
                        if (diff == 1)
                        {
                            m[v] = m[u] + 1;
                            q.push(v);
                        }
                    }
                }
            }    
            cout << s << " " << t << " " << m[t] << endl;
        }
        if (N > 0)
                cout << endl;
    }
}