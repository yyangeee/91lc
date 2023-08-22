#include <vector>
#include <string>
#include <iostream>
#include <math.h>
#include<numeric>
using namespace std;

class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int length = stones.size();
        int total = accumulate(stones.begin(), stones.end(), 0);
        int target = total/2;
        vector<int> dp(target+1);
        for (int i = 0; i < length; i++) {
            int x = stones[i];
            for (int j = target; j >= x; j-- ) {
                dp[j] = max(dp[j-x] + x, dp[j]);
            }
        }
        int summinus = dp[target];
        int result = abs(total  - 2*summinus);
        return total;
    }
};

int main() {
    int a[5] = {1,1,4,2,2};
    vector<int> stone(a,a+5);
    int result = Solution().lastStoneWeightII(stone);
    cout << result << endl;
    return 0; 
}