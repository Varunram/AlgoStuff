#include<iostream>
#include<algorithm>
#include<string>
using namespace std; using std::cin; using std::cout;

int main(){
  long long int x, sum, n, flag; char a[10000]; sum =flag=0;
  cin>>n;
  for (int i=0;i<n;i++){
    cin>>x;
    cin>>a;
    if (a[0]=='S'){
      sum += x;
    } else if (a[0] == 'N'){
      sum -= x;
    } else {
      if ((sum==0) || (sum == 20000)){
        flag = 0;
      }
    }
    if((sum < 0) || (sum > 20000))
    { flag = 0; sum =-1;}
  }
  if (sum==0){flag = 1;}
  else if(sum>0){flag = 0;}
  if (flag == 0)
  cout<<"NO";
  else
  cout<<"YES";
}
