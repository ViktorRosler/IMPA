#include <bits/stdc++.h>

using namespace std;

#define INF 0x3f3f3f3f
  
// iPair ==> Integer Pair
typedef pair<long long, long long> iPair;
  
// To add an edge
void addEdge(vector <pair<long long, long long>> adj[], long long u, long long v, long long wt)
{
    adj[u].push_back(make_pair(v, wt));
    adj[v].push_back(make_pair(u, wt));
}
   
  
// Prints shortest paths from src to all other vertices
vector<long long int> shortestPath(vector<pair<long long,long long> > adj[], long long V, long long src)
{
    priority_queue< iPair, vector <iPair> , greater<iPair> > pq;
  
    vector<long long int> dist(V, INF);
  
    pq.push(make_pair(0, src));
    dist[src] = 0;

    while (!pq.empty())
    {
        long long u = pq.top().second;
        pq.pop();
  
  		for (int i{0}; i<adj[u].size(); ++i)
        //for (pair<long long,long long> x : adj[u])
        {
            long long v = adj[u][i].first;
            long long weight = adj[u][i].second;
  
            if (dist[v] > dist[u] + weight)
            {
                dist[v] = dist[u] + weight;
                pq.push(make_pair(dist[v], v));
            }
        }
    }

    return dist;
}

int main() 
{
	ifstream cin("10296.txt");

	while (true)
	{
		long long nodes, paths;
		cin >> nodes;

		if (cin >> paths)
		{
			vector<iPair> adj[nodes+1];
			long long degrees[nodes+1] = {0};
			long long total = 0;
			for (int i{0}; i<paths; ++i)
			{
				long long a,b,c;
				cin >> a >> b >> c;
			
				total += c;

				degrees[a] += 1;
				degrees[b] += 1;

				addEdge(adj, a, b, c);
			}

			vector<long long> odd;
			vector<vector<long long int>> distances(nodes+1);
			for (int i{1}; i<=nodes; ++i)
			{
				if (degrees[i] % 2 != 0)
				{
					odd.push_back(i);
					distances[i] = shortestPath(adj,nodes,i);
				}
			}

			long long extra = INF;
			for (int j{0}; j<100000; ++j)
			{
				random_shuffle(odd.begin(), odd.end());
				long long temp = 0;
        		for (int i{0}; i<odd.size(); i+= 2)
        		{
        			temp += distances[odd[i]][odd[i+1]];
        		}
        		if (temp < 0) {continue;}
        		extra = min(extra, temp);
    		} 

			cout << total + extra << endl;
		}
		else {break; }
	}
	return 0;
}