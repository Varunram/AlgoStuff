#include<iostream>
#include<algorithm>
using namespace std; using std::cin; using std::cout;
#define N 200000
int main(){
  long long int n, a[N], sum[N], i,j,k;
  cin>>n;
  for(i=0;i<n;i++) cin>>a[i];
  for(i =0;i<n;i++) sum[i]=0;
  for(i=0;i<n;i++){
    for( j=0;j<n;j++){
      k = a[j];
      while((k>0)&&(k--%a[i]!=0));
      if (k!=0) sum[i]=sum[i]+k+1;
    }
  }
  if (n == 1)
  cout<<a[0];
  else
  cout<< *std::max_element(sum, sum+n);
  return 0;
}
