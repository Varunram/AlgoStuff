#include<iostream>
using namespace std; using std::cin; using std::cout;

int search(int i ,char a, char b[]){
  for(;i<strlen(b); i++){
    if(b[i] == a)
    return i;
  }
  return -1;
}
int main(){
  int j,k,t;
  k = -1;
  char a[1000], b[1000], swap[2000], rep1,rep2;
  cin>>a;
  cin>>b;
  for (int i=0;i<strlen(a); i++){
    j = search(i ,a[i],b);
    if ((j!= -1)&&(j!=i)){
      rep1 = b[i]; rep2 = b[j];
      for (int p=0;p<strlen(a); p++){
        if (b[p] == rep1)
        b[p]=rep2;
        if(b[p] == rep2)
        b[p]=rep1;
      }
    }
    cout<<b<<"\n";
  }
}
