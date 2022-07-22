// https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
#include <bits/stdc++.h>
using namespace std;

class Edge {
public:
	int src, dest, weight;
};


class Graph {
public:
	
	// V-> Number of vertices, E-> Number of edges
	int V, E;

	Edge* edge;
};

// Creates a graph with V vertices and E edges
Graph* createGraph(int V, int E) {
	Graph* graph = new Graph;
	graph->V = V;
	graph->E = E;

	graph->edge = new Edge[E];

	return graph;
}

// A structure to represent a subset for union-find
class subset {
public:
	int parent;
	int rank;
};


int find(subset subsets[], int i) {
	if (subsets[i].parent != i)
		subsets[i].parent
			= find(subsets, subsets[i].parent);
	return subsets[i].parent;
}

// A function that does union of two sets of x and y
// (uses union by rank)
void Union(subset subsets[], int x, int y) {
	int xroot = find(subsets, x);
	int yroot = find(subsets, y);

	// Attach smaller rank tree under root of high
	// rank tree (Union by Rank)
	if (subsets[xroot].rank < subsets[yroot].rank)
		subsets[xroot].parent = yroot;
	else if (subsets[xroot].rank > subsets[yroot].rank)
		subsets[yroot].parent = xroot;

	// If ranks are same, then make one as root and
	// increment its rank by one
	else {
		subsets[yroot].parent = xroot;
		subsets[xroot].rank++;
	}
}

// Compare two edges according to their weights.
// Used in qsort() for sorting an array of edges
int myComp(const void* a, const void* b)
{
	Edge* a1 = (Edge*)a;
	Edge* b1 = (Edge*)b;
	return a1->weight > b1->weight;
}

// The main function to construct MST using Kruskal's
// algorithm
int KruskalMST(Graph* graph)
{
	int V = graph->V;
	Edge result[V]; // Tnis will store the resultant MST
	int e = 0; // An index variable, used for result[]
	int i = 0; // An index variable, used for sorted edges

	qsort(graph->edge, graph->E, sizeof(graph->edge[0]),
		myComp);

	// Allocate memory for creating V ssubsets
	subset* subsets = new subset[(V * sizeof(subset))];

	// Create V subsets with single elements
	for (int v = 0; v < V; ++v)
	{
		subsets[v].parent = v;
		subsets[v].rank = 0;
	}

	// Number of edges to be taken is equal to V-1
	while (e < V - 1 && i < graph->E)
	{
		Edge next_edge = graph->edge[i++];

		int x = find(subsets, next_edge.src);
		int y = find(subsets, next_edge.dest);

		if (x != y) {
			result[e++] = next_edge;
			Union(subsets, x, y);
		}
		// Else discard the next_edge
	}

	int minimumCost = 0;
	for (i = 0; i < e; ++i){minimumCost = minimumCost + result[i].weight;}
	return minimumCost;
}

// Driver code
int main()
{
	int V; // Number of vertices in graph
	int E; // Number of edges in graph

	//ifstream cin("11631.txt");

	while (true) {
		cin >> V >> E;

		if ( V == 0 && E == 0) {break;}

		Graph* graph = createGraph(V, E);

		int total_cost = 0;
		for (int i{0}; i<E; ++i) {
			int x,y,z;
			cin >> x >> y >> z;

			graph->edge[i].src = x;
			graph->edge[i].dest = y;
			graph->edge[i].weight = z;

			total_cost += z;
		}

		int minimum_cost = KruskalMST(graph);

		cout << total_cost - minimum_cost << endl;

	}

}

