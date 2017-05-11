#include<iostream>
#include<string>
using namespace std;
using std::cin;
using std::cout;
int main(){
  long long int n, i, dem, rep, cntr;
  char a[200000];
  int sum =0, val[200000];
  cin>>n;
  cin>>a;
  for(i=0;i<n;i++){
    if (a[i]=='D'){
      val[i] = 1;
    } else {
      val[i] = -1;
    }
  }
  while(true){
    dem = rep = 0;
    for (i=0;i<n;i++) {
      if (val[i] == 1) dem ++;
      if (val[i] == -1) rep ++;
    }
    if(dem == 0){
      printf("%c",'R');
      return 0;
    }
    if (rep == 0){
      printf("%c",'D');
      return 0;
    }
    for(int i=0;i<n;i++){
      if(cntr*val[i] < 0){ //If the current vote is an enemy's, cancel it
      cntr +=val[i];
      val[i] = 0;
      } else cntr+=val[i];
    }
  }
}
