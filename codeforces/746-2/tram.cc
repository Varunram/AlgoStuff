#include<algorithm>
#include<iostream>
using namespace std;
using std::cin;
using std::cout;

int main(){
  int s,x1,x2,t1,t2,p,d,res;
  cin>>s>>x1>>x2>>t1>>t2>>p>>d;
  if(x1>x2){
    x1 = s-x1;
    x2 = s-x2;
    d*=-1;
    p = s-p;
  }
  p*=d;
  if(p>x1){
    p -= 2*s;
  }
  res = min((x2-x1)*t2,(x2-p)*t1);
  cout<<res<<endl;
  return 0;
}
