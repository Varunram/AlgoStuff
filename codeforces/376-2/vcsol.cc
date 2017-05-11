#include<bits/stdc++.h>
#define N 1000010
#define ll long long
using namespace std;
int n,x,a[N],f[N];
ll ans;
int main()
{
	cin>>n;
	while(n--) scanf("%d",&x),a[x]++;
	for(int i=200000;i;i--) f[i]=f[i+1]+a[i];
	for(int i=1;i<=200000;i++)
	if(a[i])
	{
		ll sum=0;
		for(int j=i;j<=200000;j+=i) sum+=(ll)(f[j]-f[j+i])*j;
		ans=max(ans,sum);
	}
	cout<<ans;
}
