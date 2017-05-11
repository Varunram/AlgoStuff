/*
#include<iostream>
#include<algorithm>
using namespace std;
using std::cin;
using std::cout;

int main(){
  long long int n, c[200000], d[200000], i, ctr, flag = 0;
  cin>>n;
  for(i=0; i<n ; i++){
    cin>>c[i]>>d[i];
    ctr = ctr - c[i];
  }
  if(n==1){cout<<"Infinity"; flag = 1;}
  else {
    for (i=1;i<n;i++){
      if((c[i] > 0) && (c[i-1] > 0) && (d[i] > d[i-1]))
      { cout<<"Impossible"; flag = 1;}
    }
  }
  cout<<ctr;
  if (flag == 0){
  cout<< (d[0] == 1? 1901 -ctr : 1899 - ctr); }
}
*/
#include<iostream>
#include<algorithm>
using namespace std;
using std::cin;
using std::cout;

int main(){
  long long int n, l ,r ,ctr, c, d;
  l = - 100000000;
  r = 100000000;
  ctr = 0;
  cin >>n;
  for(int i=0;i<n;i++){
    cin>>c>>d;
    d == 1? l = max(l,1900-ctr) : r = min(r, 1899 - ctr);
    ctr += c;
    if(l>r){
      cout<<"Impossible"<<endl;
      return 0;
    }
  }
  if (r>=100000000){
    cout<<"Infinity"<<endl;
    return 0;
  }
  cout<<r+ctr<<endl;
  return 0;
}
