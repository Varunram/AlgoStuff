#include<iostream>
#include<algorithm>

using namespace std; using std::cin; using std::cout;
int max(int n){
  int sum = 0;
  for(int i=1;i<=n;i++)
  sum += 5*i;
  return sum;
}
int main(){
  int n,k, i=1;
  cin>>n>>k;
  k = 240 - k;
  while(true){
    if(max(i) > k)
    break;
    i++;
  }
  cout<< (n > i-1 ? i-1 : n);
  return 0;
}
