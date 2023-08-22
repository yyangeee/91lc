#include <vector>
#include <string>
#include <iostream>
#include <math.h>
#include<numeric>
using namespace std;

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int length = coins.size();
        vector< vector<int> > dp(length+1, vector<int> (amount+1, 0));
        dp[0][0] = 1;
        for (int i = 1 ; i <= length; i++) {
            int x = coins[i-1];
            for (int j = 0; j <= amount; j++) {
                dp[i][j] = dp[i-1][j];
                for (int k = 1; k * x <= j ; k++) {
                    dp[i][j] += dp[i-1][j - k*x];
                }
            }
        }
        return dp[length][amount];
    }
};

int main() {
    int a[3] = {1,2,5};
    vector<int> coin(a,a+3);
    int result;
    result = Solution().change(5,coin);
    cout << result << endl;
    return 0;
}