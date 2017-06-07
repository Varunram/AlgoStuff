// Program to count substrings which are
// divisible by 8 but not by 3
#include <bits/stdc++.h>
using namespace std;
#define MAX 1000

// Returns count of substrings divisible by 8
// but not by 3.
int count(char s[], int len)
{
    int cur = 0, dig = 0;
    int sum[MAX], dp[MAX][3];

    memset(sum, 0, sizeof(sum));
    memset(dp, 0, sizeof(dp));

    dp[0][0] = 1;

    // Iterating the string.
    for (int i = 1; i <= len; i++)
    {
        dig = int(s[i-1])-48;
        cur += dig;
        cur %= 3;

        sum[i] = cur;

        // Prefix sum of number of substrings whose
        // sum of digits mudolo 3 is 0, 1, 2.
        dp[i][0] = dp[i-1][0];
        dp[i][1] = dp[i-1][1];
        dp[i][2] = dp[i-1][2];

        dp[i][sum[i]]++;
    }

    int ans = 0, dprev = 0, value = 0, dprev2 = 0;

    // Iterating the string.
    for (int i = 1; i <= len; i++)
    {
        dig = int(s[i-1])-48;

        // Since single digit 8 is divisible
        // by 8 and not by 3.
        if (dig == 8)
            ans++;

        // Taking two digit number.
        if (i-2 >= 0)
        {
            dprev = int(s[i-2])-48;  // 10th position
            value = dprev*10 + dig;  // Complete 2 digit
                                     // number

            if ((value%8 == 0) && (value%3 != 0))
                ans++;
        }

        // Taking 3 digit number.
        if (i-3 >= 0)
        {
            dprev2 = int(s[i-3])-48; // 100th position
            dprev  = int(s[i-2])-48;  // 10th position

            // Complete 3 digit number.
            value = dprev2*100 + dprev*10 + dig;

            if (value%8 != 0)
                continue;

            // If number formed is divisible by 8 then
            // last 3 digits are  also divisible by 8.
            // Then all the substring ending at this
            // index is divisible.
            ans += (i-2);

            // But those substring also contain number
            // which are not divisible by 3 so
            // remove them.
            ans -= (dp[i-3][sum[i]]);
        }
    }

    return ans;
}

// Driven Program
int main()
{
    char str[] = "6564525600";
    int len = strlen(str);
    cout << count(str, len) <<endl;
    return 0;
}
