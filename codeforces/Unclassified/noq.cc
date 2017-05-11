#include<iostream>
#include<algorithm>
using namespace std; using std::cin; using std::cout;

int main(){
  long long int n ,i,j,ans[3000], a[3000], b[3000];
  cin>>n;
  for(int i=1;i<=n;i++){
    cin>>a[i];
    a[i] = a[i] - i;
    b[i] = a[i];
  }
  sort(b+1, b+n+1);
  for(i=1;i<=n;i++){
    for(j=1;j<=n;j++){
      ans[j] += abs(a[i] - b[j]);
      if(j>1) ans[j] = min(ans[j], ans[j-1]);
    }
  }
  cout<<ans[n]<<" ";
  return 0;
}
