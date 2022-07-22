#include <stdio.h>
  
using namespace std;

int main() {
  int roadmap = 1;
  int roads;
  int points;
  int ans;
  double neg,pos;

  int a[3000], b[3000], c[3000];
  int x[100], y[100];

  while(scanf("%d", &roads) == 1) {

    if (roads == 0) {
      return 0;
    }

    
    for(int i = 0; i < roads; i++)
      scanf("%d %d %d", &a[i], &b[i], &c[i]);

    
    scanf("%d", &points);
    for(int i = 0; i < points; i++)
      scanf("%d %d", &x[i], &y[i]);

    ans = 0;
    for(int p = 0; p < points; p++) {
      neg = 0;
      pos = 0;
      for(int i = 0; i < roads; i++) {
        if (a[i]*x[p]+b[i]*y[p]+c[i] > 0) {
          pos++;
        } else {
          neg++;
        }
      }
      ans += pos*(pos-1)/2;
      ans += neg*(neg-1)/2;
    } 

    printf("Roadmap %d:\n", roadmap);
    printf("Negative Builders Ltd. will build %d New Roads.\n", ans);
    roadmap++;
  }

  return 0;
}