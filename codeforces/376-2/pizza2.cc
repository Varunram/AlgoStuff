#include<algorithm>
#include<iostream>
using namespace std; using std::cin; using std::cout;

#define N 200000
int main(){
  int a[N], sum=0, n;
  cin >>n;
  for(int i=0;i<n;i++) cin>>a[i];
  a[n] = a[n+1] = 1;
  for (int i=0;i<n;i++){
    if ((a[i]%2 == 0)&&(a[i]>0)){
      a[i] = a[i] -2;
    } else if (a[i]>0){
      a[i] = a[i] - 1;
      a[i+1] = a[i+1] - 1;
    }
    sum += a[i];
  }
  cout<< (sum%2==0? "YES" : "NO");
}
