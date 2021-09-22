#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (41.94%)
# Likes:    1211
# Dislikes: 0
# Total Accepted:    163.4K
# Total Submissions: 389.7K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,0]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,4,-1,1]
# 输出：2
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [7,8,9,11,12]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -2^31 
# 
# 
#官方题解

# @lc code=start

from typing import List


class Solution:

    # 3 应该放在索引为 2 的地方
    # 4 应该放在索引为 3 的地方

    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                self.__swap(nums, i, nums[i] - 1)

        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1

        return size + 1

    def __swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]

# @lc code=end

