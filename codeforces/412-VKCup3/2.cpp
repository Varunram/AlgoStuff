#include<iostream>
#include<algorithm>

using namespace std;

int check(int x, int p){
  int i,j;
  j=0;
  i = (x/50)%475;
  while(j<25){
    i = (i*96+42)%475;
    if(26+i == p)
    return true;
    j++;
  }
  return false;
}
int main(){
  int p,x,y,ctr,var;
  ctr = 0;
  cin>>p>>x>>y;

  while(x>=y){
    var = check(x,p);
    if(var){
      cout<<0;
      exit(0);
    }
    x-=50;
    ctr++;
  }
  x+=ctr*50;
  ctr = 0;
  while(x>=y){
    var = check(x,p);
    if(var){
      if(ctr%2 == 0)
      {cout<<ctr/2; exit(0); }
      else
      {cout<<ctr/2+1;}
      exit(0);
    }
    x +=50;
    ctr++;
  }
  return 0;
}
