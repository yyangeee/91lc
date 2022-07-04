# 剑指 Offer 42. 连续子数组的最大和
https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
## 思路
前缀和法计算当前元素及其前方所有元素的和，减去前方区间最小的和，可以得到解
## 学到的语法
float("-inf")负无穷

## 代码
```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minn = 0
        ans = float("-inf")
        prenum = 0
        for i in range(len(nums)):
            prenum += nums[i]
            ans = max(ans, prenum - minn)
            if prenum<minn:
                minn = prenum
        return ans

```

## 复杂度

https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/solution/cong-bao-li-po-jie-dao-dong-tai-gui-hua-yfvkp/
动态规划
从左到右计算每个元素的最大和
递推 当前元素是否加上前面的值
```py
class Solution {
    public int maxSubArray(int[] nums) {
        int[] dp = new int[nums.length];

        int max = nums[0];
        dp[0] = nums[0];

        for (int i=1; i<nums.length; i++) {
            dp[i] = Math.max(dp[i-1], 0) + nums[i];
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}
```