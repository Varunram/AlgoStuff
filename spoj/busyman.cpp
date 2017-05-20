#include<iostream>
#include<algorithm>
using namespace std;
struct man{
  int start, end;
};
int cmp(man x1, man x2){
  if(x1.end<x2.end)
  return true;
  if(x1.end==x2.end)
  return (x1.start<x2.start);
  return false;
}
int main(){
  int n, cnt, prev, t;
  man x[1000000];
  scanf("%d", &t);
  while(t--){
    cnt =0;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
    scanf("%d%d", &x[i].start, &x[i].end);
    sort(x, x+n, cmp);
    cnt = 1;
    prev = x[0].end;
    for(int j=0;j<n;j++){
      if(x[j].start>=prev){
        cnt++;
        prev = x[j].end;
      }
    }
    printf("%d\n", cnt);
  }
  return 0;
}
