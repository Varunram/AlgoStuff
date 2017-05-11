#include<iostream>
#include<algorithm>
using namespace std; using std::cin; using std::cout;

int main(){
  long long int n, ctr = 0, ctr1 = 0, ctr2 = 0;
  char str[100000];
  cin>>n;
  cin>>str;
  for(int i=1;i<n;i++){
    if(str[i] == 'b'){
      if(str[i-1] == 'b'){
        ctr1 ++; // painting the cockroach
        if(str[i+1] == 'r')
        { ctr2++; str[i]='r'; str[i+1] = 'b'; i++;}
        i++;  //swapping if possible bbr -> brb
      }
    } else if (str[i] == 'r'){
      if(str[i-1] == 'r'){
        ctr1++;
        if(str[i+1] == 'b')
        { ctr2 ++; str[i]='b'; str[i+1]='r'; i++;}
        i++;
      }
    }
  }
  cout<< ((ctr2 == 0)? ctr1 : (ctr1 == 0)? ctr2 : min(ctr1,ctr2));
}
