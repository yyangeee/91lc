//#include <string.h>
#include <vector>
#include <iostream>
#include <math.h>
#include<numeric>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total = accumulate(nums.begin(), nums.end(), 0);
        int target = total/2;
        int length = nums.size();
        if (2*target != total) return false;
        vector< vector<bool> > dp(length, vector<bool>(target+1, false));

        for (int k = 0; k < length; k++) {
            dp[k][0] = true;
        }
        dp[0][0] = true;
        if (target > nums[0]) dp[0][target] = true;
        for (int i = 1; i < length; i++) {
            for (int j = 1; j <= target; j++) {
                if (j < nums[i]) continue;
                dp[i][j] = (dp[i-1][j] == true)||(dp[i-1][j-nums[i]] == true) ? true : false;
            }
        }
        return dp[length][target] == true;
    }
};

int main() {
    int a[4] = {1,5,11,5};
    std::vector<int> nums(a,a+4);
    bool result;
    result = Solution().canPartition(nums);    
    cout << result << endl;
    return 0;
//调试+背包
}
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) {
            return false;
        }
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int maxNum = *max_element(nums.begin(), nums.end());
        if (sum & 1) {
            return false;
        }
        int target = sum / 2;
        if (maxNum > target) {
            return false;
        }
        vector<vector<int>> dp(n, vector<int>(target + 1, 0));
        for (int i = 0; i < n; i++) {
            dp[i][0] = true;
        }
        dp[0][nums[0]] = true;
        for (int i = 1; i < n; i++) {
            int num = nums[i];
            for (int j = 1; j <= target; j++) {
                if (j >= num) {
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        return dp[n - 1][target];
    }
};

作者：力扣官方题解
链接：https://leetcode.cn/problems/partition-equal-subset-sum/solutions/442320/fen-ge-deng-he-zi-ji-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。