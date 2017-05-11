#include<iostream>
#include<algorithm>
using namespace std; using std::cin; using std::cout;
int a[10000],n;

int min(int x){
  long int min = 100000000;
  for(int i=0;i<n-x;i++){
    if((a[i+x] - a[i])<min)
    min = a[i+x] - a[i];
  }
  return min;
}
int max(int x){
  long int max = -100000000;
  for(int i=0;i<n-x;i++){
    if((a[i+x] - a[i])>max)
    max = a[i+x] - a[i];
  }
  return max;
}

int main(){
  cin>>n;
  for(int i=0;i<n; i++)
  cin>>a[i];
  //min(2) = 2
  //max(1) = 4
  cout<<(min(2) > max(1)? min(2) : max(1));
}
