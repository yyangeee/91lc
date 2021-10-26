#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (42.55%)
# Likes:    1391
# Dislikes: 0
# Total Accepted:    192.5K
# Total Submissions: 450.2K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
# 。
# 
# 
# 
# 注意：
# 
# 
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a", t = "a"
# 输出："a"
# 
# 
# 示例 3:
# 
# 
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 和 t 由英文字母组成
# 
# 
# 
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = dict()
        ans = []
        minlength = len(s)+1
        num = len(t)
        for i in range(len(t)):
            map[t[i]] = map.setdefault(t[i],0)-1
        left,match,resleft,resright = 0,0,0,0
        for right in range(0,len(s)):
            if s[right] in map:
                map[s[right]] = map.setdefault(s[right],0)+1
                if map.get(s[right]) <= 0:
                    match += 1
            while match == num:
                if (right-left +1) < minlength:
                    minlength = right-left +1     
                    resleft = left
                    resright = right         
                # 取长度min(len(s)+1,right-left +1) 并保存left：right之间的数据：
                if s[left] in map:
                    map[s[left]] = map.get(s[left])-1
                    if map[s[left]] < 0:
                        match -= 1
                left += 1
        ans = s[resleft : resright + 1] 
        return ans if minlength < len(s)+1 else ""
         
        #if len(ans)<(len(s)+1) else ""

solu = Solution()
solo = solu.minWindow(s = "ADOBECODEBANC", t = "ABC")
print(solo)
# @lc code=end

