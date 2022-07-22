#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int cases,rows,columns,days;
string row;

int main() 
{
	ifstream cin("10443.txt");

	cin >> cases;

	for (int i{0}; i<cases; ++i)
	{
 		cin >> rows >> columns >> days;

 		int map1[rows][columns];
 		int map2[rows][columns];

 		for (int j{0}; j<rows; ++j)
 		{
 			cin >> row;

 			for (int k{0}; k<columns; ++k)
 			{
 				map1[j][k] = row[k];
 			}
 		}

 		for (int j{0}; j<days; ++j)
 		{
 			
 			for (int k{0}; k<rows; ++k)
 			{
 				for (int l{0}; l<columns; ++l)
 				{
 					char val,val2;

 					if (j % 2 == 0)
 					{
 						val = map1[k][l];
 						map2[k][l] = val;
 					}
 					else
 					{
						val = map2[k][l];
 						map1[k][l] = val;
 					}
 					

 					if (k > 0) 
 					{
 						j % 2 == 0 ? val2 = map1[k-1][l] : val2 = map2[k-1][l];
 						if (val == 'R' && val2 == 'P') {j % 2 == 1 ? map1[k][l] = 'P' : map2[k][l] = 'P';}
 						else if (val == 'P' && val2 == 'S') {j % 2 == 1 ? map1[k][l] = 'S' : map2[k][l] = 'S';}
 						else if (val == 'S' && val2 == 'R') {j % 2 == 1 ? map1[k][l] = 'R' : map2[k][l] = 'R';}
 					}

 					if (k+1 < rows) 
 					{
 						j % 2 == 0 ? val2 = map1[k+1][l] : val2 = map2[k+1][l];
 						if (val == 'R' && val2 == 'P') {j % 2 == 1 ? map1[k][l] = 'P' : map2[k][l] = 'P';}
 						else if (val == 'P' && val2 == 'S') {j % 2 == 1 ? map1[k][l] = 'S' : map2[k][l] = 'S';}
 						else if (val == 'S' && val2 == 'R') {j % 2 == 1 ? map1[k][l] = 'R' : map2[k][l] = 'R';}
 					}

 					if (l > 0) 
 					{
 						j % 2 == 0 ? val2 = map1[k][l-1] : val2 = map2[k][l-1];
 						if (val == 'R' && val2 == 'P') {j % 2 == 1 ? map1[k][l] = 'P' : map2[k][l] = 'P';}
 						else if (val == 'P' && val2 == 'S') {j % 2 == 1 ? map1[k][l] = 'S' : map2[k][l] = 'S';}
 						else if (val == 'S' && val2 == 'R') {j % 2 == 1 ? map1[k][l] = 'R' : map2[k][l] = 'R';}
 					}

 					if (l+1 < columns) 
 					{
  						j % 2 == 0 ? val2 = map1[k][l+1] : val2 = map2[k][l+1];
 						if (val == 'R' && val2 == 'P') {j % 2 == 1 ? map1[k][l] = 'P' : map2[k][l] = 'P';}
 						else if (val == 'P' && val2 == 'S') {j % 2 == 1 ? map1[k][l] = 'S' : map2[k][l] = 'S';}
 						else if (val == 'S' && val2 == 'R') {j % 2 == 1 ? map1[k][l] = 'R' : map2[k][l] = 'R';}						
 					}
 				}
 			}
 		}

 		if (i > 0) {cout << endl; }
 		if (days % 2 == 0)
 		{	
 			for (int j{0}; j<rows; ++j)
 			{
 				string s = "";
 				for (int k{0}; k<columns; ++k)
 				{	
 					s += map1[j][k];
 				}
 				cout << s << endl;
 			}
 		}
 		else
 		{
 			for (int j{0}; j<rows; ++j)
 			{
 				string s = "";
 				for (int k{0}; k<columns; ++k)
 				{	
 					s += map2[j][k];
 				}
 				cout << s << endl;
 			}

 		}


	}
}