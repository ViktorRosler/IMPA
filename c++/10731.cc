#include <bits/stdc++.h>

using namespace std;

int lines, ind;
string s;
vector<char> ss;
vector<string> strings;
map<int,char> dict;
map<char,int> dict2;

class Graph
{
	int vertices;
	list<int> *adjacency_lists;

public:
	Graph(int V)
	{
		vertices = V;
		adjacency_lists = new list<int>[V];
	}

	void addEdge(int v, int w)
	{
		adjacency_lists[v].push_back(w);
	}

	Graph getTranspose()
	{
		Graph g(vertices);
		for (int i{0}; i<vertices; ++i)
		{
			list<int>::iterator iter;
			for (iter = adjacency_lists[i].begin(); iter != adjacency_lists[i].end(); ++iter)
			{
				g.adjacency_lists[*iter].push_back(i);
			}
		}
		return g;
	}

	void DFSOrder(int v, bool visited[], stack<int> &Stack)
	{
		visited[v] = true;

		list<int>::iterator iter;
		for (iter = adjacency_lists[v].begin(); iter != adjacency_lists[v].end(); ++iter)
		{
			if (!visited[*iter]) {DFSOrder(*iter, visited, Stack);}
		}

		Stack.push(v);
	}

	void DFSUtil(int v, bool visited[])
	{
	    // Mark the current node as visited and print it
	    visited[v] = true;
	    
	    ss.push_back(dict[v]);
	  
	    // Recur for all the vertices adjacent to this vertex
	    list<int>::iterator i;
	    for (i = adjacency_lists[v].begin(); i != adjacency_lists[v].end(); ++i)
	        if (!visited[*i])
	            DFSUtil(*i, visited);
	}

	void SCCs()
	{
	    stack<int> Stack;
	  
	    // Mark all the vertices as not visited (For first DFS)
	    bool *visited = new bool[vertices];
	    for(int i = 0; i < vertices; i++)
	        visited[i] = false;
	  
	    // Fill vertices in stack according to their finishing times
	    for(int i = 0; i < vertices; i++)
	        if(visited[i] == false)
	            DFSOrder(i, visited, Stack);
	  
	    // Create a reversed graph
	    Graph gr = getTranspose();
	  
	    // Mark all the vertices as not visited (For second DFS)
	    for(int i = 0; i < vertices; i++)
	        visited[i] = false;
	  
	    // Now process all vertices in order defined by Stack
	    while (Stack.empty() == false)
	    {
	        // Pop a vertex from stack
	        int v = Stack.top();
	        Stack.pop();
	  
	        // Print Strongly connected component of the popped vertex
	        if (visited[v] == false)
	        {
	            gr.DFSUtil(v, visited);

	            sort(ss.begin(), ss.end());
	            s = "";
	            for (int i{0}; i<ss.size(); ++i)
	            {
	            	if (i > 0) {s += " ";}
	            	s += ss[i];
	            }

	            strings.push_back(s);
	        	ss.clear();
	            
	        }
	    }
	}
};

int main() 
{
	ifstream cin("10731.txt");

	bool first = true;
	while (cin >> lines)
	{
		if (lines == 0) {break;}
		if (first) {first = false;}
		else {cout << endl;}

		vector<vector<int>> v;
		set<char> c;
		dict.clear();
		dict2.clear();
		strings.clear();
		ind = 0;
		
		for (int i{0}; i<lines; ++i)
		{
			v.push_back(vector<int>(0));
			for (int j{0}; j < 6; ++j)
			{
				char tmp;
				cin >> tmp;
				c.insert(tmp);

				int b = 0;
				if (dict2.count(tmp) == 1)
				{
					b = dict2[tmp];
				}
				else
				{
					b = ind;
					dict2[tmp] = b;
					dict[b] = tmp;
					++ind;
				}
				//cout << tmp << int(tmp) << endl;
				v[i].push_back(b);
			}
		}

		Graph g(c.size());
		for (int i{0}; i<lines; ++i)
		{
			int a = v[i][5];
			for (int j{0}; j < 5; ++j)
			{
				//cout << a << v[i][j] << endl;
				g.addEdge(a, v[i][j]);
			}
		}

		g.SCCs();

		sort(strings.begin(), strings.end());
		for (int i{0}; i < strings.size(); ++i)
		{
			cout << strings[i] << endl;
		}
	}
}