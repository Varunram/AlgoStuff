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
