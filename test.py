
def intersect(nums1,nums2):
    res = []
    i,j = 0,0
    while i<len(nums1) and j < len(nums2):

        if nums1[i] < nums2[j]:

            res.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            res.append(nums2[j])
            j += 1
        else:
            i += 1
            j += 1
        if i == len(nums1) and j != len(nums2):
            res.append(nums2[j:])
        if j == len(nums2) and i != len(nums1):
            res.append(nums1[i:])
    return res




s1 = [1, 2, 4, 5, 7, 9]
s2 = [1, 2, 5, 6, 9]
print(intersect(s1, s2))