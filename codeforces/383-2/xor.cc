#include<bits/stdc++.h>
int main(){
  long long int n,x,m[200000],a,b =0,i;
  std::cin>>n>>x;
  for( i =0; i<n;i++){
    std::cin>>a;b+=m[x^a]; m[a]++;
  }
  std::cout<<b;
}
