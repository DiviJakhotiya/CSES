#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;
//actual working solution time complexity is exactly the same as my python solution
int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {

            if (i == j) {
                dp[i][j] = 0;
            } else {
                dp[i][j] = INT_MAX;

                // vertical cuts
                for (int k = 1; k < i; k++) {
                    dp[i][j] = min(dp[i][j],
                                   dp[k][j] + dp[i - k][j] + 1);
                }

                // horizontal cuts
                for (int k = 1; k < j; k++) {
                    dp[i][j] = min(dp[i][j],
                                   dp[i][k] + dp[i][j - k] + 1);
                }
            }
        }
    }

    cout << dp[n][m] << endl;
}