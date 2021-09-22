#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#
# https://leetcode-cn.com/problems/buddy-strings/description/
#
# algorithms
# Easy (30.16%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    27.6K
# Total Submissions: 91.5K
# Testcase Example:  '"ab"\n"ba"'
#
# 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
# 
# 交换字母的定义是取两个下标 i 和 j （下标从 0 开始），只要 i!=j 就交换 A[i] 和 A[j] 处的字符。例如，在 "abcd" 中交换下标
# 0 和下标 2 的元素可以生成 "cbad" 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入： A = "ab", B = "ba"
# 输出： true
# 解释： 你可以交换 A[0] = 'a' 和 A[1] = 'b' 生成 "ba"，此时 A 和 B 相等。
# 
# 示例 2：
# 
# 
# 输入： A = "ab", B = "ab"
# 输出： false
# 解释： 你只能交换 A[0] = 'a' 和 A[1] = 'b' 生成 "ba"，此时 A 和 B 不相等。
# 
# 
# 示例 3:
# 
# 
# 输入： A = "aa", B = "aa"
# 输出： true
# 解释： 你可以交换 A[0] = 'a' 和 A[1] = 'a' 生成 "aa"，此时 A 和 B 相等。
# 
# 示例 4：
# 
# 
# 输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
# 
# 
# 示例 5：
# 
# 
# 输入： A = "", B = "aa"
# 输出： false
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# A 和 B 仅由小写字母构成。
# 
# 
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            stest = set()
            for a in s:
                if a in stest:
                    return True
                stest.add(a)
            return False

        pair = []
        for a,b in zip(s,goal):
            if a != b:
                pair.append((a,b))
        if len(pair) >2:
            return False

        return len(pair) == 2 and pair[0] == pair[1][::-1]

            
# @lc code=end

