#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int nr_airports;
double a,b;
int distances[1000][1000];

#define earthRadiusKm 6371.0

// This function converts decimal degrees to radians
double deg2rad(double deg) {
  return (deg * M_PI / 180);
}

//  This function converts radians to decimal degrees
double rad2deg(double rad) {
  return (rad * 180 / M_PI);
}

/**
 * Returns the distance between two points on the Earth.
 * Direct translation from http://en.wikipedia.org/wiki/Haversine_formula
 * @param lat1d Latitude of the first point in degrees
 * @param lon1d Longitude of the first point in degrees
 * @param lat2d Latitude of the second point in degrees
 * @param lon2d Longitude of the second point in degrees
 * @return The distance between the two points in kilometers
 */
double distanceEarth(double lat1d, double lon1d, double lat2d, double lon2d) {
  double lat1r, lon1r, lat2r, lon2r, u, v;
  lat1r = deg2rad(lat1d);
  lon1r = deg2rad(lon1d);
  lat2r = deg2rad(lat2d);
  lon2r = deg2rad(lon2d);
  u = sin((lat2r - lat1r)/2);
  v = sin((lon2r - lon1r)/2);
  return 2.0 * earthRadiusKm * asin(sqrt(u * u + cos(lat1r) * cos(lat2r) * v * v));
}

int main() 
{
	ifstream cin("10316.txt");
	
	while (cin >> nr_airports)
	{
		
		vector<pair<double,double>> airports;
		
		for (int i{0}; i<nr_airports; ++i)
		{
			cin >> a >> b;
			airports.push_back(make_pair(a,b));	
		}

		int mm = 1000000;
		int ap;
		for (int i{0}; i<nr_airports; ++i)
		{
			int m = 0;
			for (int j{0}; j<nr_airports; ++j)
			{
				if (i==j) 
				{
					distances[i][j] = 0;
					distances[j][i] = distances[i][j];
				}
				else if (distances[i][j] == 0)
				{
					distances[i][j] = distanceEarth(airports[i].first, airports[i].second, airports[j].first, airports[j].second);
					distances[j][i] = distances[i][j];

				}

				if (distances[i][j] > m)
				{
					m = distances[i][j];
				}
				
			}
			if (m <= mm)
			{
				ap = i;
				mm = m;
			}
		}
		memset(distances, 0, sizeof distances);
		cout << fixed << setprecision(2) << airports[ap].first << " " << airports[ap].second << endl;
	}
}

