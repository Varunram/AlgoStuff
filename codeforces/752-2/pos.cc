#include<iostream>
using namespace std; using std::cin; using std::cout;

int main(){
  long int n,m,k,r,d;
  char s;
  cin>>n>>m>>k;
  s= k%2==0? 'R' : 'L';
  r = k%(2*m)==0? (k/(2*m)) : (k/(2*m)+1);
  k = k-(k/(2*m))*(2*m);
  d = k==0? m : k%2==0? k/2 : k/2+1;
  cout<<r<<" "<<d<< " "<<s;
}
