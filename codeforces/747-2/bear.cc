#include<iostream>
#include<algorithm>
using namespace std;
using std::cin;
using std::cout;

int main(){
  int t[200000], neg[200000], diff[200000];
  int cnt =0, n,k, switches;
  cin>>n>>k;

  for(int i=0;i<n; i++){
    cin>>t[i];
    if(t[i]<0)
    neg[cnt++] = i;
  }
  if(cnt==0){
    cout<<0;
  } else if(cnt>k){
    cout<<-1;
  }else{
    switches = cnt*2;
    k -= cnt;
    cnt --;
    for(int i=0;i<cnt;i++){
      diff[i] = neg[i+1] - neg[i] -1;
    }
    sort(diff, diff+cnt);
    for(int i=0;i<cnt;i++){
      if(k>=diff[i]){
        switches-=2;
        k -= diff[i];
      }
    }
    if(n - neg[cnt] -1 <=k){
      switches--;
    }
    cout<<switches;
  }
 return 0;
}
