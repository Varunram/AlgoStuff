#include<iostream>
#include<algorithm>
using namespace std; using std::cin; using std::cout;

int main(){
  int n, a[100],b[200], sum, i1, cnt; b[1] = 1; sum = 0; cnt = 0; i1 = 2;
  cin>>n;
  for(int i=1; i<=n; i++) cin>>a[i];

  for(int i=1;i<=n;i++)
  if(a[i] ==0) cnt++;

  if ((n== 1) && (a[1] == 0))
  { cout<<"NO"; return 0; }
  if (n - cnt !=0){
    cout<< n-(cnt);
    cout<<endl;
    for(int i=1;i<=n;i++){
      if (a[i] != 0){
        cout<<sum+1<<i<<" "<<endl;
        sum = i;
      }
      else{
        sum = i-1;
      }
    }
  } else {
    cout<<"NO"; return 0;
  }
}
