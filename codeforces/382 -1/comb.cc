#include<cstdio>
#include <algorithm>
#define N 3000
int m, n, a[N], b[N];
char ans[N][N];

inline bool comp(int x, int y){
   return a[x] > a[y];
}

bool missval() {
  int currarr = 0, maxavail = 0;
  for (int i = 1; i <= n; i++){
     if ((currarr += a[i]) > (maxavail += 2 * (m - i)))
     return false;
   }
  for (int i = n + 1; i <= m; i++) {
    maxavail += 2 * (m - i);
    a[i] = std::min(a[i - 1], maxavail - currarr);
    currarr += a[i];
    if (currarr > maxavail)
    return false;
  }
  return currarr == maxavail;
}

int main() {
  scanf("%d%d",&m,&n);
  for (int i = 1; i <= n; ++i)
  scanf("%d",&a[i]);
  if (!missval()){
  puts("no");
  return 0;
  }
  for (int i = 1; i <= m; i++) {
    ans[i][i] = 'X';
    for (int j = i + 1; j <= m; j++)
    b[j] = j;
    std::sort(b+1+i,b+1+m,comp); //using object as comp
    for (int j = m; j > i; j--) {
      int k = b[j];
      if (a[i] >= 2) {
        ans[i][k] = 'W';
        ans[k][i] = 'L';
        a[i] -= 2;
      } else if (a[i] == 1) {
        ans[i][k] = ans[k][i] = 'D';
        a[i] --;
        a[k] --;
      } else {
        ans[i][k] = 'L';
        ans[k][i] = 'W';
        a[k] -= 2;
      }
    }
  }
  puts("yes");
  for (int i = 1; i <= m; i++)
  puts(ans[i]+1);
  return 0;
}
