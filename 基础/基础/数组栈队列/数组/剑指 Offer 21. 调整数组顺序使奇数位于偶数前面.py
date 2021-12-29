
#不改变奇数顺序
https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
class Solution:
    def exchange(self, nums) :
        left = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                if i == 0:
                    continue
                while nums[left] % 2 == 1 and left < i:
                    left += 1
                if nums[left] % 2 == 0:
                    nums[i] , nums[left] = nums[left],nums[i]
                    left += 1
        return nums
 

class Solution1:
    def exchange(self, nums) :
        total = 0
        for i in range(len(nums)):
            
            if nums[i] % 2 == 1:
                total += 1
                tmp = nums[i]
                k = i
                if i == 0:
                    
                    continue
                while total <= k:
                    nums[k] = nums[k-1]
                    k -= 1
                nums[total-1] = tmp
        return nums
ss = Solution1()
str = [1,2,3,4,5,6,7]
print(ss.exchange(str))

            
