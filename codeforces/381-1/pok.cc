// Partially referenced from Mr.Dindows' solution for implementation
#include<iostream>
#include<algorithm>
using namespace std;
using std::cin; using std::cout;
#define N 2000
int main(){
  int n,a1,b1,i,j,k;
  float a[N][N], p[N], u[N];
  cin>>n>>a1>>b1;
  for(i=0;i<n; i++)
  cin>>p[i];
  for(i=0;i<n;i++)
  cin>>u[i];

  for (i=0;i<n;i++){
    int mina = max(0, a1-n+i);
    int minb = max(0, b1-n+i);
    int maxa = min(a1, i);
    int maxb = min(b1, i);

    for(j=maxa; j>=mina; j--) for(k = maxb; k>=minb; k--){
      a[j+1][k] = max(a[j+1][k], (a[j][k] + p[i]));
      a[j][k+1] = max(a[j][k+1], (a[j][k] + u[i]));
      a[j+1][k+1] = max(a[j+1][k+1], a[j][k] + ((p[i]+u[i] - p[i]*u[i])));
    }
  }
  cout<<a[a1][b1];
  return 0;
}
