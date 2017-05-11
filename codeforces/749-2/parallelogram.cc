#include<iostream>
#include<algorithm>
using namespace std; using std::cin; using std::cout;

int main(){
  float x[3], y[3], midx[3], midy[3], finx[3], finy[3];
  for (int i=0; i<3;i++)
  cin>>x[i]>>y[i];
  midx[0] = (x[0]+x[1])/2;   midy[0] = (y[0]+y[1])/2;
  midx[1] = (x[1]+x[2])/2;   midy[1] = (y[1]+y[2])/2;
  midx[2] = (x[2]+x[0])/2;   midy[2] = (y[2]+y[0])/2;
  finx[0] = 2*midx[0] - x[2]; finy[0] = 2*midy[0] - y[2];
  finx[1] = 2*midx[1] - x[0]; finy[1] = 2*midy[1] - y[0];
  finx[2] = 2*midx[2] - x[1]; finy[2] = 2*midy[2] - y[1];
  cout<<3<<"\n";
  for(int i=0;i<3;i++){
    cout<<finx[i]<<" "<<finy[i]<<"\n";
  }
  return 0;
}
