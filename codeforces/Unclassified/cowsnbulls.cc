#include<cstdio>
#include<algorithm>
#include<cstdlib>
using namespace std;

int notposs[10000], a[4], b[4], combs = 5040;

void todigit(int u){
	for (int i = 0; i < 4; i++ , u/=10)
	a[i] = u % 10;
}

int digitcheck(int u){
	int cnt[10] = {};
	for (int i = 0; i < 4; i++,u /= 10){
		cnt[u % 10]++;
		if (cnt[u % 10]>1)
		return 0;
	}
	return 1;
}

int nextnum(int u){
	while (1){
		u = (u + 1) % 10000;
		if (digitcheck(u) && !notposs[u])
			return u;
	}
}

void print(int u){
	todigit(u);
	for (int i = 0; i < 4; i++)
		printf("%c", '0' + a[i]), b[i] = a[i];
	printf("\n");
	fflush(stdout);
}

void looptr(int c, int d){
	for (int i = 0; i < 10000; i++){
		if (!digitcheck(i) || notposs[i])
			continue;
		int A = 0, B = 0;
		int cnt[10] = {}, cnt2[10] = {};
		todigit(i);
		for (int j = 0; j < 4; j++)
			if (a[j] == b[j])
				A++;  // Digits and position both match
			else
				cnt[a[j]]++, cnt2[b[j]]++;
		for (int j = 0; j < 10; j++)
			B += min(cnt[j], cnt2[j]); // Digit match only
		if (A != c || B != d) // Checkign whether both the numbers match
			notposs[i] = 1, combs--;
	}
}

int main() {
	srand(12345);
	while (1)
	{
		int p = nextnum(0);
		for (int t = rand() % combs; t > 0; t--)
		p = nextnum(p);
		print(p);
		int c, d;
		scanf("%d%d", &c, &d);
		if (c == 4)
			break;
		looptr(c, d);
	}
}
