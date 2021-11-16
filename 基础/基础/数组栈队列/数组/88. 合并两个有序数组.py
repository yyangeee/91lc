class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left,right = 0,0
        total = []
        while left < m or right < n:
            if left == m:
                total.append(nums2[right])
                right += 1
            elif right == n:
                total.append(nums1[left])
                left += 1            
            elif nums1[left] < nums2[right]:
                total.append(nums1[left])
                left += 1
            else:
                total.append(nums2[right])
                right += 1
        print(total)
        return total
        # nums1[:] = total  题目就得这么输出

