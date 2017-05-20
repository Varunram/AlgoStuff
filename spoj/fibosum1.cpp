// http://codeforces.com/blog/entry/14516
#include <map>
#include <iostream>
using namespace std;

#define long long long
const long M = 1000000007; // modulo
map<long, long> F;

long f(long n) {
	if (F.count(n)) return F[n];
	long k=n/2;
	if (n%2==0) { // n=2*k
		return F[n] = (f(k)*f(k) + f(k-1)*f(k-1)) % M;
	} else { // n=2*k+1
		return F[n] = (f(k)*f(k+1) + f(k-1)*f(k)) % M;
	}
}

int main(){
		long n1, sum, r1,r2;
		cin>>n1;
		while(n1--){
			sum=0;
			cin>>r1>>r2;
			F[0]= 1;
			F[1]=1;
			sum = sum+ f(r2+1) - f(r1+1) - 2;
			cout<<-f(r1) + f(r2-1+2);
		}
		return 0;
}
