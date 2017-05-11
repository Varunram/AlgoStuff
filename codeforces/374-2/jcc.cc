#include<iostream>
#include<algorithm>
#include<string>
using namespace std; using std::cin; using std::cout;

int main(){
  int i, count =0;int ls= 0; int count1 = 0; char c[100]; int n;
  cin>>n;
  cin>>c;
  ls = c[0] == 'B'? 1: -1;
  for(int i=1;i<n;i++){
    if((c[i] == 'W') && (c[i-1] == 'B'))
    ls ++;
  }
  cout<<ls<<endl;
  for(int i=0;i<n;i++){
    if(c[i]=='B')
    count ++;
    else if(count != 0){
      cout<<count<<" ";
      count =0;
      count1++;
    } else {
      count1++;
    }
  }
  if(count != 0)
  cout<<count<<" ";
  if (count1 == strlen(c))
  cout<<"0 ";
}
