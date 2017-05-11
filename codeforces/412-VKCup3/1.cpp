#include<iostream>
#include<algorithm>

using namespace std;
int main(){
  int a[1000][1000], b[1000][1000], n;
  cin>>n;
  for(int i=0;i<n;i++){
    cin>>a[i][0]>>a[i][1];
    if(a[i][1] != a[i][0]){
      cout<<"rated";
      exit(0);
    }
  }
  for(int i=0;i<n-1;i++){
    if(a[i][0] < a[i+1][0]){
      if((a[i][0] == a[i][1]) && (a[i+1][0] == a[i+1][1])){
        cout<<"unrated";
        exit(0);
      }
      cout<<"rated";
      exit(0);
    }
  }
  cout<<"maybe";
}
