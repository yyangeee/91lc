#include <vector>
#include <iostream>
#include <math.h>
#include<numeric>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int total = accumulate(nums.begin(),nums.end(),0);
        if (total < target) {
            return 0;
        } else if ((total - target) & 1) {
            return 0;
        } 
        int key = (total - target) / 2;
        // 转化为凑成key有几种选择
        int length = nums.size();
        vector< vector<int> > dp(length, vector<int>(key +1 , 0));
        if (nums[0] <= key) {
            dp[0][nums[0]] = 1;
        }
        dp[0][0] = (nums[0] != 0) ? 1:2;

        for (int i = 1 ; i < length; i++) {
            dp[i][0] = dp[i-1][0];
            if (nums[i] == 0) {
                dp[i][0] = dp[i-1][0] * 2;
            }
        }
        for (int i = 1 ; i < length ; i++) {
            for (int j = 1 ; j <= key ; j++) {
                if (j >= nums[i]) {
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]];
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        return dp[length-1][key];
    }

    int findTargetSumWays2(vector<int>& nums, int target) {
        int total = accumulate(nums.begin(),nums.end(),0);
        if (total < target) {
            return 0;
        } else if ((total - target) & 1) {
            return 0;
        } 
        int key = (total - target) / 2;
        int length = nums.size();
        vector< vector<int> > dp(length+1, vector<int>(key +1 , 0));    
        dp[0][0] = 1; //表示什么值都不考虑，只有一种情况凑到目标0
        for (int i = 1;i <= length; i++) {
            for (int j = 0; j <= key; j++) {
                dp[i][j] = dp[i-1][j];
                if (j >= nums[i]){
                    dp[i][j] += dp[i-1][j-nums[i-1]];
                }
            }
        }
        return dp[length][key];
    }
};

int main() {
    int a[5] = {1,1,1,1,1};
    std::vector<int> strs(a,a+5);
    int result;
    result = Solution().findTargetSumWays(strs, 3);    
    cout << result << endl;
    return 0;
}