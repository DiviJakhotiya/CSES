#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n , x;
    cin >> n >> x;
    vector<int> F(n);
    for (int i = 0; i < n; i++) {
        cin >> F[i];
    }
    long long MOD = 1000000007;
    std::sort(F.begin(), F.end());
    vector<long long> dp(x + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= x; i++) {
        for (int coin : F) {
            if (i >= coin) {
                dp[i] = (dp[i] + dp[i - coin]) % MOD;
            }
        }
    }
    cout << dp[x] << endl;
}
